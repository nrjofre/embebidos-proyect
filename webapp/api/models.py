from django.db import models
from django.contrib.auth.models import User

# Create your models here.
SLOT_CHOICES = (
        (1, 'Slot 1'),
        (2, 'Slot 2'),
        (3, 'Slot 3'),
    )

class Document(models.Model):
    rut = models.CharField(max_length=18)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    dispenser_slot = models.IntegerField(choices=SLOT_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    
class Retrieve(models.Model):
    rut = models.CharField(max_length=10)
    password = models.CharField(max_length=6)