from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from profile.models import *
from profile.api.serializers import *

from django.contrib.auth.models import User
import json


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



@api_view(['POST'])
def profile_add(request,userId):
	user = User.objects.get(id=userId)
	profile ,created = Profile.objects.get_or_create(user=user)
	serializer = ProfileSerializer(instance=profile,data=request.data)
	data = {}
	if serializer.is_valid():
		serializer.save()
		profile.name = user.username
		profile.email = user.email
		profile.save()
		data["success"] = "create successfull"
	else:
		data["failure"] = serializer.errors
	return Response(data=data)

@api_view(['PUT'])
def user_update(request):

    
    try:
         user=request.user
           

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(instance=user ,data=request.data)
    data={}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "update success"
        return Response(data=data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)