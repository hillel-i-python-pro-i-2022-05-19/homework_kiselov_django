# Register your models here.
from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

from .contact_validator import contact_validator
from .models import Contact, Tag
from .models import ContactDetail


class ContactDetailForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = ['contact_type', 'contact_value']

    def clean(self):
        cleaned_data = super(ContactDetailForm, self).clean()

        if contact_validator(cleaned_data.get("contact_type"), cleaned_data.get("contact_value")) == False:
            raise ValidationError(f'{cleaned_data.get("contact_type")} введён некорректно')

        return cleaned_data


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'birthday']


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['tag']


@admin.register(ContactDetail)
class ContactAdmin(admin.ModelAdmin):
    form = ContactDetailForm
    list_display = ['contact_type', 'contact_value']
