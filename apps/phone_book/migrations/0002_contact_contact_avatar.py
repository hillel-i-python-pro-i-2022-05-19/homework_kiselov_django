# Generated by Django 4.0.6 on 2022-08-27 10:46

import apps.phone_book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_avatar',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=apps.phone_book.models.get_icon_path, verbose_name='Avatar'),
        ),
    ]
