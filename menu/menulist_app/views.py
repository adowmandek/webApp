# from Menu.models import Menu
from menulist_app.models import Menu
from django.shortcuts import render
from django.forms import Form
from django.urls.conf import re_path
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.db.models.aggregates import StdDev
from .forms import Menuregistrationform




def menu_list(request):
     menu= Menu.objects.all()
     return render(request,"menu_list.html",{"menus":menu})


def  edit_menu(request,id):
     menu=Menu.objects.get(id=id)

     # return redirect(request,"edit_menu.html",)

     if request.method=="POST":
          form=Menuregistrationform(request.POST,instance=menu)
          if form.is_valid():
               form.save()
     else:
          form=Menuregistrationform(instance=menu)
          return render(request,"edit_menu.html",{"form":form})
     return redirect(request,"menu_register.html",)


def delete_menu(request,id):
          menu=Menu.objects.get(id=id)
          menu.delete()
          return redirect("menu_list")
def menu_register(request):
     if request.method=="POST":
          form=Menuregistrationform(request.POST)
          if form.is_valid():
               form.saved()
     # else:
     #     print("form.error")

     form=Menuregistrationform()
     return render(request,"menu_register.html",{"form":form})
