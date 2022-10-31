from enum import unique
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Thing(models.Model):
    """Thing model, model of a thing"""
    name = models.CharField(max_length=30, blank=False, unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.PositiveSmallIntegerField(
        validators = [
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
