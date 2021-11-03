
from django import forms
from.models import Menu

class Menuregistrationform(forms.ModelForm):
    class Meta:
        model=Menu
        fields="__all__"