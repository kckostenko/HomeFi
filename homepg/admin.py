from django.contrib import admin
from .models import Post, SmartHome, Room, Light, Lock, Alarm
# Register your models here.

admin.site.register(Post)
admin.site.register(SmartHome)
admin.site.register(Room)
admin.site.register(Light)
admin.site.register(Lock)
admin.site.register(Alarm)