from django.urls import path
from . import views

urlpatterns = [
    path('user-profile',views.user_profile_view,name='user_profile_view'),
]
