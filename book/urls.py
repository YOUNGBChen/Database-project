from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/',views.add),
    path('list/',views.list),
    path('show/',views.show),
    path('borrow/',views.borrow),
    path('return/',views.returnbook),
    path('check/',views.checkbook),
    path('success/',views.success),
    path('borrowed/', views.checkbook),
]