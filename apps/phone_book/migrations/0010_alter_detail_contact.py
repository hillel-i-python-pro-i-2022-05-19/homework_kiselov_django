# Generated by Django 4.0.6 on 2022-09-09 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("phone_book", "0009_rename_contactdetail_detail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detail",
            name="contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="detail",
                to="phone_book.contact",
            ),
        ),
    ]
