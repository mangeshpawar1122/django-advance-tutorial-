from . import views
from django.urls import path

urlpatterns = [
    path('user/',views.user_list,name='user_list')
]
