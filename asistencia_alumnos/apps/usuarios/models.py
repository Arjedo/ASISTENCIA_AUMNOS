
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    biografia = models.CharField(max_length=255, null=True, blank=True)