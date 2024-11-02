from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required


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


@login_required  
def user_page(request, user_id):
    print(f"User: {request.user}, Is Authenticated: {request.user.is_authenticated}")  
    return render(request, "user_page.html", {
        "user_id": user_id,
        "user": request.user 
    })
