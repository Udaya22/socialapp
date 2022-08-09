from django.db import models

from django.conf import settings
from django.urls import reverse

# Create your models here.

# https://docs.djangoproject.com/en/4.0/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag

class Group(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='GroupMembers')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'id':self.id})


class GroupMembers(models.Model):

    group = models.ForeignKey(Group, related_name='memberships', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_groups', on_delete=models.CASCADE)

    def __str__(self):
        return self.group.name

    class Meta:
        unique_together = ('group','user')
