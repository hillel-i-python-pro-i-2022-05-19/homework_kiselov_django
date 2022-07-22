from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.creator, name='contactcreator'),
    path('read/', views.reader, name='contactreader'),
    path('update/', views.updatortemp, name='contactupdator'),
    path('update/<str:name>', views.updator, name='contactupdator'),
    path('delete/', views.deleter, name='contactdeleter'),
]
