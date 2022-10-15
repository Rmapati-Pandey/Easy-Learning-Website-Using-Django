from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'authentication/login.html')

def registration(request):
    return render(request,'authentication/register.html')

def forgetpassword(request):
    return render(request,'authentication/forget.html')
