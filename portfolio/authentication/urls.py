from django.urls import path
from  . import views
#. include all methods of views file
urlpatterns = [
    #path('new/',views.employee),
    # path('',views.home,name='home'),
    # path('about/',views.aboutus, name='about'),
    path('',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('forget-password',views.forgetpassword,name='forgetpassword'),

]
