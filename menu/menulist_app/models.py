from django.db import models
from django.db.models.fields import GenericIPAddressField

# Create your models here.

class Menu(models.Model):
    menu_name=models.CharField(max_length=10)
    menu_price=models.CharField(max_length=10)
    menu_quantity=models.CharField(max_length=12)

    def __str__(self):
            return self.menu_name

