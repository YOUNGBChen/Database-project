from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/',views.add),
    path('list/',views.list),
    path('show/',views.show)
]