from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200,null=True)
	phone_number = PhoneNumberField(region="IN")
	

	def __str__(self):
		return self.name