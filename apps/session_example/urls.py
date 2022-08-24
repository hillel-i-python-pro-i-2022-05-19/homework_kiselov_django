from django.urls import path
from .views import SessionExample


urlpatterns = [
    path("", SessionExample.as_view(), name="session"),
]
