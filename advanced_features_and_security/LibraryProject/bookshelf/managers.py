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