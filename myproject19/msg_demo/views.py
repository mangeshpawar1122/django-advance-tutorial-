from django.shortcuts import render
from django.contrib import messages
# Create your views here.

def show_msg(request):
  messages.debug(request,'This is a Debuging message.')
  messages.info(request,'This is a Info Messsage.')
  messages.success(request,'This is a success Message.')
  messages.warning(request,'This is a warning Message.')
  messages.error(request,'This is a error message.')
  return render(request,'massege.html')