from django.shortcuts import render, redirect
from django.contrib.auth import login
from .form import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()

    return render(request,'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request,'registration/profile.html')

from django.contrib.auth.forms import UserChangeForm

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'registration/edit_profile.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        request.user.email = request.POST.get('email', '')
        request.user.save()
    return render(request, 'profile.html', {'user': request.user})



