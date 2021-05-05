from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail
from .forms import RegistrationForm
from .models import *


# Create your views here.

def home(request):

    cities = Cityy.objects.all()
    programs = Categories.objects.all()
   
    sent = False

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():


            return redirect('/')

    else:
        form = RegistrationForm()
    return render(request, 'conference/home.html',{'form':form,'cities':cities,'programs':programs})

    