from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.list,name="list"),

    path('list/', views.list,name="list"),
    path('add/', views.add, name="add"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('change/<int:id>', views.change, name="change"),


]
