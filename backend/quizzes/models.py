from django.db import models
from django.contrib.auth.models import User


class Round(models.Model):
    round_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200, default='Round')
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['round_number']

    def __str__(self):
        return f"Round {self.round_number} - {self.title}"


class Question(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"Round {self.round.round_number} - Q{self.order}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    option_label = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')], blank=True)

    def __str__(self):
        return f"{self.option_label or ''} {self.text}"


class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    round = models.ForeignKey(Round, on_delete=models.CASCADE, related_name='attempts')
    score = models.IntegerField(default=0)
    total = models.IntegerField(default=10)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-completed_at']

    def __str__(self):
        return f"{self.user.username} - Round {self.round.round_number} ({self.score}/{self.total})"


