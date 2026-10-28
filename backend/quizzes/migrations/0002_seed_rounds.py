from django.db import migrations

from quizzes.seed_data import ROUNDS


def seed_rounds(apps, schema_editor):
    Round = apps.get_model('quizzes', 'Round')
    Question = apps.get_model('quizzes', 'Question')
    Choice = apps.get_model('quizzes', 'Choice')

    for round_data in ROUNDS:
        round_obj, _ = Round.objects.update_or_create(
            round_number=round_data['round_number'],
            defaults={
                'title': round_data['title'],
                'description': round_data['description'],
                'is_active': True,
            },
        )

        for order, question_data in enumerate(round_data['questions'], start=1):
            question, _ = Question.objects.update_or_create(
                round=round_obj,
                order=order,
                defaults={'text': question_data['text']},
            )
            for label, (choice_text, is_correct) in zip('ABCD', question_data['choices']):
                Choice.objects.update_or_create(
                    question=question,
                    option_label=label,
                    defaults={'text': choice_text, 'is_correct': is_correct},
                )


def unseed_rounds(apps, schema_editor):
    Round = apps.get_model('quizzes', 'Round')
    Round.objects.filter(round_number__in=range(2, 11)).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_rounds, unseed_rounds),
    ]
