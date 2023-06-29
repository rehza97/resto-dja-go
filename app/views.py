from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    nm = Menu.objects.all()
    
    context ={
        'menu' : nm 
    }
    return render(request , 'base/index.html',context)

def about(request):
    return render(request , 'base/about.html')

def booking(request):
    return render(request , 'base/booking.html')

def contact(request):
    return render(request , 'base/contact.html')

def menu(request):
    nm = Menu.objects.all()
    
    context ={
        'menu' : nm 
    }
    return render(request , 'base/menu.html',context)

def service(request):
    return render(request , 'base/service.html')

def team(request):
    return render(request , 'base/team.html')

def testimonial(request):
    return render(request , 'base/testimonial.html')