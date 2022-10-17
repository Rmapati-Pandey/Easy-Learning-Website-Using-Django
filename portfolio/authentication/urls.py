from django.urls import path
from  . import views
#. include all methods of views file
urlpatterns = [
    #path('new/',views.employee),
    # path('',views.home,name='home'),
    # path('about/',views.aboutus, name='about'),
    path('',views.authlogin,name='login'),
    path('registration/',views.authregistration,name='registration'),
    path('forget-password/',views.forgetpassword,name='forgetpassword'),
    path('logout/',views.authlogout,name='logout')
]
