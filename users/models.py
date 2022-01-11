from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import time
import uuid


class CustomUserManager(BaseUserManager):
    """this class to set some override functions for users"""

    def _create_user(self, email, password, **extra_fields):
        """Fx to create a simple user"""
        if not email:
            raise ValueError('You must provide your email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Fx to create a super user"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('name', 'admin')
        extra_fields.setdefault('phone_number', '0991991320')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('A super user must have a is_staff set to True')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('A super user must have is_superuser set to True')

        create = self._create_user(email, password, **extra_fields)
        return create


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    """Class for customer user model instead of the system model"""

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_number = models.CharField(default=0, max_length=25)
    dob = models.DateField(null=True, default=None)
    position = models.CharField(max_length=255, null=True, blank=True, default=None)
    city = models.CharField(max_length=255, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    # For super user

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.email
