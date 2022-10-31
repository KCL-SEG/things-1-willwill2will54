from django.db import models

class Thing(models.Model):
    """Thing model, model of a thing"""
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
