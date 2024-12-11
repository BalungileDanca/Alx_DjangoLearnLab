
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

Customuser = get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        extra_kwargs = {'followers': {'read_only': True}}
class RegisterSerializer(serializers.ModelSerializer):
    # Explicitly define the password field for extra control (e.g., write-only)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customuser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Use the Django user manager to create the user
        user = Customuser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Create a token for the new user
        Token.objects.create(user=user)
        return user