from django.contrib import admin
from . models import YouTubeUser
from django.core.cache import cache
from django.contrib import messages

@admin.action(description='Clear User Cache')
def clear_user_cache(modeladmin, request,queryset):
  cache.delete('users_data')
  messages.success(request,'User cache clear Successfully !')

# Register your models here.
@admin.register(YouTubeUser)
class YouTubeUserAdmin(admin.ModelAdmin):
  list_display = ['name','email','subscribers']
  actions = [clear_user_cache]