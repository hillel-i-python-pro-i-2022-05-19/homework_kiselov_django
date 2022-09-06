from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import MainpageView, ReaderView, DeleterView, CreatorView, DeleterListView, UpdaterListView, UpdaterView, \
    TagsCreatorView, DetailsCreatorView

urlpatterns = [
    path("", MainpageView.as_view(), name="main_page"),
    path("create_contact/", login_required(CreatorView.as_view()), name="contactcreator"),
    path("read_contact/", ReaderView, name="contactreader"),
    path("update_contact/", login_required(UpdaterListView.as_view()), name="contactupdater_temp"),
    path("update_contact/<int:pk>", UpdaterView.as_view(), name="contactupdater"),
    path("delete_contact/", login_required(DeleterListView.as_view()), name="contactdeleter_temp"),
    path("delete_contact/<int:pk>", DeleterView.as_view(), name="contactdeleter"),
    path("create_new_tags/", TagsCreatorView.as_view(), name="tagscreator"),
    path("create_new_details/", DetailsCreatorView.as_view(), name="detailscreator"),
]
