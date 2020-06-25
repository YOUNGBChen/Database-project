from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import book
from django.http import HttpResponse
from book import models

# Create your views here.

def index(request):
    return render(request,"menu.html")

def add(request):
    if request.method == "POST":
        new_ISBN = request.POST.get('isbn')
        new_name = request.POST.get('name')
        new_writer = request.POST.get('writer')
        new_publish = request.POST.get('publish')
        new_sort = request.POST.get('sort')
        new_year = request.POST.get('year')
        models.book.objects.create(
            ISBN = new_ISBN ,
            name = new_name ,
            writer = new_writer,
            publish = new_publish,
            sort = new_sort,
            year = new_year,
        )
        book_lis = models.book.objects.all()
        return redirect('http://127.0.0.1:8000/book')
    return render(request,"Book.html")