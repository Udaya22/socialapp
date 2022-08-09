from distutils.log import Log
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerListView(ListView):
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class OwnerDetailView(DetailView):
    """
    Sub-class to view a detail page 
    """

class OwnerCreateView(LoginRequiredMixin, CreateView):
    
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.save
        return super(OwnerCreateView, self).form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
