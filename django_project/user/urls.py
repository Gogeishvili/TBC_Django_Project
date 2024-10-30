from django.urls import path
from django.contrib.auth import views
from user import views


app_name='user'

urlpatterns = [
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogOutView.as_view(),name='log_out'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path("<int:user_id>/", views.user_main_page, name="user_main_page"),
]
