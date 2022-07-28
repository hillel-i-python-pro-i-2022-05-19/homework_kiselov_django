# Generated by Django 4.0.6 on 2022-07-28 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0002_alter_contact_contact_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdetail',
            name='contact_type',
            field=models.CharField(choices=[('Phone', 'phones'), ('email', 'Email'), ('Telegram', 'telegram'), ('LinkedIn', 'Linkedin')], default='Phone', max_length=255, verbose_name='Contact_type'),
        ),
        migrations.AlterField(
            model_name='contactdetail',
            name='contact_value',
            field=models.CharField(max_length=255, unique=True, verbose_name='Contact_value'),
        ),
    ]
