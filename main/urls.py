from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('',views.MainView.as_view(),name="groups-list"),
    path('signup',views.SignUp.as_view(),name="signup"),
]