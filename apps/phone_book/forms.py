from django import forms


class CreateForm(forms.Form):
    contact_name = forms.CharField(
        label="contact_name",
    )
