from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration.forms import AuthUserForm, RegistrationForm


class RegistrationNewUser(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class AuthUser(LoginView):
    form_class = AuthUserForm
    template_name = 'registration/authorization.html'

    def get_success_url(self):
        return reverse_lazy('home')


class ExitFromSite(LogoutView):

    def get_next_page(self):
        return reverse_lazy('home')
