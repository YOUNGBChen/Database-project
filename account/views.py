from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse

# Create your views here.
from account import models

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')
        new_idcard = request.POST.get('idcard')
        if User.objects.filter(username=new_username):
            return render(request,'Done1.html')
        else:
            models.User.objects.create(
                username=new_username,
                password=new_password,
                idcard=new_idcard,
            )
            user_lis = models.User.objects.all()
            return redirect('http://127.0.0.1:8000/user/login')
    return render(request,"register.html")

def detail(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            user = User.objects.filter(username = username,password = password)
            if user:
                return redirect('http://127.0.0.1:8000/book')
            else:
                return HttpResponse("密码错误，请尝试重新登陆")
        else:
            return HttpResponse("用户名不存在，请返回注册")
    return render(request,"login.html")

def not_exist(request):
    return render(request,'notexist2.html')