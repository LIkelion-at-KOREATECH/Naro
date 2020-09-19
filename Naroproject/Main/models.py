from django.db import models

# Create your models here.

class Textmodel(models.Model):
    answer = models.TextField(max_length=200, default="대답해주세요")