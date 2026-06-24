from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_profile, name='upload_profile'),
    path('profile/', views.profile_view, name='profile_view'),
]
