from django.urls import path
from profile.api.views import *
app_name = 'profile'


urlpatterns = [
	path('profile_add/user=<int:userId>/', profile_add, name="profile_add"),
	path('user_update/',user_update, name="user_update"),		


	]