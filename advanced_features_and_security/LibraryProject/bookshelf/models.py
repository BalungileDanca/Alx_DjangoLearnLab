from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    publication_year = models.IntegerField(null=True)

    class Meta:
        permissions = [
            ('can_view', 'can view'),
            ('can_edit', 'can edit'),
            ('can_create', 'can create'),
            ('can_delete', 'can delete'),
        ]

    def __str__(self):
        return self.title


    

from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class CustomUserManager(BaseUserManager):
    """
    Custom manager for CustomUser
    """

    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        """
        Creates and returns a regular user with an email, username, and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo)
        user.set_password(password)  # Encrypt the password
        user.save(using=self._db)  # Save the user instance in the database
        return user

    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None):
        """
        Creates and returns a superuser with email, username, password, and the required fields.
        """
        user = self.create_user(username, email, password, date_of_birth, profile_photo)
        user.is_staff = True  # Set staff status for superuser
        user.is_superuser = True  # Set superuser status
        user.save(using=self._db)  # Save the superuser instance in the database
        return user

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    # Add custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    

from django.db import models
from django.conf import settings

class LogEntry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name='bookshelf_logentries'  # Use a unique related_name
    )
   
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title



    
