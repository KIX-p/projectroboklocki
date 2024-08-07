from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import JsonResponse


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def form1(request):
    return render(request, 'main/form1.html')

def form2(request):
    return render(request, 'main/form2.html')

