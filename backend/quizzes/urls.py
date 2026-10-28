from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoundViewSet, QuestionViewSet, ChoiceViewSet, AttemptViewSet, register, login_view, me

router = DefaultRouter()
router.register(r'rounds', RoundViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'attempts', AttemptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', register),
    path('auth/login/', login_view),
    path('auth/me/', me),
]

