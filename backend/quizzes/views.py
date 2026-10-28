from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Round, Question, Choice, Attempt
from .serializers import (
    RoundListSerializer, RoundDetailSerializer, QuestionSerializer,
    ChoiceSerializer, AttemptSerializer, UserSerializer
)


class RoundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Round.objects.filter(is_active=True).order_by('round_number')
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return RoundListSerializer
        return RoundDetailSerializer
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def submit(self, request, pk=None):
        round_obj = self.get_object()
        answers = request.data.get('answers', {})  # question_id -> choice_id
        questions = round_obj.questions.all()
        total = questions.count()
        score = 0

        for question in questions:
            choice_id = answers.get(str(question.id)) or answers.get(question.id)
            if choice_id:
                try:
                    choice = question.choices.get(id=choice_id)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

        attempt = Attempt.objects.create(user=request.user, round=round_obj, score=score, total=total)
        serializer = AttemptSerializer(attempt)
        correct = score
        incorrect = total - score
        return Response({
            'score': score,
            'total': total,
            'correct_answers': correct,
            'incorrect_answers': incorrect,
            'round_number': round_obj.round_number,
            'attempt': serializer.data
        }, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def my_attempt(self, request, pk=None):
        round_obj = self.get_object()
        attempts = Attempt.objects.filter(user=request.user, round=round_obj).order_by('-completed_at')
        if attempts.exists():
            attempt = attempts.first()
            serializer = AttemptSerializer(attempt)
            return Response(serializer.data)
        return Response({'attempted': False})


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [IsAuthenticated]


class AttemptViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AttemptSerializer
    permission_classes = [IsAuthenticated]
    queryset = Attempt.objects.none()

    def get_queryset(self):
        return Attempt.objects.filter(user=self.request.user).order_by('-completed_at')





@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user': UserSerializer(user).data}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Please enter username and password'}, status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})
    return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    return Response(UserSerializer(request.user).data)


