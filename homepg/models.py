# models everywhere is so that the database is updated
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

def requesting(request):
    currentOwner = request.user
    return currentOwner

# inherits from the above models class so in the parenthesis below
class Post(models.Model):
    # now create attributes and so each is a different field in DB
    # so now add fields for the table in DB
    title = models.CharField(max_length=100)
    # text field is just unrestricted text
    content = models.TextField()
    # update the date posted to current date time each time the post
    # was edited for auto_now so going to use one that uses creation time
    # only of auto_now_add but to change as an option then use
    # default=timezone.now
    date_posted = models.DateTimeField(default=timezone.now)
    # now need the user for the author so get that from other table and add
    # the place up above- on delete says if user deleted if delete post too
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # create a dunder method to control how we want this to printed out
    def __str__(self):
        return self.title


class SmartHome(models.Model):
    houseName = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # create a dunder method to control how we want this to printed out

    def __str__(self):
        return self.houseName


# have to fill out room name first after making name for house or cannot add
# lights or anything since rooms will be drop down with options? this way
# the rooms field will always be filled out in the DB, need this to know where

# also can make a query for all and get them all and then add them into a text box
# drop down thing for rooms with this owner etc
class Room(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    roomName = models.CharField(max_length=20)

    # create a dunder method to control how we want this to printed out

    def __str__(self):
        return self.roomName


class Light(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # does it need to be a foreign key or can it just be a char field?
    roomLoc = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    lightName = models.CharField(max_length=20)
    lightType = models.CharField(default='default light', max_length=20,
                                 choices=[('default light', 'default light'), ('floor lamp', 'floor lamp'),
                                          ('table lamp', 'table lamp'), ('ceiling light', 'ceiling light')])
    dimness = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    # apparently used for checkboxes? This is true and false use
    state = models.BooleanField(default=0)
    # need something that can check a list of colors that can be a drop down
    # or a list that is here? maybe checkconstraint? charfield made for now
    color = models.CharField(max_length=20)

    # create a dunder method to control how we want this to printed out

    def __str__(self):
        return self.lightName
    # maybe how to get the objects from another class? by query: models.QuerySet()


# not sure how to add a list so there can be a list of codes to choose from or add?
# will this be its own class for the codes? or can you make a list? or add a code at a time and
# check that against the lock name so if the code matches then the lock has that code as
# well as others so many locks but code is what is different in table

class Lock(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    lockName = models.CharField(max_length=20)
    roomLoc = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    state = models.BooleanField(default=0)
    code1 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    code2 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    code3 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    code4 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])

    # create a dunder method to control how we want this to printed out

    def __str__(self):
        return self.lockName


class Alarm(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    alarmName = models.CharField(max_length=20)
    state = models.BooleanField(default=0)
    code1 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    code2 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    code3 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    code4 = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1000), MaxValueValidator(9999)])

    # create a dunder method to control how we want this to printed out

    def __str__(self):
        return self.alarmName


'''
class SmartHome2(models.Model):
    houseName = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Room2(models.Model):
    houseName = models.ForeignKey(SmartHome2.houseName, on_delete=models.CASCADE)
    owner = models.ForeignKey(SmartHome.owner, on_delete=models.CASCADE)
    roomName = models.CharField(max_length=20)

class Light2(models.Model):
    houseName = models.ForeignKey(Room2.houseName, on_delete=models.CASCADE)
    owner = models.ForeignKey(Room2.owner, on_delete=models.CASCADE)
'''
