from django.shortcuts import render
from .models import about
from .models import client
# Create your views here.


def home(request):
    aboutdata=about.objects.all()[0]
    clientdata=client.objects.all()
    context={
       'about':aboutdata,
       'client':clientdata
    }
    # text={
    # 'name' : "Rmapati Pandey",
    # 'age' : 23,
    # 'phone' : 9267975616,
    # 'friend_name': ['rmapati','nikhil', 'apoorva', 'ayush']
    # }
    return render(request,'index.html', context) #we have to allocate it to the django to imform him that
    #return HttpResponbe("This is our home page")

def aboutus(request):
    #data="get all data from database" #all the queries we can write here
    #return HttpResponse(data)
    return render(request,'about.html')
    #return HttpResponse("This is about Home Page")
