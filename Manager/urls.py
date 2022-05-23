from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from CustomerHome import views as cust_views
from vehicle import views as veh_views

urlpatterns = [
    path('', views.index, name="Manager"),
    path('signin/',cust_views.signin, name="SignIn"),
    path('Logout/',cust_views.Logout, name="Logout"),
    path('Profile/',views.Profile, name="Profile"),
    path('AllCustomers/',views.AllCustomers, name="AllCustomers"),
    path('AllVehicles/',views.AllVehicles, name="AllVehicles"),
    
    path('ManagerCustomerProfile/<str:customer_email>/',views.Customer_Profile,name="ManagerCustomerProfile"),
    path('UploadVehicle/',views.upload_Vehicle, name="UploadVehicle"),
    path('Vehicle/UploadVehicle',veh_views.upload_vehicle,name="UploadVehicle"),
]