from django.db import models
from user.models import User


class UserCard(models.Model):
    name = models.CharField(max_length=30, default="user card")
    user = models.OneToOneField(User, verbose_name="user_card", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name}'s {self.name}"
