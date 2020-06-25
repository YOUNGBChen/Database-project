from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"menu.html")

def add(request):
    if request.method == "POST":
        ISBN = request.POST.get('ISDN')
        name = request.POST.get('name')
        writer = request.POST.get('writer')
        publish = request.POST.get('publish')
        sort = request.POST.get('sort')
        year = request.POST.get('yearv')