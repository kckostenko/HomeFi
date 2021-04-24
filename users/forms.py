from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxLengthValidator, MinLengthValidator

from homepg import models as Models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    class Meta:
        # Class Meta keeps our configurations in one place
        # The model is the User model
        # the fields are what fields are in the form and in what order!
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class addLights(forms.Form):
    #order it by the user as well? like the id or whatever somehow?
    #check all of the querying possibilities that wrote down as to how to be specfiic
    # do we need to filter thruogh using the current user?
    lightName = forms.CharField(max_length=20, label='Light Name')
    roomLoc = forms.ModelChoiceField(queryset=Models.Room.objects.all(), label='Room Location')
    lightType = forms.CharField(max_length=20,label='Light Type', widget=forms.Select(choices=[('default light','default light'),
                                                                                               ('floor lamp','floor lamp'),
                                                                                                ('table lamp', 'table lamp'),
                                                                                                ('ceiling light', 'ceiling light')]))
    dimness = forms.IntegerField(initial=0, min_value=0, max_value=100, label='Dimness', required=False)
    state = forms.BooleanField(required=False, label='ON/OFF')
    # need something that can check a list of colors that can be a drop down
    # or a list that is here? maybe checkconstraint of if its a color or not?

    #initial='yellow' for a default color?
    color = forms.CharField(max_length=20, label='Color', required=False)
    class Meta:
        model = Models.Light
        fields = ['lightName', 'roomLoc', 'lightType', 'state', 'dimness', 'color']

class addLocks(forms.Form):
    lockName = forms.CharField(min_length=2, max_length=20, label='Lock Name')
    roomLoc = forms.ModelChoiceField(queryset=Models.Room.objects.all(), label='Room Location')
    state = forms.BooleanField(required=False, label='LOCKED/UNLOCKED')
    code1 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='First Code')
    code2 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Second Code')
    code3 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Third Code')
    code4 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Fourth Code')
    class Meta:
        model = Models.Lock
        fields = ['lockName', 'roomLoc', 'state', 'code1', 'code2', 'code3', 'code4']

class addAlarm(forms.Form):
    alarmName = forms.CharField(min_length=2, max_length=20, label='Alarm Name')
    state = forms.BooleanField(required=False, label='ARMED/DISARMED')
    code1 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='First Code')
    code2 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Second Code')
    code3 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Third Code')
    code4 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Fourth Code')
    class Meta:
        model = Models.Alarm
        fields = ['alarmName', 'state', 'code1', 'code2', 'code3', 'code4']
