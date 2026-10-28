from django.contrib import admin
from .models import Round, Question, Choice, Attempt


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4
    max_num = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    list_display = ['round_number', 'title', 'is_active', 'created_at']
    list_editable = ['is_active']
    ordering = ['round_number']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'round', 'order', 'text']
    list_filter = ['round']
    ordering = ['round__round_number', 'order']
    inlines = [ChoiceInline]


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'round', 'score', 'total', 'completed_at']
    list_filter = ['round']
    readonly_fields = ['completed_at']


