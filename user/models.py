from django.db import models

from django.contrib.auth.models import AbstractBaseUser,UserManager
from django.contrib.auth.models import PermissionsMixin




class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, null=True, blank=True)
    username = models.CharField(max_length=15, unique=True)
    is_admin = models.BooleanField(default=False,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)
    is_superuser = models.BooleanField(default=False,null=True,blank=True)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    full_name = models.TextField(null=True,blank=True)
    phone = models.CharField(max_length=10,null=False,blank=False)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return self.username
     


