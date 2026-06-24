from django.urls import path
from . import views

urlpatterns = [
    path('send-test/',views.send_test_email,name='send_test_email')
]
