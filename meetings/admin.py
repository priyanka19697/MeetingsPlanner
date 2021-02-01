from django.contrib import admin

# Register your models here.

from .models import Meeting, MeetingRoom

# add classes which u want the admin to access
admin.site.register(Meeting)
admin.site.register(MeetingRoom)
