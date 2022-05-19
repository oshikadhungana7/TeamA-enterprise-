from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

import CustomerHome

urlpatterns = [
     
  
    
   
   
  
    path('signin/',views.signin,name="SignIn"),

    
    path('Logout/',views.Logout,name="Logout"),    
    path('register/',views.register,name="Register"),
    
    
    
    path('LoginAuthentication/',views.LoginAuthentication,name="LoginAuthentication"),
    path('RegisterCustomer/',views.RegisterCustomer,name="RegisterCustomer"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)