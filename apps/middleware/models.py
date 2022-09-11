from django.db import models


class SimpleLogger(models.Model):
    username = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    count_of_visits = models.PositiveIntegerField(default=0)
    last_visit = models.DateTimeField()


# Create your models here.
