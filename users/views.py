from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')
    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'User Successfully logout')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        'profile': profile,
        'topSkills': topSkills,
        'otherSkills': otherSkills,

    }
    return render(request, 'users/user-profile.html', context)
