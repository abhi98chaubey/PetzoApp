from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/base.html')

def careers(request):
    # return HttpResponse('careers Page')
    return render(request, 'accounts/careers.html')

def howItWork(request):
    # return HttpResponse('howItWork Page')
    return render(request, 'accounts/howItWork.html')

def partnerships(request):
    # return HttpResponse('partnerships Page')
    return render(request, 'accounts/partnerships.html')

def blog(request):
    # return HttpResponse('blog Page')
    return render(request, 'accounts/blog.html')

def login(request):
    # return HttpResponse('login Page')
    return render(request, 'accounts/login.html')


def downloadApp(request):
    # return HttpResponse('download-app Page')
    return render(request, 'accounts/downloadApp.html')
