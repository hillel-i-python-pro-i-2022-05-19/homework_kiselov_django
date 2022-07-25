from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateForm(forms.Form):
    contact_name = forms.CharField(label='Имя', max_length=100, required=False)
    phone_value = PhoneNumberField(label=("Номер телефона"), required=False)


class UpdateForm(forms.Form):
    contact_name = forms.CharField(label='Введите новое имя', max_length=100, required=False)
    phone_value = PhoneNumberField(label=("Введите новый номер телефона"), required=False)
