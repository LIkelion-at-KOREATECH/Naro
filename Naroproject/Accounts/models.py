from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    The_date_of_ones_birth = models.DateTimeField(default='1950-01-01')
    email = models.CharField(max_length=40, default='example@example.com')