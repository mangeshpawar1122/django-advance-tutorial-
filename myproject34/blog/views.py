from django.shortcuts import render
from django.core.cache import cache
from .models import UserProfile
# Create your views here.

def user_profile_view(request):
  users_data=cache.get('users_data')
  if users_data is None:
    print('Fetching data from database')
    users_data=UserProfile.objects.all()
    cache.set('users_data',users_data)
  else:
    print('Fetching data from cache')

  return render(request,'user-profile-view.html',{'user':users_data})