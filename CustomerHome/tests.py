from CustomerHome.views import register, signin, Logout, RegisterCustomer, LoginAuthentication, Home, Profile
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from django.test.client import Client
from .views import *


class TestUrls(SimpleTestCase):
    def test_register_url(self):
        url = reverse("Register")
        self.assertEquals(resolve(url).func, register)

    def test_register_url(self):
        url = reverse("SignIn")
        self.assertEquals(resolve(url).func, signin)

    def test_register_url(self):
        url = reverse("Logout")
        self.assertEquals(resolve(url).func, Logout)

    def test_register_url(self):
        url = reverse("RegisterCustomer")
        self.assertEquals(resolve(url).func, RegisterCustomer)

    def test_register_url(self):
        url = reverse("LoginAuthentication"),
        self.assertEquals(resolve(url).func, LoginAuthentication)

    def test_register_url(self):
        url = reverse("Home"),
        self.assertEquals(resolve(url).func, )

    def test_register_url(self):
        url = reverse("Profile"),
        self.assertEquals(resolve(url).func, Profile)
    
    def test_register_url(self):
        url = reverse("Owner.urls"),
        self.assertEquals(resolve(url).func, Owner)

    def test_register_url(self):
        url = reverse("Manager.urls"),
        self.assertEquals(resolve(url).func, Manager)