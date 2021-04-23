from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, addLights
# many possible types of django messages. Error, Success, Warning, Info, Debug...

from homepg import models as lightModel


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
            lightsObj = lightModel.Light()

            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            lightsObj.lightName = form.cleaned_data['lightName']
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