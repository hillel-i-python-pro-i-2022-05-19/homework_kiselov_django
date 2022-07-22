from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .forms import CreateForm, DeleteForm, UpdateForm, UpdateTempForm
from .models import Contact


def creator(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("contact_name")
            phone = form.cleaned_data.get("phone_value")
            if not (Contact.objects.filter(contact_name=name) or Contact.objects.filter(phone_value=phone)):
                Contact.objects.create(contact_name=name, phone_value=phone)
                return HttpResponse("Новый контакт успешно добавлен")
            else:
                raise ValueError("Контакт с таким именем или номером телефона уже существует")
    else:
        form = CreateForm()
    return render(request, 'Phone_book/creator.html', {'form': form})


def reader(request: HttpRequest) -> HttpResponse:
    result = Contact.objects.all()
    return render(request, 'Phone_book/reader.html', {'data': result})


def updatortemp(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        update_form = UpdateTempForm(request.POST)
        if update_form.is_valid():
            name_to_update = update_form.cleaned_data.get("contact_name")
            result = Contact.objects.filter(contact_name=name_to_update).values()[0]
            if result:
                return render(request, 'Phone_book/read_one.html', {'data': result})
            else:
                return HttpResponse("Записи с данным именем не существует")
    else:
        update_form = UpdateTempForm()
        return render(request, 'Phone_book/updator.html', {'form': update_form})


def updator(request: HttpRequest, name: str) -> HttpResponse:
    if request.method == "POST":
        update_form = UpdateForm(request.POST)
        if update_form.is_valid():
            print("ИМЯ:", name)
            new_name = update_form.cleaned_data.get("contact_name")
            new_phone = update_form.cleaned_data.get("phone_value")
            if Contact.objects.filter(contact_name=name):
                Contact.objects.filter(contact_name=name).update(contact_name=new_name, phone_value=new_phone)
                return HttpResponse("Контакт успешно изменён")
            else:
                return HttpResponse("Такого контакта нет")
    else:
        update_form = UpdateForm()
    return render(request, 'Phone_book/creator.html', {'form': update_form})


def deleter(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        del_form = DeleteForm(request.POST)
        if del_form.is_valid():
            name = del_form.cleaned_data.get("name_to_del")
            if Contact.objects.filter(contact_name=name):
                Contact.objects.filter(contact_name=name).delete()
                return HttpResponse("Контакт удалён")
            else:
                return HttpResponse("Контакта с таким именем не существует")
    else:
        del_form = DeleteForm()
    return render(request, 'Phone_book/deleter.html', {'form': del_form})
