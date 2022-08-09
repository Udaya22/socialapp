from django.contrib import admin

from main.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(User, UserAdmin)
