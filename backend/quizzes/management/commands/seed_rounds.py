from django.core.management.base import BaseCommand
from django.db import transaction

from quizzes.models import Choice, Question, Round
from quizzes.seed_data import ROUNDS


class Command(BaseCommand):
    help = 'Create or update the ten quiz rounds with their questions and choices.'

    @transaction.atomic
    def handle(self, *args, **options):
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

        self.stdout.write(self.style.SUCCESS(
            f'Seeded {len(ROUNDS)} rounds with 10 questions each.'
        ))
