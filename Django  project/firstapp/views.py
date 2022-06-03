from ast import Num
from datetime import datetime
import email
from tokenize import Number
from unicodedata import name
from django.forms import Textarea
from django.shortcuts import render, HttpResponse
from firstapp.models import Contact

from django.contrib import messages

# Create your views here.
def index (request):
    return render(request, "index.html" )
    # return HttpResponse("This is home page")

def about (request):
    return render(request, "about.html" )

def portfolio (request):
    return render(request, "portfolio.html" )

def contacttest (request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        Number= request.POST.get('number')
        Textarea= request.POST.get('Textarea')
        Contact.objects.create(name=name, email=email,Number=Number,Textarea=Textarea,
        date=datetime.today())
        messages.success(request,'Your message has been sent!!!')
    return render(request, "contact.html" )

# def usama (request):
#     return render(request, "contact.html" )

