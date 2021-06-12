from django.db import models
from primitiva_project.models import DateRegister
from .managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class User(AbstractBaseUser, PermissionsMixin, DateRegister):
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=24, unique=True)
    about = models.TextField(_('about'), max_length=500, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f"{self.username} - {self.email}"
