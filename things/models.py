from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model, CharField, IntegerField


class Thing(Model):

    name: CharField = CharField(max_length=30, blank=False, unique=True)
    description: CharField = CharField(max_length=120, blank=True)
    quantity: IntegerField = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
