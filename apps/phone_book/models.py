# !!!!! импорт должен быть не напрямую(core.settings), а:
from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    contact_name = models.CharField(max_length=255, null=False, unique=True)
    phone_value = PhoneNumberField(null=False, blank=False, unique=True)
    # что бы сослаться на модель кастомного юзера:  !!!settings.AUTH_USER_MODEL!!!
    creator_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"ИМЯ {self.contact_name} Телефон {self.phone_value}"
