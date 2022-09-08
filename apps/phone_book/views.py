from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, CreateView
from .models import Contact, Tag, Detail
from django.views import View
from .forms import CreateForm, DetailForm, UpdateForm
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .query_to_dict import querydict_to_dict


class MainpageView(TemplateView):
    template_name = "phone_book/base.html"


def ReaderView(request: HttpRequest) -> HttpResponse:
    result = Contact.objects.all()
    values = Detail.objects.all()
    return render(request, "phone_book/reader.html", {"data": result, "values": values})


class DeleterListView(ListView):
    model = Contact
    template_name = "phone_book/deleter.html"


class DeleterView(DeleteView):
    model = Contact
    success_url = reverse_lazy("contactdeleter_temp")
    template_name = "phone_book/contact_confirm_delete.html"


class CreatorView(View):
    model = Contact
    template_name = "phone_book/contact_form.html"
    success_url = reverse_lazy("contactcreator")
    initial = {"key": "value"}
    form_class1 = CreateForm

    def get(self, request, *args, **kwargs):
        form1 = self.form_class1(initial=self.initial)
        return render(request, self.template_name, {"form1": form1})

    def post(self, request):
        form1 = self.form_class1(request.POST, request.FILES, initial=self.initial)
        if form1.is_valid():
            contact = form1.save()
            tags = querydict_to_dict(request.POST).get("tags")
            for tag in tags:
                contact.tags.add(tag)

            details_form = querydict_to_dict(request.POST).get("details")

            for detail_id in details_form:
                detail = Detail.objects.get(id=detail_id)
                Detail.objects.filter(id=detail_id).delete()
                contact.detail.create(
                    id=detail_id, contact_type=detail.contact_type, contact_value=detail.contact_value, contact=contact
                )

            contact.creator = request.user
            contact.save()
        return render(request, self.template_name, {"form1": form1})


class UpdaterListView(ListView):
    model = Contact
    template_name = "phone_book/updater.html"


class UpdaterView(UpdateView):
    model = Contact
    template_name = "phone_book/updater_final.html"
    # fields = ["contact_name"]
    form_class = UpdateForm
    success_url = reverse_lazy("contactupdater_temp")


class TagsCreatorView(CreateView):
    model = Tag
    fields = ["tag"]
    template_name = "phone_book/tags_creator.html"
    success_url = reverse_lazy("contactcreator")


class DetailsCreatorView(CreateView):
    model = Detail
    form_class = DetailForm
    template_name = "phone_book/details_creator.html"
    success_url = reverse_lazy("contactcreator")
