from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('create/', views.creator, name='contactcreator'),
    path('read/', views.reader, name='contactreader'),
    path('update/', views.updatertemp, name='contactupdator_temp'),
    path('update/<str:name>', views.updater, name='contactupdater'),
    path('delete/', views.deletertemp, name='contactdeleter_temp'),
    path('delete/<str:name>', views.deleter, name='contactdeleter'),
    path('delete_final/<str:name>', views.deleter_final, name='contactdeleter_final')
]
