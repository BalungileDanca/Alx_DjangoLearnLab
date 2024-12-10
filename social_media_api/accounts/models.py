from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=250)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')

