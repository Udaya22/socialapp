from django.urls import reverse
from django.db import models
from django.conf import settings
from groups.models import Group, GroupMembers

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
    
    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.Username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']