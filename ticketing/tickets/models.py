from django.db import models 
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth import get_user_model


# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            raise ValueError("email is not provided here, email is required.")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)      
    is_superuser = models.BooleanField(default=False)   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'low'),
        ('medium', 'medium'),
        ('high', 'high')
    ]

    STATUS = [
        ('open', 'open'),
        ('in progress', 'in progress'),
        ('closed', 'closed')
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title