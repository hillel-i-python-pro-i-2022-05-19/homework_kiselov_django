from django.core.management.base import BaseCommand, CommandError
from apps.phone_book.models import Contact
from faker import Faker
import logging
from typing import Iterator

faker = Faker()


def contact_generator(amount_of_contacts) -> Iterator[Contact]:
    for _ in range(amount_of_contacts):
        contact = Contact(
            contact_name=faker.name(),
            phone_value=faker.phone_number(),
        )
        contact.save()
        yield contact


class Command(BaseCommand):
    help = "Create contact"

    def add_arguments(self, parser):
        parser.add_argument("amount", type=int)

    def handle(self, *args, **options):
        amount_of_contact = options["amount"]

        logger = logging.getLogger("create_contacts")

        logger.info(f"Amount of contacts before: {Contact.objects.count()}")

        generator_object = contact_generator(amount_of_contact)
        for el in generator_object:
            print(el)
        # contact_list = [f'{el.contact_name}{el.phone_value}' for el in generator_object]

        logger.info(f"Amount of contacts after: {Contact.objects.count()}")
