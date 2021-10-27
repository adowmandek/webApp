
from django import forms
from django.db.models.base import Model
from django.forms import fields
from.models import Menu

class Menuregistrationform(forms.ModelForm):
    class Meta:
        model=Menu
        fields="__all__"