from django.http import HttpResponse
from . models import Category,Product
from django.shortcuts import render
from django.contrib import auth, messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Category,Product

# Create your views here.
def index(request):
    items=Product.objects.all()
    return render(request,'index.html',{'items':items})



def register(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
                return redirect('medishop:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('medishop:login')
        else:
            messages.info(request,'password already exist')
            return redirect('medishop:register')
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid user')
            return redirect('medishop:login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def detail(request, product_id):
    if request.user.is_authenticated:
        item = Product.objects.get(id=product_id)
    else:
        return redirect('medishop:login')
    return render(request, 'detail.html', {'item': item})

def alloitems(request):
    items=Product.objects.filter(category=1)
    return render(request,'index.html',{'items':items})
def homeitems(request):
    items=Product.objects.filter(category=2)
    return render(request,'index.html',{'items':items})
def ayuritems(request):
    items=Product.objects.filter(category=3)
    return render(request,'index.html',{'items':items})

def thank(request):
    return render(request,'thank.html')