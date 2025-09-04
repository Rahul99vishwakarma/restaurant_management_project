from django.shortcuts import render
from .models import menuitem

def menu_page(request):
    items = menuitem.object.all()
    return render(request,'menu.html',{'items':items})