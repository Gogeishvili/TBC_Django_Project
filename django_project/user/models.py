from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):  
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, unique=True)  
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 

    objects = CustomUserManager()

    USERNAME_FIELD = 'name'  
    REQUIRED_FIELDS = ['email']  

    def __str__(self):
        return self.email
