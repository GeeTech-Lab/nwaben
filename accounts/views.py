from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .models import User
from .forms import UserChangeForm

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from accounts import forms


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
    template_name = "accounts/login.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    # Takes users to success_url if the login...
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


# The default django signup form uses only username tp log users
# if you want to use email, then create form.py
class SignupView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/register.html"


class UpdateUserProfileView(generic.UpdateView ):
    template_name = 'accounts/update_profile.html'
    model = User
    form_class = UserChangeForm
    fields = ["phone", "avatar", "bio"]
    success_url = reverse_lazy('profile')


class UserProfileView(generic.DetailView, generic.UpdateView):
    template_name = "accounts/profile.html"
    model = User
    fields = ["phone", "avatar", "bio"]
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user
