from django.url import path
from .views import menu_list

urlpatterns = [
    path("menu/", menu_list, name="menu")
]