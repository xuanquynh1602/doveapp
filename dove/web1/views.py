from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'web1/home.html')
def base(request):
    return render(request,'web1/base.html')
def login(request):
    return render(request,'web1/login.html')
from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponse
def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request,'pages/contact.html')
def error(request):
    return render(request,'pages/error.html')
def register(request):
    form = RegistrationForm()



