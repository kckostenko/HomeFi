"""django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    # view that gets run when go to 127.0.0.1:8000/admin
    path('admin/', admin.site.urls),

    # # whenever django encounters include(), it will get rid of what its already processed
    # # (i.e. the homepg part of the url...). It will then go into the homepg/urls.py file. But remember, its
    # # already discarded homepg so when it gets there, its an empty route/string! Hence why empty string in
    # # homepg/urls.py. The urls.py then says, if you give me an empty string, I'm going to call the home function
    # # from homepg/views.py, which then sends an HTTPResponse to my browser!!!
    # path('home/', include('homepg.urls')),

    # SET User Registration Page
    path('register/', user_views.register, name='register'),
    path('addRooms/', user_views.addRoom, name="add-rooms"),
    path('removeRooms/', user_views.removeRoom, name="remove-rooms"),
    path('addLights/', user_views.lightsForm, name="add-lights"),
    path('removeLights/', user_views.deleteLightsForm, name="remove-lights"),
    path('changeLights/', user_views.changeLights, name="change-lights"),
    path('addLocks/', user_views.locksForm, name="add-locks"),
    path('removeLocks/', user_views.deleteLocksForm, name="remove-locks"),
    path('addAlarm/', user_views.alarmForm, name="add-alarm"),
    path('checkAlarmPin/', user_views.correctAlarmPin, name="check-alarm-pin"),
    path('changeAlarm/',user_views.changeAlarm, name="change-alarm"),
    # Log In View
    path('login/', auth_views.LoginView.as_view(template_name='homepg/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepg/logout.html'), name='logout'),
    # SET HOMEPAGE WITH EMPTY STRING
    path("", include("homepg.urls")),


]
