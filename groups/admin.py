from django.contrib import admin
from groups.models import Group, GroupMembers

# Register your models here.

admin.site.register(Group)
admin.site.register(GroupMembers)
