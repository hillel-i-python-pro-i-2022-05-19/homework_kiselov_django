# Generated by Django 4.0.6 on 2022-07-18 18:16

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("contact_name", models.CharField(max_length=255)),
                (
                    "phone_value",
                    phonenumber_field.modelfields.PhoneNumberField(
                        help_text="Phone number", max_length=128, region=None, unique=True
                    ),
                ),
            ],
        ),
    ]
