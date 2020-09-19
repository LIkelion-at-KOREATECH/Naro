from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
# Create your models here.

class User(AbstractBaseUser):

    email = models.EmailField(max_length= 255, unique=True, primary_key=True)
    date_of_birth = models.DateField(default = timezone.now)

    nickname = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'

    # MBTI
    MBTI_CHOICES = (
        ('ISTJ', 'ISTJ'),
        ('ISFJ','ISFJ'),
        ('INFJ','INFJ'),
        ('INTJ','INTJ'),
        ('ISTP','ISTP'),
        ('ISFP','ISFP'),
        ('INFP','INFP'),
        ('INTP','INTP'),
        ('ESTP','ESTP'),
        ('ESFP','ESFP'),
        ('ENTP','ENTP'),
        ('ENFP','ENFP'),
        ('ESTJ','ESTJ'),
        ('ESFJ','ESFJ'),
        ('ENFJ','ENFJ'),
        ('ENTJ','ENTJ'),
    )
    mbti_result = models.CharField(max_length=5, choices=MBTI_CHOICES)