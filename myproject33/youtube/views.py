from django.shortcuts import render
from django.core.cache import cache
from . models import YouTubeUser
# Create your views here.

def users_list(request):
  users = cache.get('user_data')
  if not users:
    print('Cache Miss : Fetching data from database')
    users = YouTubeUser.objects.all()
    cache.set('user_data',users,timeout=60) # time out is a 60 seconds
  else:
    print('cache hit : Fetching data from cache')

  return render(request,'user_list.html',{'user':users})
