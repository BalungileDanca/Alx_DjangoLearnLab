from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
     def create_user(self, username,bio, profile_picture, followers, password):
          # validation
          if not username:
               raise ValueError("username is required")
          user = self.model(username=username, bio=bio, profile_picture=profile_picture, password=password)
          user.set_password(password)
          user.save(using=self._db)
          return user
     
     def create_superuser(self, username, bio, profile_picture, password):
          user = self.create_user(username, bio, profile_picture, password)
          user.is_staff = True
          user.is_superuser = True
          user.save(using= self._db)
          return user

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=250)
    profile_picture= models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    following = models.ManyToManyField('self', symmetrical=False, related_name='follows')

    objects = UserManager()
    REQUIRED_FIELDS = []

