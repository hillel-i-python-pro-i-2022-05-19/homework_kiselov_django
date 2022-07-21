from django import forms
from phonenumber_field.formfields import PhoneNumberField


class CreateForm(forms.Form):
    contact_name = forms.CharField(label='Имя', max_length=100, required=False)
    phone_value = PhoneNumberField(label=("Номер телефона"), required=False)


class DeleteForm(forms.Form):
    name_to_del = forms.CharField(label='Введите имя, которое хотите удалить', max_length=100, required=False)


class UpdateTempForm(forms.Form):
    contact_name = forms.CharField(label='Введите имя, которое хотите изменить', max_length=100, required=False)


class UpdateForm(forms.Form):
    contact_name = forms.CharField(label='Введите новое имя', max_length=100, required=False)
    phone_value = PhoneNumberField(label=("Введите новый номер телефона"), required=False)
