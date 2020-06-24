from django.shortcuts import render
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
        nwe_id = request.POST.get('id')
        #new_user=models.User(username = new_username,password = new_password,id=nwe_id)
        #new_user.save()
        models.User.objects.create(
            username=new_username,
            password=new_password,
            id=nwe_id,
        )
        user_lis = models.User.objects.all()
        return
    return render(request,"register.html")

def detail(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username):
            user = User.objects.filter(username = username,password = password)
            if user:
                return HttpResponse('登陆成功')
            else:
                return HttpResponse("密码错误，请尝试重新登陆")
        else:
            return HttpResponse("用户名不存在，请返回注册")
    return render(request,"login.html")