from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def employee(request):
    return HttpResponse("This is the employee page")

def profile(request):
    return render(request,'employee/profile.html')
    #return HttpResponse('This is employee profile')
