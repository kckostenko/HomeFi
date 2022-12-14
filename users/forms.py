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
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(addLights, self).__init__(*args, **kwargs)
        self.fields['roomLoc'] = forms.ModelChoiceField(Models.Room.objects.filter(owner=user), label='Room Location')
        self.order_fields(self.Meta.fields)

    # roomLoc = forms.ModelChoiceField(queryset=Models.Room.objects.all(), label='Room Location')
    # order it by the user as well? like the id or whatever somehow?
    # check all of the querying possibilities that wrote down as to how to be specfiic
    # do we need to filter thruogh using the current user?
    lightName = forms.CharField(max_length=20, label='Light Name')
    # roomLoc = forms.ModelChoiceField(queryset=Models.Room.objects.all(), label='Room Location')
    # roomLoc = forms.ModelChoiceField(queryset=Models.Room.objects.filter(owner=user.id), label='Room Location')
    lightType = forms.CharField(max_length=20, label='Light Type',
                                widget=forms.Select(choices=[('default light', 'default light'),
                                                             ('floor lamp', 'floor lamp'),
                                                             ('table lamp', 'table lamp'),
                                                             ('ceiling light', 'ceiling light')]))
    dimness = forms.IntegerField(initial=0, min_value=0, max_value=100, label='Dimness', required=False)
    state = forms.BooleanField(required=False, label='ON/OFF')
    # need something that can check a list of colors that can be a drop down
    # or a list that is here? maybe checkconstraint of if its a color or not?

    # initial='yellow' for a default color?
    color = forms.CharField(max_length=20, label='Color', required=False)

    class Meta:
        model = Models.Light
        fields = ['lightName', 'roomLoc', 'lightType', 'state', 'dimness', 'color']


