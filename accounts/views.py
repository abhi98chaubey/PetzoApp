from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/index.html')

def careers(request):
    # return HttpResponse('careers Page')
    return render(request, 'accounts/careers.html')

def howItWork(request):
    return render(request, 'accounts/howItWork.html')

def partnerships(request):
    return render(request, 'accounts/partnerships.html')

def blog(request):
    return render(request, 'accounts/blog.html')

def login(request):
    return render(request, 'accounts/login.html')

def downloadApp(request):
    return render(request, 'accounts/downloadApp.html')

def pricing(request):
    return render(request, 'accounts/pricing.html')

def checkOutForm(request):
    return render(request, 'accounts/checkOutForm.html')