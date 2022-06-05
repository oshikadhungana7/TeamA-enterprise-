from django import forms
from .models import Customer
from django.contrib.auth.models import User




class Customer_data(forms.ModelForm):
    class Meta():
        model = Customer
        fields = "__all__"
