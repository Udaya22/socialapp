from . import models
from main.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerDeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy

from django.conf import settings

# Create your views here.


class PostList(ListView):
    model = models.Post

class UserPosts(OwnerListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'

class PostDetail(OwnerDetailView):
    model = models.Post

class createPost(OwnerCreateView):
    model = models.Post
    user = settings.AUTH_USER_MODEL
    fields = ['message']

    def get_success_url(self):
        return reverse_lazy("posts:for_user",args=(self.request.user.username,))

class DeletePost(OwnerDeleteView):
    model = models.Post
    def get_success_url(self):
        return reverse_lazy("posts:for_user",args=(self.request.user.username,))

