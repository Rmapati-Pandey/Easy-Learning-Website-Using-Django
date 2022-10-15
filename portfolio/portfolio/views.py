from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    # text={
    # 'name' : "Rmapati Pandey",
    # 'age' : 23,
    # 'phone' : 9267975616,
    # 'friend_name': ['rmapati','nikhil', 'apoorva', 'ayush']
    # }
    return render(request,'index.html',) #we have to allocate it to the django to imform him that
    #return HttpResponse("This is our home page")

def about(request):
    #data="get all data from database" #all the queries we can write here
    #return HttpResponse(data)
    return render(request,'about.html')
    #return HttpResponse("This is about Home Page")

def contact(request):
    return render(request,'contact.html')
