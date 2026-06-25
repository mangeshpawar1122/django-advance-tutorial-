from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache
# Create your views here.

def user_list(request):
  users = cache.get('users_list')

  if not users:
    print("cache miss :querying database for user !")
    users = UserProfile.objects.all()
    cache.set('users_list',users,timeout=60)
  else:
    print('cache hit :retrieved users from cache ! ')  
  return render(request,'user.html',{'user':users})