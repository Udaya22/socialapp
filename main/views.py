from django.views.generic import ListView, CreateView
from .forms import UserCreateForm
from django.urls import reverse_lazy

# Create your views here.

class MainView(ListView):
    pass

class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'main/signup.html'
