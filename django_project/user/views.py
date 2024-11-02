from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .models import User


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("store:index")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    next_page = reverse_lazy("store:index")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.next_page)


class LogOutView(LogoutView):
    next_page = reverse_lazy("store:index")


@method_decorator(login_required, name="dispatch")
class UserPageView(DetailView):
    template_name = "user_page.html"
    model = User
    context_object_name = "user"

    def get_object(self, queryset=...):
        return self.request.user
