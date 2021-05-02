from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, addLights, addAlarm, addLocks, removeLocks, removeLights, alarmPin, \
    changeAlarmForm, addRoomForm, deleteRoomForm, changeLightForm, changeLockForm, lockPin
from django.forms.models import model_to_dict
from homepg.models import Post, Light, Room, Lock, Alarm

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
            messages.success(request, 'Account created for' + username + '! You can now log in!')
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
        form = addLights(request.POST, user=request.user)
        if form.is_valid():
            # form.save()
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
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = addLights(user=request.user)

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/lightsForm.html', {'form': form})


def deleteLightsForm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = removeLights(request.POST, user=request.user)
        if form.is_valid():
            lightsObj = Model.Light()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            lightsObj.lightName = form.cleaned_data['lightName']
            lightsObj.owner = request.user
            # Pull all codes for that lock name from the Data Model...
            # if user's entry matches one of the four codes
            entry = Model.Light.objects.get(id=lightsObj.lightName.id)
            entry.delete()
            messages.success(request, 'Light ' + str(lightsObj.lightName) + ' deleted!')
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = removeLights(user=request.user)
    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/removeLights.html', {'form': form})


def locksForm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = addLocks(request.POST, user=request.user)
        # form.roomLoc.queryset = Model.Room.filter(user=user_id.id)
        if form.is_valid():
            locksObj = Model.Lock()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            locksObj.lockName = form.cleaned_data['lockName']
            locksObj.state = form.cleaned_data['state']
            locksObj.roomLoc = form.cleaned_data['roomLoc']
            locksObj.code1 = form.cleaned_data['code1']
            locksObj.code2 = form.cleaned_data['code2']
            locksObj.code3 = form.cleaned_data['code3']
            locksObj.code4 = form.cleaned_data['code4']
            locksObj.owner = request.user
            locksObj.save()
            messages.success(request, 'Lock ' + locksObj.lockName + ' created!')
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = addLocks(user=request.user)

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/locksForm.html', {'form': form})


def deleteLocksForm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = removeLocks(request.POST, user=request.user)
        if form.is_valid():
            lockObj = Model.Lock()

            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            lockObj.lockName = form.cleaned_data['lockName']
            lockObj.owner = request.user
            lockObj.entryPin = form.cleaned_data['entryPin']
            # Pull all codes for that lock name from the Data Model...
            allCodes = Model.Lock.objects.filter(lockName=lockObj.lockName)
            # Need to extract each code using its field name (Ex: code1, code2, etc. etc.)
            # Saves as a QuerySet list with one element. The [0] extracts that one element
            code1 = allCodes.values_list('code1', flat=True)[0]
            code2 = allCodes.values_list('code2', flat=True)[0]
            code3 = allCodes.values_list('code3', flat=True)[0]
            code4 = allCodes.values_list('code4', flat=True)[0]
            codeList = [code1, code2, code3, code4]
            # if user's entry matches one of the four codes
            if lockObj.entryPin in codeList:
                entry = Model.Lock.objects.get(id=lockObj.lockName.id)
                entry.delete()
                messages.success(request, 'Lock ' + str(lockObj.lockName) + ' deleted!')
                return redirect("status-page")
            else:
                messages.error(request, 'Lock ' + str(lockObj.lockName) + ' PIN incorrect!')
    else:
        # if not POST request, will create a blank form!
        form = removeLocks(user=request.user)
    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/removeLocks.html', {'form': form})


