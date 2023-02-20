import logging

from django.core.management.base import BaseCommand
from apps.contact_generator.models import Contact
from apps.contact_generator.services.generate_contacts import generate_of_contacts


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--amount",
            help="How many animals do you want to generate?",
            type=int,
            default=10,
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        logger = logging.getLogger("django")

        queryset = Contact.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        for data in generate_of_contacts(amount=amount, is_auto_generated=True):
            data.save()
        logger.info(f"Current amount of contacts after: {queryset.count()}")
