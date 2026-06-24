from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def set_cookie(request):
  response = HttpResponse('Cookie set Successfully')
  response.set_cookie('username','Mangesh Pawar',max_age=60*60*24*7) # Cookie store a 7 days
  response.set_cookie('course','Django Course',max_age=60*60*24*7)
  return response

def get_cookie(request):
  username = request.COOKIES.get('username','Guest')
  course = request.COOKIES.get('course','No Course selected')
  # return HttpResponse(f"Welcome User : {username} to your Course {course}")
  if 'username' in request.COOKIES:
    return HttpResponse(f"Welcome User : {username} to your Course {course}")
  else:
    return HttpResponse("user not found")


def delete_cookie(request):
  response = HttpResponse("All seccessfully Deleted")
  response.delete_cookie('username')
  response.delete_cookie('course')
  return response

  #return HttpResponse("All seccessfully Deleted")