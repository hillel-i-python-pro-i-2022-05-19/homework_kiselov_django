from .models import Contact
from django.views.generic import TemplateView, ListView, DeleteView, CreateView, UpdateView
from .models import Contact
from django.urls import reverse_lazy


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


class CreatorView(CreateView):
    model = Contact
    template_name = "phone_book/creator.html"
    fields = ["contact_name", "phone_value"]
    success_url = reverse_lazy("contactcreator")


class UpdaterListView(ListView):
    model = Contact
    template_name = "phone_book/updater.html"


class UpdaterView(UpdateView):
    model = Contact
    template_name = "phone_book/updater_final.html"
    fields = ["contact_name", "phone_value"]
    success_url = reverse_lazy("contactupdater_temp")
