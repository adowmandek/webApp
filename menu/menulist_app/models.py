from django.db import models
from django.db.models.fields import GenericIPAddressField

# Create your models here.

class Menu(models.Model):
    name=models.CharField(max_length=10)
    quantity=models.CharField(max_length=12)

    def __str__(self):
            return self.menu_name

