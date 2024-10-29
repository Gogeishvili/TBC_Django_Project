from django.shortcuts import render
from .forms import RegisterForm,LoginForm 
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('store:index')

    def form_valid(self, form):
        user = form.save()  
        login(self.request, user) 
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginView(LoginView):
    template_name = 'login.html'  
    authentication_form = LoginForm
    next_page = reverse_lazy('store:index')  

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.next_page)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect(self.next_page)  

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))







def user_main_page(request,user_id):
    return render(
        request, "index.html", {
            'user_id':user_id
        }
    )