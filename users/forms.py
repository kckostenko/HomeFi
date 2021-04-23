from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
    # roomLoc = models.CharField(max_length=20)
    #ROOM_NAMES = [("living room", "living room")]
    #light_types = ['Floor Lamp', 'Table Lamp', 'Ceiling Light']
    # roomLoc = forms.ForeignKey(Room, on_delete=models.CASCADE)
    #roomLoc = forms.CharField(label="Room Location: ", widget=forms.Select(choices=ROOM_NAMES))
    lightName = forms.CharField(max_length=20)
    #lightType = forms.CharField(max_length=256)
    # , choices=[('floor lamp', 'floor lamp'), ('table lamp', 'table lamp'),
    #                                                          ('ceiling light', 'ceiling light')]
    # dimness = forms.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    dimness = forms.IntegerField(min_value=0, max_value=100)
    # apparently used for checkboxes? This is true and false use
    state = forms.BooleanField()
    # need something that can check a list of colors that can be a drop down
    # or a list that is here? maybe checkconstraint? charfield made for now
    color = forms.CharField(max_length=20)

    class Meta:
        model = Models.Light
        fields = ['lightName', 'state', 'dimness', 'color']
