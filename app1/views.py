from django.shortcuts import render

from .models import book

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("hello,django")
# def about(request):
#     return HttpResponse("hello")
# Create your views here.

def home(request):
    data=["python","css","js","react","django"]
    return render(request,"home.html",{"a":data})
def about(request):
    data = {
        'name': 'Nikhil',
        'age': 21,
        'course': 'B.Sc Computer Science',
    }
    return render(request, 'about.html', data)
def contact(request):
    return render(request,"contact.html")

def viewbook(request):
    a=book.objects.all()
    return render(request,'viewbook.html',{"ab":a})