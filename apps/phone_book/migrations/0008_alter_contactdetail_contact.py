# Generated by Django 4.0.6 on 2022-08-31 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("phone_book", "0007_alter_contactdetail_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactdetail",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contact",
                to="phone_book.contact",
            ),
        ),
    ]
