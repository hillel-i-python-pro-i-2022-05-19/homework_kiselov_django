from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from .models import Contact
from django.views import View
from .forms import CreateForm
from django.shortcuts import render


class MainpageView(TemplateView):
    template_name = "phone_book/base.html"


class ReaderView(ListView):
    model = Contact
    template_name = "phone_book/reader.html"


class DeleterListView(ListView):
    model = Contact
    template_name = "phone_book/deleter.html"


class DeleterView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contactdeleter_temp")
    template_name = "phone_book/contact_confirm_delete.html"


class CreatorView(View):
    model = Contact
    template_name = "phone_book/creator.html"
    fields = ["contact_name", "phone_value"]
    success_url = reverse_lazy("contactcreator")
    initial = {"key": "value"}
    form_class = CreateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact_name = form.data.get("contact_name")
            phone_value = form.data.get("phone_value")
            creator_name = request.user
            Contact.objects.create(contact_name=contact_name, phone_value=phone_value, creator_name=creator_name)

        return render(request, self.template_name, {"form": form})


class UpdaterListView(ListView):
    model = Contact
    template_name = "phone_book/updater.html"


class UpdaterView(UpdateView):
    model = Contact
    template_name = "phone_book/updater_final.html"
    fields = ["contact_name", "phone_value"]
    success_url = reverse_lazy("contactupdater_temp")
