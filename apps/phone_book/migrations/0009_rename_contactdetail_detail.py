# Generated by Django 4.0.6 on 2022-09-04 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("phone_book", "0008_alter_contactdetail_contact"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ContactDetail",
            new_name="Detail",
        ),
    ]