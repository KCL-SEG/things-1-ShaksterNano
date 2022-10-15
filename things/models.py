from django.db import models
from django.db.models import Model, CharField, IntegerField


class Thing(Model):

    name: CharField = models.CharField()
    description: CharField = models.CharField()
    quantity: IntegerField = models.IntegerField()
