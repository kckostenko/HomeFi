from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # home view... note view.home is the FUNCTION from views.py
    # empty path maps to home view...
    path("", views.home, name="business-home"),
    # 127.0.0.1:8000/home/about/
    # remember, the include() in django_tutorial/url.py CHOPS OFF what it has already processed. So when it gets here
    # it has already chopped off "127.0.0.1/home" leaving ONLY "about/"...
    # It's all about that nesting BAYYY-BEEEE **finger guns**
    path("about/", views.about, name="business-about"),
    path("login/", views.login, name="user-login"),
    path("shop/", views.shop, name="business-shop"),
    path("smarthome/", views.smarthome, name="smart-home"),
    path("forgotpswd/", views.forgotpswd, name="forgot-pswd"),
]
