from django.shortcuts import render
from .models import Post, Light, Room, Lock, Alarm
from django.contrib.auth.decorators import login_required


# from time import asctime, struct_time
# from django.http import HttpResponse

# Create your views here.
# posts in a list of dictionaries, containing info about each "post"

# DUMMY DATA
# posts = [
#     {
#         'user': "TESTING",
#         'date_logged': "3 Apr 2020"
#     },
#     {
#         'user': "TESTING2",
#         'date_logged': "4 Apr 2020"
#     }
# ]


# Creating logic/functions for how we want to handle certain routes...
# map URLs to these functions to LOCAL "urls.py" file (different that project wide urls.py file)
def home(request):
    # run Query on Post Model and run Query on Post
    # NOTE: MUST import POST in the beginning...
    # need to load in templates here! Use render()
    # render still returns an HTTP Response!
    return render(request, "homepg/home.html")

def status(request):

    dbEntries = {
        'rooms': Room.objects.filter(owner=request.user),
        'lights': Light.objects.filter(owner=request.user),
        'locks': Lock.objects.filter(owner=request.user),
        'alarms': Alarm.objects.filter(owner=request.user),
    }

    return render(request, "homepg/statusPage.html", dbEntries)


def about(request):
    # return HttpResponse("<h1> About Us: We Cool </h1>")
    return render(request, "homepg/about.html")


def login(request):
    return render(request, "homepg/login.html")


def shop(request):
    return render(request, "homepg/shop.html")


@login_required
def smarthome(request):
    return render(request, "homepg/smarthome.html")


def forgotpswd(request):
    return render(request, "homepg/ForgotPswd.html")
