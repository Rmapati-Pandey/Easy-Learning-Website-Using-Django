from django.urls import path
from  . import views
#. include all methods of views file
urlpatterns = [
    path('new/',views.employee),
    path('profile/',views.profile,name='profile'),
]
