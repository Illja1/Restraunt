from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lands, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string







def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Register complete')
            return redirect('login')
        else:
            messages.error(request, 'Register not complete')
    else:
        form = UserRegisterForm()
    return render(request, 'land/register.html',{"form":form,'title':'Restraunt'})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
            form = UserLoginForm()
    return render(request, 'land/login.html',{"form":form,'title':'Restraunt'})

def start_page(request):
    start_page = Lands.objects.all()
    categories = Category.objects.all()
    context = {

    'title':'Restraunt',
    'categories':categories,
    }
    return render(request,'land/head.html',context=context)




def get_category(request,category_id):
    menu = Lands.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
    'menu':menu,
    'categories': categories,
    'category':category,
    'title':'Restraunt',
    }

    return render(request,'land/category.html',context=context)



def Menu(request):
    menu = Lands.objects.all()
    categories = Category.objects.all()
    context = {
    'menu':menu,
    'title':'Food menu',
    'categories':categories,
    }
    return render(request,'land/menu.html',context=context)
