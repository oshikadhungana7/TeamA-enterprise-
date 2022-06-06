from django import forms
from .models import Customer


class Customer_data(forms.ModelForm):
    class Meta():
        model = Customer
        fields = "__all__"