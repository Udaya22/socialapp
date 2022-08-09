from django.db import IntegrityError
from django.contrib import messages

from django import views
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from groups.models import Group, GroupMembers
from django.urls import reverse, reverse_lazy

from main.owner import OwnerListView, OwnerDetailView

from django.shortcuts import redirect

from posts.models import Post

# Create your views here.

class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    fields = ['name' , 'description']
    success_url = reverse_lazy("groups:all")

    def form_valid(self, form):
        group = form.save()
        user = self.request.user
        GroupMembers.objects.create(group=group, user=user)
        return super().form_valid(form)

class GroupsList(ListView):
    model = Group

class GroupDetail(OwnerDetailView):
    model = Group

class JoinGroup(LoginRequiredMixin, views.View):
    
    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        try:
            GroupMembers.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request,("You are already a member of this group{}".format(group.name)))

        return redirect(reverse_lazy('groups:single', args=[pk]))

class LeaveGroup(LoginRequiredMixin, views.View):

    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        group_member = GroupMembers.objects.get(group=group,user=self.request.user)
        try:
            group_member.delete()
        
        except:
            messages.warning(self.request,("Unable to leave from group{}".format(group.name)))
        
        return redirect(reverse_lazy('groups:single', args=[pk]))

class UserGroupList(OwnerListView):

    model = GroupMembers
    template_name = 'groups/user_group_list.html'

class CreateGroupPost(CreateView):
    
    model = Post
    template_name= 'posts/post_form.html'
    fields=['message']
    
    def get_success_url(self):
        return reverse_lazy('groups:single', args=[self.kwargs['pk']])

    def form_valid(self, form):
        object = form.save(commit=False)
        object.group = Group.objects.get(pk=self.kwargs['pk'])
        object.user = self.request.user
        object.save
        return super(CreateGroupPost, self).form_valid(form)

