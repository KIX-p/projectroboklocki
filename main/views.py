from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def form1(request):
    return render(request, 'main/form1.html')

def form2(request):
    return render(request, 'main/form2.html')