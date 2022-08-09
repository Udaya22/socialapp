from django import urls
from django.urls import path
from groups.views import CreateGroup, GroupsList, GroupDetail, JoinGroup, LeaveGroup, UserGroupList, CreateGroupPost

app_name = 'groups'

urlpatterns = [
    path('',GroupsList.as_view(),name='all'),
    path('new',CreateGroup.as_view(),name='create'),
    path('posts_in/<pk>',GroupDetail.as_view(),name='single'),
    path('join/<pk>',JoinGroup.as_view(),name='join'),
    path('leave/<pk>',LeaveGroup.as_view(),name="leave"),
    path('for/<username>',UserGroupList.as_view(),name='for_user'),
    path('post_to/<pk>', CreateGroupPost.as_view() , name="group_post")
]