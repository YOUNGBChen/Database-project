from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from book.models import bbook
from django.http import HttpResponse
from book import models as md
from account import models
from account.models import User


# Create your views here.

def index(request):
    return render(request,"menu.html")

def list(request):
    return render(request,"List.html")

def success(request):
    return render(request,"success2.html")

def add(request):
    if request.method == "POST":
        new_ISBN = request.POST.get('isbn')
        new_name = request.POST.get('name')
        new_writer = request.POST.get('writer')
        new_publish = request.POST.get('publish')
        new_sort = request.POST.get('sort')
        new_year = request.POST.get('year')
        md.bbook.objects.create(
            ISBN = new_ISBN,
            name = new_name,
            writer = new_writer,
            publish = new_publish,
            sort = new_sort,
            year = new_year,
        )
        book_lis = md.bbook.objects.all()
        return redirect('http://127.0.0.1:8000/book')
    return render(request,"Book.html")

def show(request):
    books = bbook.objects.all()
    return render(request,"List.html",{'books':books})

def borrow(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        users = User.objects.filter(username = username)
        userss = User.objects.get(username=username)
        sum = userss.borrowed
        id = userss.idcard
        if users:
            bbook.objects.filter(name = name).update(username = username)
            if (id == '0') :
                if sum<5 :
                    sum = sum + 1
                    User.objects.filter(username = username).update(borrowed = sum)
                    return redirect('http://127.0.0.1:8000/book/success')
                else:
                    return HttpResponse('借的太多了')

            else  :
                if sum<2 :
                    sum = sum + 1
                    User.objects.filter(username = username).update(borrowed = sum)
                    return redirect('http://127.0.0.1:8000/book/success')
                else:
                    return HttpResponse('借的太多了')

        else:
            return redirect('http://127.0.0.1:8000/user/not_exist/')

    return render(request,'Borrow.html')

def returnbook(request):
    if request.method == "POST":
        username = request.POST.get('username')
        name = request.POST.get('name')
        users = User.objects.filter(username=username)
        userss = User.objects.get(username=username)
        sum = userss.borrowed
        id = userss.idcard
        if users:
            book.objects.filter(name = name).update(username = 0 )
            sum = sum - 1
            User.objects.filter(username=username).update(borrowed=sum)
            return redirect('http://127.0.0.1:8000/book/success')
        else:
            return redirect('http://127.0.0.1:8000/user/not_exist/')
    return render(request, 'Return.html')

def checkbook(request):
    if request.method == "POST":
        username = request.POST.get('username')
        books = book.objects.filter(username = username)
        return render(request, "List2.html", {'books': books})
    return render(request,'Check_login.html')

def money():
    return HttpResponse('15yuan')