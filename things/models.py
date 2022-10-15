from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models import Model, CharField, PositiveIntegerField


class Thing(Model):

    name: CharField = models.CharField(max_length=30, blank=False, unique=True)
    description: CharField = models.CharField(max_length=120, blank=True)
    quantity: PositiveIntegerField = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
