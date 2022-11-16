from django.contrib import admin
from django.urls import path

url = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
]