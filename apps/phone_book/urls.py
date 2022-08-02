from django.urls import path

from .views import MainpageView, ReaderView, DeleterView, CreatorView, DeleterListView, UpdaterListView, UpdaterView

urlpatterns = [
    path('', MainpageView.as_view(), name='main_page'),
    path('create_contact/', CreatorView.as_view(), name='contactcreator'),
    path('read_contact/', ReaderView.as_view(), name='contactreader'),
    path('update_contact/', UpdaterListView.as_view(), name='contactupdater_temp'),
    path('update_contact/<int:pk>', UpdaterView.as_view(), name='contactupdater'),
    path('delete_contact/', DeleterListView.as_view(), name='contactdeleter_temp'),
    path('delete_contact/<int:pk>', DeleterView.as_view(), name='contactdeleter'),
]
