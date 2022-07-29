from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    contact_name = models.CharField(max_length=255, null=False, unique=True)
    phone_value = PhoneNumberField(null=False, blank=False,
                                   unique=True)

    def __str__(self):
        return f'ИМЯ {self.contact_name} Телефон {self.phone_value}'
