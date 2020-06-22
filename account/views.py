from django.shortcuts import render


# Create your views here.
from account import models

def register1(request):
    # if request.method == "POST":
    new_username = request.POST.get('username')
    new_password = request.POST.get('password')
    return render(request,"login.html")