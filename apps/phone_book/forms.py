from django import forms
from phonenumber_field.formfields import PhoneNumberField
from apps.phone_book.models import Contact, Detail,Tag
from django.forms.models import inlineformset_factory,BaseInlineFormSet
from .contact_validator import contact_validator
from django.core.exceptions import ValidationError



class DetailForm(forms.ModelForm):
    class Meta:
        model =  Detail
        fields = (
            "contact_type",
            "contact_value",
            "contact"
        )

    def clean(self):
        cleaned_data = super(DetailForm, self).clean()
        if contact_validator(cleaned_data.get("contact_type"), cleaned_data.get("contact_value")) == False:
            raise ValidationError(f'{cleaned_data.get("contact_type")} введён некорректно')

        return cleaned_data




class CreateForm(forms.ModelForm):
    details = forms.ModelMultipleChoiceField(Detail.objects.filter(contact=None))
    class Meta:
        model = Contact
        fields = (
            "contact_name",
            "birthday",
            "tags",
            "contact_avatar",
            "creator",
            "details"
        )


class UpdateForm(forms.ModelForm):
    details = forms.ModelMultipleChoiceField(Detail.objects.all())
    class Meta:
        model = Contact
        fields = (
            "contact_name",
            "birthday",
            "tags",
            "contact_avatar",
            "creator",
            "details"
        )





