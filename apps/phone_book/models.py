from datetime import datetime

from django.db import models


class ContactTypeChoices(models.TextChoices):
    PHONE = 'Phone', 'phones'
    EMAIL = 'email', 'Email'
    TELEGRAM = 'Telegram', 'telegram'
    LINKEDIN = 'LinkedIn', 'Linkedin'



class Tag(models.Model):
    tag = models.CharField('tag', help_text='tag_name', max_length=255)

    def __str__(self) -> str:
        return f'{self.tag}'

    __repr__ = __str__


class Contact(models.Model):
    contact_name = models.CharField('Name', help_text='Contact_name', max_length=255, null=False, unique=True)
    birthday = models.DateField('Birth', help_text='date_of_birth', default=datetime.strptime('20/07/1998', "%d/%m/%Y"))
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self) -> str:
        return f'{self.contact_name} - {self.birthday}'

    __repr__ = __str__


class ContactDetail(models.Model):
    contact_type = models.CharField('Contact_type', max_length=255, choices=ContactTypeChoices.choices,
                                    default=ContactTypeChoices.PHONE)
    contact_value = models.CharField('Contact_value', max_length=255, unique=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="contact")

    def __str__(self):
        return f'{self.contact_type} - {self.contact_value}'
