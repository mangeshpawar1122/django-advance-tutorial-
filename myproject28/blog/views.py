from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def set_session(request):
  request.session['username']='mangesh'
  request.session['course'] = 'Django full course' 
  return HttpResponse("Session data save succesfully !")

def get_session(request):
  username = request.session.get('username','Guest')
  course = request.session.get('course', 'Not enrolled')
  return HttpResponse(f"Welcom : {username} You are learning {course} ")

def delete_session(request):
  # try:
  #   del request.session['username']
  #   del request.session['course']
  # except KeyError:
  #   pass
  # return HttpResponse('session deta delete succesfully !')

  
  request.session.flush() # this will delete all session
  return HttpResponse('All session data deleted succesfully')

