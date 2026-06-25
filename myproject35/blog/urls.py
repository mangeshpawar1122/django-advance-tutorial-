from . import views 
from django.urls import path

urlpatterns = [
    path('user/',views.user_list,name='user_list'),
    path('clear/',views.clear_cache,name='clear_cache'),
]
