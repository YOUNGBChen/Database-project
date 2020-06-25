from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register),
    path('login/',views.detail),
    path('not_exist/',views.not_exist),
    path('',views.index),
]