from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Round, Question, Choice, Attempt


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'text', 'option_label']


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'order', 'choices']


class RoundListSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField()
    attempted = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    class Meta:
        model = Round
        fields = ['id', 'round_number', 'title', 'description', 'question_count', 'attempted', 'score']

    def get_question_count(self, obj):
        return obj.questions.count()

    def get_attempted(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            return Attempt.objects.filter(user=request.user, round=obj).exists()
        return False

    def get_score(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user') and request.user.is_authenticated:
            attempt = Attempt.objects.filter(user=request.user, round=obj).order_by('-completed_at').first()
            if attempt:
                return attempt.score
        return None


class RoundDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    question_count = serializers.SerializerMethodField()

    class Meta:
        model = Round
        fields = ['id', 'round_number', 'title', 'description', 'question_count', 'questions']

    def get_question_count(self, obj):
        return obj.questions.count()


class AttemptSerializer(serializers.ModelSerializer):
    round_number = serializers.ReadOnlyField(source='round.round_number')
    correct_answers = serializers.SerializerMethodField()
    incorrect_answers = serializers.SerializerMethodField()

    class Meta:
        model = Attempt
        fields = ['id', 'round', 'round_number', 'score', 'total', 'correct_answers', 'incorrect_answers', 'completed_at']

    def get_correct_answers(self, obj):
        return obj.score

    def get_incorrect_answers(self, obj):
        return obj.total - obj.score


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_fields = ['id']


