from django.db import models
from django.forms import CharField


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
