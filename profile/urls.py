from django.urls import path
from . import views

urlpatterns = [

		path('',views.home,name='home'),
		path('register/',views.register,name='register'),
		path('profile_register/<str:n>/',views.profile_register,name='profile_register'),
		path('login-h/',views.loginpage, name='login-h'),
		path('logout-h/',views.logoutUser, name='logout-h'),
		path('change_password/', views.change_password, name='change_password'),
		path('update_user', views.update_user, name='update_user'),



]