from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from web1.models import Users

# Create your views here.
def home(request):
    return render(request,'web1/home.html')
def base(request):
    return render(request,'web1/base.html')
def login(request):
    return render(request,'web1/login.html')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        new_user = Users(
            username=username,
            password=password,
            name=name
        )
        new_user.save()
        return redirect('web1/login.html')
           
    return render(request,'web1/signup.html')



