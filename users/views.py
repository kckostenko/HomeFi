from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, addLights, addAlarm, addLocks
# many possible types of django messages. Error, Success, Warning, Info, Debug...

from homepg import models as Model


def register(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for' + username +  '! You can now log in!')
            return redirect("login")
    else:
        # if not POST request, will create a blank form!
        form = UserRegisterForm()

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/registers.html', {'form': form})

def lightsForm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = addLights(request.POST)
        if form.is_valid():
            #form.save()
            lightsObj = Model.Light()

            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            lightsObj.lightName = form.cleaned_data['lightName']
            lightsObj.roomLoc = form.cleaned_data['roomLoc']
            lightsObj.lightType = form.cleaned_data['lightType']
            lightsObj.color = form.cleaned_data['color']
            lightsObj.dimness = form.cleaned_data['dimness']
            lightsObj.state = form.cleaned_data['state']
            lightsObj.owner = request.user
            lightsObj.save()
            messages.success(request, 'Light ' + lightsObj.lightName + ' created!')
            return redirect("smart-home")
    else:
        # if not POST request, will create a blank form!
        form = addLights()

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/lightsForm.html', {'form': form})

def locksForm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = addLocks(request.POST)
        if form.is_valid():
            locksObj = Model.Lock()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            locksObj.lockName = form.cleaned_data['lockName']
            locksObj.state = form.cleaned_data['state']
            locksObj.roomLoc = form.cleaned_data['roomLoc']
            ##lightsObj.roomLoc = form.cleaned_data['roomLoc']
            locksObj.code1 = form.cleaned_data['code1']
            locksObj.code2 = form.cleaned_data['code2']
            locksObj.code3 = form.cleaned_data['code3']
            locksObj.code4 = form.cleaned_data['code4']
            locksObj.owner = request.user
            locksObj.save()
            messages.success(request, 'Lock ' + locksObj.lockName + ' created!')
            return redirect("smart-home")
    else:
        # if not POST request, will create a blank form!
        form = addLocks()

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/locksForm.html', {'form': form})

def alarmForm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = addAlarm(request.POST)
        if form.is_valid():
            alarmObj = Model.Alarm()

            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            alarmObj.alarmName = form.cleaned_data['alarmName']
            alarmObj.state = form.cleaned_data['state']
            alarmObj.code1 = form.cleaned_data['code1']
            alarmObj.code2 = form.cleaned_data['code2']
            alarmObj.code3 = form.cleaned_data['code3']
            alarmObj.code4 = form.cleaned_data['code4']
            alarmObj.owner = request.user
            alarmObj.save()
            messages.success(request, 'Alarm ' + alarmObj.alarmName + ' created!')
            return redirect("smart-home")
    else:
        # if not POST request, will create a blank form!
        form = addAlarm()

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/alarmForm.html', {'form': form})
