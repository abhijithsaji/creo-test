from django.shortcuts import render ,redirect ,HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home(request):
	return render(request,'index.html')


def register(request):

    form = CreateUserForm()
    #form2 = ProfileForm()
    user=''
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            
            messages.success(request, 'Account was created for ' + username)

            profile = Profile.objects.get_or_create(user=user,name=username,email=email)
            # form2 = ProfileForm(instance=profile,request.post)
            # if form2.is_valid():
            # 	form2.save()
            #Token.objects.create(user=user)

            context = {'user':user}

            return redirect('profile_register',user.id)
    context = {'form':form,'user':user}
    return render(request, 'register.html',context)

def profile_register(request,n):

    
    form = ProfileForm()

    if request.method == 'POST':
    	profile = Profile.objects.get(user=n)
    	form = ProfileForm(instance=profile, data=request.POST)
    	if form.is_valid():
            form.save()
            
            
            
            
            #profile = Profile.objects.get_or_create(user=user,name=username,email=email)
            # form2 = ProfileForm(instance=profile,request.post)
            # if form2.is_valid():
            # 	form2.save()
            #Token.objects.create(user=user)

            
            return redirect('login')
    context = {'form':form}
    return render(request, 'register2.html',context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

@login_required(login_url='login')
def update_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        messages.success(request, 'Your password was successfully updated!')
        return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'update_user.html', {'form': form})