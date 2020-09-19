from rest_framework import serializers
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from profile.models import*
from phonenumber_field.modelfields import PhoneNumberField


class ProfileSerializer(serializers.ModelSerializer):
	phone_number = PhoneNumberField(region="IN")
	class Meta:
		model = Profile
		fields = ['phone_number']

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ['username','email']