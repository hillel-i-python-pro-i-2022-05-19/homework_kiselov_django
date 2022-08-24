from django.shortcuts import render  # noqa: F401
from django.views import generic
from apps.users.forms import SignUpForm
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "users/register.html"


# Create your views here.
