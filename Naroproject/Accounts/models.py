from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
# Create your models here.

class User(AbstractBaseUser):

    email = models.EmailField(max_length= 255, unique=True, primary_key=True)
    date_of_birth = models.DateField(default = timezone.now)
    nickname = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
