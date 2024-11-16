from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    publication_year = models.IntegerField(null=True)


from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
     def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
         if not date_of_birth:
             raise ValueError('date of birth is required')
         user = self.model(username=username, date_of_birth=date_of_birth, profile_photo=profile_photo)
         user.set_password(password)
         user.save(using=self._db)
         return user
     def create_superuser(self, username, password=None, date_of_birth=None, profile_photo=None):
         user = self.create_user(username, password, date_of_birth, profile_photo)
         user.is_staff = True
         user.is_superuser = True
         user.save(using=self._db)
         return user
          
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username
   

# Create your models here.
