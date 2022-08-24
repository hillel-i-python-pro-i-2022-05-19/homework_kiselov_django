from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateForm(forms.Form):
    contact_name = forms.CharField(
        label="contact_name",
    )
    phone_value = PhoneNumberField(label="contact_value")