def correctLockPin(request):
    if request.method == "POST":
        form = lockPin(request.POST, user=request.user)
        if form.is_valid():
            locksObj = Model.Lock()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            locksObj.lockName = form.cleaned_data['lockName']
            locksObj.entryPin = form.cleaned_data['entryPin']
            locksObj.owner = request.user
            # Pull all codes for that lock name from the Data Model...
            allCodes = Model.Lock.objects.filter(lockName=locksObj.lockName)
            # Need to extract each code using its field name (Ex: code1, code2, etc. etc.)
            # Saves as a QuerySet list with one element. The [0] extracts that one element
            code1 = allCodes.values_list('code1', flat=True)[0]
            code2 = allCodes.values_list('code2', flat=True)[0]
            code3 = allCodes.values_list('code3', flat=True)[0]
            code4 = allCodes.values_list('code4', flat=True)[0]
            # alarmObj.save()
            codeList = [code1, code2, code3, code4]
            # if user's entry matches one of the four codes
            if locksObj.entryPin in codeList:
                messages.success(request, 'PIN code for ' + str(locksObj.lockName) + ' correct!')
                return redirect("change-lock")
            else:
                messages.info(request, 'Pin code for ' + str(locksObj.lockName) + ' incorrect!')
    else:
        # if not POST request, will create a blank form!
        form = lockPin(user=request.user)

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/lockPinCheck.html', {'form': form})


def changeLock(request):
    if request.method == "POST":
        # if get post request will create form that has request.POST data!
        form = changeLockForm(request.POST, user=request.user)
        if form.is_valid():
            locksObj = Model.Lock()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            tempBool = form.cleaned_data['newNameBool']
            if tempBool:
                locksObj.lockName = form.cleaned_data['newLockName']
            elif not tempBool:
                locksObj.lockName = form.cleaned_data['lockName']
            else:
                print("WHOOPSIE! clearly I coded something wrong wtf")

            locksObj.state = form.cleaned_data['state']
            locksObj.roomLoc = form.cleaned_data['roomLoc']
            locksObj.code1 = form.cleaned_data['code1']
            locksObj.code2 = form.cleaned_data['code2']
            locksObj.code3 = form.cleaned_data['code3']
            locksObj.code4 = form.cleaned_data['code4']
            locksObj.owner = request.user
            # get the old alarm name
            allCodes = Model.Lock.objects.filter(owner_id=request.user)
            # old Alarm Name
            currentName = allCodes.values_list('lockName', flat=True)[0]
            # if the old alarm name and new alarm name aren't equal...
            # delete the old alarm entry
            entry = Model.Lock.objects.get(lockName=str(currentName))
            entry.delete()
            # replace it with the new data
            locksObj.save()
            messages.success(request, 'Lock ' + str(locksObj.lockName) + ' edited!')
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = changeLockForm(user=request.user)
    return render(request, 'users/changeLockForm.html', {'form': form,
                                                         'rooms': Room.objects.filter(owner=request.user),
                                                         'locks': Lock.objects.filter(owner=request.user)})


def alarmForm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top
        allAlarms = Model.Alarm.objects.filter(owner_id=request.user.id)
        # if get post request will create form that has request.POST data!
        form = addAlarm(request.POST)
        if form.is_valid() and not allAlarms:
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
            return redirect("status-page")
        else:
            messages.info(request, "You already have one alarm for this home! \n You cannot have multiple!")
    else:
        # if not POST request, will create a blank form!
        form = addAlarm()
        return render(request, 'users/alarmForm.html', {'form': form})


def correctAlarmPin(request):
    if request.method == "POST":
        form = alarmPin(request.POST, user=request.user)
        if form.is_valid():
            alarmObj = Model.Alarm()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            alarmObj.alarmName = form.cleaned_data['alarmName']
            alarmObj.entryPin = form.cleaned_data['entryPin']
            alarmObj.owner = request.user
            # Pull all codes for that lock name from the Data Model...
            allCodes = Model.Alarm.objects.filter(alarmName=alarmObj.alarmName)
            # Need to extract each code using its field name (Ex: code1, code2, etc. etc.)
            # Saves as a QuerySet list with one element. The [0] extracts that one element
            code1 = allCodes.values_list('code1', flat=True)[0]
            code2 = allCodes.values_list('code2', flat=True)[0]
            code3 = allCodes.values_list('code3', flat=True)[0]
            code4 = allCodes.values_list('code4', flat=True)[0]
            # alarmObj.save()
            codeList = [code1, code2, code3, code4]
            # if user's entry matches one of the four codes
            if alarmObj.entryPin in codeList:
                messages.success(request, 'PIN code for ' + str(alarmObj.alarmName) + ' correct!')
                return redirect("change-alarm")
            else:
                messages.info(request, 'Pin code for ' + str(alarmObj.alarmName) + ' PIN incorrect!')
    else:
        # if not POST request, will create a blank form!
        form = alarmPin(user=request.user)

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/alarmPinCheck.html', {'form': form})


