from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Contact, ContactDetail


def main_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'phone_book/base.html')


def reader(request: HttpRequest) -> HttpResponse:
    result = Contact.objects.all()
    values = ContactDetail.objects.all()
    return render(request, 'phone_book/reader.html', {'data': result, 'values': values})
