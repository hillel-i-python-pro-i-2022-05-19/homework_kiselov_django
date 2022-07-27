from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('create_contact/', views.creator, name='contactcreator'),
    path('read_contact/', views.reader, name='contactreader'),
    path('update_contact/', views.updatertemp, name='contactupdater_temp'),
    path('update_contact/<str:name>', views.updater, name='contactupdater'),
    path('delete_contact/', views.deletertemp, name='contactdeleter_temp'),
    path('delete_contact/<str:name>', views.deleter, name='contactdeleter'),
    path('delete_contact_final/<str:name>', views.deleter_final, name='contactdeleter_final')
]
