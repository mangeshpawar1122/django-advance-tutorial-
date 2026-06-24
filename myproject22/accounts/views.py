from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile


def login_view(request):
    next_url = request.GET.get('next', '')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect(next_url or 'profile_view')

        messages.error(request, "Invalid username or password.")

    return render(request, 'accounts/login.html', {'next': next_url})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile Picture Uploaded Successfully!")
            return redirect('profile_view')

        messages.error(request, "Error Uploading Profile Picture. Please try again.")
    else:
        form = ProfileForm()

    return render(request, 'accounts/upload_profile.html', {'form': form})


@login_required(login_url='login')
def profile_view(request):
    profiles = Profile.objects.all()
    return render(request, 'accounts/view_profile.html', {'profiles': profiles})
