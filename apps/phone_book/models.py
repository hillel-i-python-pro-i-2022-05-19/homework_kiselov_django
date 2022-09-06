# !!!!! импорт должен быть не напрямую(core.settings), а:
import uuid
from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime



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



# функция для определения пути
def get_icon_path(instance,filename:str)->str:
#     Мы хотим усложнить поиск файла(для юзера) и что бы не сохранялось оригинальное название файла
    _, extension = filename.rsplit('.', maxsplit=1)
    # вернуть путь, куда мы это положим:
    return f"phone_book/avatars/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"



class Contact(models.Model):
    contact_name = models.CharField('Name', help_text='Contact_name', max_length=255, null=False, unique=True)
    birthday = models.DateField('Birth', help_text='date_of_birth', default=datetime.strptime('20/07/1998', "%d/%m/%Y"))
    tags = models.ManyToManyField(Tag, related_name="tags")

    # что бы сослаться на модель кастомного юзера:  !!!settings.AUTH_USER_MODEL!!!
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    contact_avatar = models.ImageField('Avatar',
                                       # куда заливать:
                                       upload_to=get_icon_path,
                                       # максимальный размер пути к файлу:
                                       max_length=255,
                                       blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.contact_name} - {self.birthday}, create by {self.creator}'

    __repr__ = __str__



class Detail(models.Model):
    contact_type = models.CharField('Contact_type', max_length=255, choices=ContactTypeChoices.choices,
                                    default=ContactTypeChoices.PHONE)
    contact_value = models.CharField('Contact_value', max_length=255, unique=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="detail", null=True, blank=True)

    def __str__(self):
        return f'{self.contact_type} - {self.contact_value}'







# # функция для определения пути
# def get_icon_path(instance,filename:str)->str:
# #     Мы хотим усложнить поиск файла(для юзера) и что бы не сохранялось оригинальное название файла
#     _, extension = filename.rsplit('.', maxsplit=1)
#     # вернуть путь, куда мы это положим:
#     return f"phone_book/avatars/{instance.pk}/{uuid.uuid4()}/avatar.{extension}"

# class Contact(models.Model):
#     contact_name = models.CharField(max_length=255, null=False, unique=True)
#     phone_value = PhoneNumberField(null=False, blank=False, unique=True)
#     # что бы сослаться на модель кастомного юзера:  !!!settings.AUTH_USER_MODEL!!!
#     creator_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#     contact_avatar = models.ImageField('Avatar',
#                                        # куда заливать:
#                                        upload_to= get_icon_path,
#                                        # максимальный размер пути к файлу:
#                                        max_length=255,
#                                        blank=True, null=True)
#
#     def __str__(self):
#         return f"ИМЯ {self.contact_name} Телефон {self.phone_value} АВАТАР {self.contact_avatar}"









# pillow - библиотека для работы с изображениями
