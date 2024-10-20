from django.db import models
from user.models import User

class UserCard(models.Model):
    user = models.ForeignKey(User, verbose_name="user_card", on_delete=models.CASCADE)
