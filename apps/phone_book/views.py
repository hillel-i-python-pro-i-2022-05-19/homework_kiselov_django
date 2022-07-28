from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Contact
import

def main_page(request: HttpRequest) -> HttpResponse:
    print(environ)
    return render(request, 'phone_book/base.html')


def reader(request: HttpRequest) -> HttpResponse:
    result = Contact.objects.all()
    return render(request, 'phone_book/reader.html', {'data': result})
