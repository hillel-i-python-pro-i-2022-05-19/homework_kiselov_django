from django.contrib import admin
from .models import SimpleLogger


@admin.register(SimpleLogger)
class SimpleLoggerAdmin(admin.ModelAdmin):
    list_display = ["username", "url", "count_of_visits", "last_visit"]