class removeLights(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(removeLights, self).__init__(*args, **kwargs)
        self.fields['lightName'] = forms.ModelChoiceField(
            queryset=Models.Light.objects.filter(owner=None) | Models.Light.objects.filter(owner=user),
            label="Light Name")

    class Meta:
        model = Models.Light


class addLocks(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(addLocks, self).__init__(*args, **kwargs)
        self.fields['roomLoc'] = forms.ModelChoiceField(
            queryset=Models.Room.objects.filter(owner=None) | Models.Room.objects.filter(owner=user),
            label='Room Location')
        self.order_fields(self.Meta.fields)

    lockName = forms.CharField(min_length=2, max_length=20, label='Lock Name')
    # roomLoc = forms.ModelChoiceField(queryset=Models.Room.objects.filter(user=request.user), label='Room Location')
    state = forms.BooleanField(required=False, label='LOCKED/UNLOCKED')
    code1 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='First Code')
    code2 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Second Code')
    code3 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Third Code')
    code4 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Fourth Code')

    class Meta:
        model = Models.Lock
        fields = ['lockName', 'roomLoc', 'state', 'code1', 'code2', 'code3', 'code4']


class removeLocks(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(removeLocks, self).__init__(*args, **kwargs)
        self.fields['lockName'] = forms.ModelChoiceField(
            queryset=Models.Lock.objects.filter(owner=None) | Models.Lock.objects.filter(owner=user), label="Lock Name")

    # lockName = forms.CharField(max_length=20,label='Lock Name', widget=forms.Select(choices=[('lock1','lock1'),
    #                                                                                            ('lock1','lock1')]))
    # lockName = forms.CharField(min_length=2, max_length=20, label="Lock Name")
    entryPin = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Enter Code')

    class Meta:
        model = Models.Lock


class changeLockForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(changeLockForm, self).__init__(*args, **kwargs)
        self.fields['roomLoc'] = forms.ModelChoiceField(
            queryset=Models.Room.objects.filter(owner=None) | Models.Room.objects.filter(owner=user),
            label='Room Location')
        self.fields['lockName'] = forms.ModelChoiceField(
            queryset=Models.Lock.objects.filter(owner=None) | Models.Lock.objects.filter(owner=user),
            label="Current Lock Name")
        self.order_fields(self.Meta.fields)

    newNameBool = forms.BooleanField(required=False, label='Change Name? Y/N',
                                     widget=forms.CheckboxInput(attrs={'checked': True}))
    newName = forms.CharField(required=False, min_length=2, max_length=20, label='New Lock Name')
    # roomLoc = forms.ModelChoiceField(queryset=Models.Room.objects.filter(user=request.user), label='Room Location')
    state = forms.BooleanField(required=False, label='LOCKED/UNLOCKED')
    code1 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='First Code')
    code2 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Second Code')
    code3 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Third Code')
    code4 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Fourth Code')

    class Meta:
        model = Models.Lock
        # fields = ['lockName','roomLoc', 'state', 'code1', 'code2', 'code3', 'code4']
        fields = ['lockName', 'newNameBool', 'newLockName', 'roomLoc', 'state', 'code1', 'code2', 'code3', 'code4']


class lockPin(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(lockPin, self).__init__(*args, **kwargs)
        self.fields['lockName'] = forms.ModelChoiceField(
            queryset=Models.Lock.objects.filter(owner=None) | Models.Lock.objects.filter(owner=user), label="Lock Name")
        self.order_fields(self.Meta.fields)

    entryPin = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Enter PIN Code')

    class Meta:
        model = Models.Lock
        fields = ['lockName', 'entryPin']


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


class changeAlarmForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(changeAlarmForm, self).__init__(*args, **kwargs)
        # self.fields['roomLoc'] = forms.ModelChoiceField(queryset=Models.Room.objects.filter(owner=None) | Models.Room.objects.filter(owner=user), label='Room Location')
        self.fields['alarmName'] = forms.ModelChoiceField(
            queryset=Models.Alarm.objects.filter(owner=None) | Models.Alarm.objects.filter(owner=user),
            label="Current Alarm Name")
        self.order_fields(self.Meta.fields)

    newNameBool = forms.BooleanField(required=False, label='Change Name? Y/N',
                                     widget=forms.CheckboxInput(attrs={'checked': True}))
    newName = forms.CharField(required=False, min_length=2, max_length=20, label='New Lock Name')
    state = forms.BooleanField(required=False, label='ARMED/DISARMED')
    code1 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='First Code')
    code2 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Second Code')
    code3 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Third Code')
    code4 = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Fourth Code')

    class Meta:
        model = Models.Alarm
        fields = ["alarmName", "newNameBool", "newName", "state", "code1", "code2", "code3", "code4"]


class alarmPin(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(alarmPin, self).__init__(*args, **kwargs)
        self.fields['alarmName'] = forms.ModelChoiceField(
            queryset=Models.Alarm.objects.filter(owner=None) | Models.Alarm.objects.filter(owner=user),
            label="Alarm Name")

    entryPin = forms.IntegerField(initial=1000, min_value=1000, max_value=9999, label='Enter PIN Code')

    class Meta:
        model = Models.Alarm


class addRoomForm(forms.Form):
    roomName = forms.CharField(min_length=2, max_length=30, label='Room Name')

    class Meta:
        model = Models.Room


class deleteRoomForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(deleteRoomForm, self).__init__(*args, **kwargs)
        self.fields['roomName'] = forms.ModelChoiceField(
            queryset=Models.Alarm.objects.filter(owner=None) | Models.Alarm.objects.filter(owner=user),
            label="Room Name")

    class Meta:
        model = Models.Room


class changeLightForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(changeLightForm, self).__init__(*args, **kwargs)
        self.fields['roomLoc'] = forms.ModelChoiceField(
            queryset=Models.Room.objects.filter(owner=None) | Models.Room.objects.filter(owner=user),
            label='Room Location')
        self.fields['lightName'] = forms.ModelChoiceField(
            queryset=Models.Light.objects.filter(owner=None) | Models.Light.objects.filter(owner=user),
            label="Light Name")
        self.order_fields(self.Meta.fields)

    newNameBool = forms.BooleanField(required=False, label='Change Name? Y/N',
                                     widget=forms.CheckboxInput(attrs={'checked': True}))
    newName = forms.CharField(required=False, min_length=2, max_length=20, label='New Lock Name')
    lightType = forms.CharField(max_length=20, label='Light Type',
                                widget=forms.Select(choices=[('default light', 'default light'),
                                                             ('floor lamp', 'floor lamp'),
                                                             ('table lamp', 'table lamp'),
                                                             ('ceiling light', 'ceiling light')]))
    dimness = forms.IntegerField(initial=0, min_value=0, max_value=100, label='Dimness', required=False)
    state = forms.BooleanField(required=False, label='ON/OFF')
    color = forms.CharField(max_length=20, label='Color', required=False)

    class Meta:
        model = Models.Light
        fields = ['lightName', "newNameBool", "newName", 'roomLoc', 'lightType', 'state', 'dimness', 'color']
