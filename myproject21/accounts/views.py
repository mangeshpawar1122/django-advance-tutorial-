from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.

def register_view(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      messages.success(request, "Registration successfully and  logged in!")
      return redirect("dashboard")
    else:
      messages.error(request,"Registration failed. please corrent the errors below. ")
  else:
    form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})  
  


from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfully")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'accounts/login.html')

def logout_view(request):
  logout(request)
  messages.success(request,"You have been Logged out.")
  return redirect('login')
@login_required(login_url='login')
def dashboard_view(request):
  return render(request,'accounts/dashboard.html')