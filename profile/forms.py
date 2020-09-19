from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import*


class CreateUserForm(UserCreationForm):

	
	class Meta:
		model = User
		fields = ['username', 'email','password1', 'password2']

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['phone_number']

class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
