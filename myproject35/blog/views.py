from django.shortcuts import render
from django.http import HttpResponse
from .models import UserList
from django.views.decorators.cache import cache_page
from django.core.cache import cache
# Create your views here.

@cache_page(30)
def user_list(request):
  print('Fatching a data from database')
  users = UserList.objects.all()
  return render(request,'user.html',{"user":users})

def clear_cache(request):
  cache.clear()
  return HttpResponse('all cache cleared')