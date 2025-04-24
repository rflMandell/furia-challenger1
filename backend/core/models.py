from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_fan = models.BooleanField(default=True) #para users normais
    is_admin = models.BooleanField(default=False) #para admins
    #em breve mais campo?? talvez :)
    