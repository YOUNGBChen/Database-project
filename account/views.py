from django.shortcuts import render

# Create your views here.
from account import models

def register(request):
    # if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    ID = request.POST.get('ID')
    return render(request,"register.html")

def detail(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return render(request,"login.html")