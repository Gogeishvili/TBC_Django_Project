from django.urls import path
from user import views

app_name='user'

urlpatterns = [
    path("<int:user_id>/", views.user_main_page, name="user_main_page"),
]
