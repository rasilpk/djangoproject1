from django.shortcuts import render,redirect

from .models import book
from .forms import bookform

# from django.http import HttpResponse

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
        'name': 'razil',
        'age': 21,
        'course': 'B.com finance',
    }
    return render(request, 'about.html', data)
def contact(request):
    return render(request,"contact.html")

def viewbook(request):
    a=book.objects.all()
    return render(request,'viewbook.html',{"ab":a})

def addbook(request):
    a=bookform(request.POST or None)
    if a.is_valid():
        a.save()
        return redirect("viewbook")
    return render(request,'addbook.html',{"ab":a})

def update_book(request,id):
    a=book.objects.get(id=id)
    b=bookform(request.POST or None ,instance=a)
    if b.is_valid():
        b.save()
        return redirect('viewbook')
    return render(request,"updatebook.html",{"ab":b})

def delete_book(request,id):
    a=book.objects.get(id=id)
    if request.method=='POST':
      a.delete()
      return redirect('viewbook')
    return render(request,"deletebook.html",{"ab":book})