def changeAlarm(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top
        # allAlarm = Model.Alarm.objects.get(owner_id=request.user.id)
        # alarmName = allAlarm.values_list('alarmName', flat=True)[0]
        # state1 = allAlarm.values_list('state', flat=True)[0]
        # code1 = allAlarm.values_list('code1', flat=True)[0]
        # code2 = allAlarm.values_list('code2', flat=True)[0]
        # code3 = allAlarm.values_list('code3', flat=True)[0]
        # code4 = allAlarm.values_list('code4', flat=True)[0]
        # data = {'alarmName': str(alarmName), "state": str(state1), "code1": str(code1),
        #         "code2": str(code2), "code3": str(code3), "code4": str(code4)}
        # if get post request will create form that has request.POST data!
        form = changeAlarmForm(request.POST)
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
            # get the old alarm name
            allCodes = Model.Alarm.objects.filter(owner_id=request.user)
            # old Alarm Name
            currentName = allCodes.values_list('alarmName', flat=True)[0]
            # if the old alarm name and new alarm name aren't equal...
            # delete the old alarm entry
            entry = Model.Alarm.objects.get(alarmName=str(currentName))
            entry.delete()
            # replace it with the new data
            alarmObj.save()
            messages.success(request, 'Alarm ' + alarmObj.alarmName + ' edited!')
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = changeAlarmForm()
    return render(request, 'users/changeAlarmForm.html',
                  {'form': form, 'rooms': Room.objects.filter(owner=request.user),
                   'alarms': Alarm.objects.filter(owner=request.user)})


def addRoom(request):
    if request.method == "POST":
        form = addRoomForm(request.POST)
        if form.is_valid():
            roomObj = Model.Room()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            roomObj.roomName = form.cleaned_data['roomName']
            roomObj.owner = request.user
            messages.success(request, 'Room ' + roomObj.roomName + ' created!')
            roomObj.save()
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = addRoomForm()
    return render(request, 'users/addRoom.html', {'form': form})


def removeRoom(request):
    if request.method == "POST":
        form = deleteRoomForm(request.POST, user=request.user)
        if form.is_valid():
            roomObj = Model.Room()
            # will tell us if form valid when submitted
            # form.cleaned_data is a DICTIONARY
            roomObj.roomName = form.cleaned_data['roomName']
            roomObj.owner = request.user
            messages.success(request, 'Room ' + str(roomObj.roomName) + ' deleted!')
            entry = Model.Room.objects.get(roomName=roomObj.roomName)
            entry.delete()
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = deleteRoomForm(user=request.user)
    return render(request, 'users/deleteRoom.html', {'form': form})


def changeLights(request):
    if request.method == "POST":
        # use user creation form that can be used in HTML (Django Provides It!)
        # NOTE: must import UserCreationForm at top

        # if get post request will create form that has request.POST data!
        form = changeLightForm(request.POST, user=request.user)
        if form.is_valid():
            # form.save()
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
            # # Okay so instead of overwriting light values I decided to just delete them
            # # and re-save
            # allCodes = Model.Light.objects.filter(owner_id=request.user)
            # # old Alarm Name
            # currentName = allCodes.values_list('lightName', flat=True)[0]
            # delete the old alarm entry
            entry = Model.Light.objects.get(lightName=str(lightsObj.lightName))
            entry.delete()
            # replace it with the new data
            lightsObj.save()
            messages.success(request, 'Light ' + str(lightsObj.lightName) + ' edited!')
            return redirect("status-page")
    else:
        # if not POST request, will create a blank form!
        form = changeLightForm(user=request.user)

    # users/registers.html is TEMPLATE
    # Dictionary {'form': form} has key of variable form, and value is new instance of UserCreationForm
    return render(request, 'users/changeLights.html', {'form': form,
                                                       'rooms': Room.objects.filter(owner=request.user),
                                                       'lights': Light.objects.filter(owner=request.user)})
