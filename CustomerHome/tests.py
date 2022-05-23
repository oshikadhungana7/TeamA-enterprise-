from CustomerHome.views import register, signin, Logout

from django.urls import reverse,resolve

from django.test import SimpleTestCase

from django.test.client import Client

from .views import *



class TestUrls(SimpleTestCase):

    def test_register_url(self):

        url=reverse("Register")

        self.assertEquals(resolve(url).func,register)

    def test_signin_url(self):

        url=reverse("SignIn")

        self.assertEquals(resolve(url).func,signin)

    def test_Logout_url(self):

        url=reverse("Logout")

        self.assertEquals(resolve(url).func,Logout)
    def test_LoginAuthentication_url(self):

        url=reverse("LoginAuthentication")

        self.assertEquals(resolve(url).func,LoginAuthentication)