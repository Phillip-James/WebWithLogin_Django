from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from WebWithLogin.models import *
from django.contrib import admin

admin.site.register(profile)
admin.site.register(subscribed_items)