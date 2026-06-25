from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mass_mail, EmailMultiAlternatives
from django.template.loader import render_to_string

# Create your views here.

# def send_bulk_email(request):
#   message1 = ('Wlcome user 1', 'Hello User 1 to our platform','pawarmangesh112203@gmail.com',['pawarmangesh860@gmail.com'])
#   message2 = ('Wlcome user 2', 'Hello User 2 to our platform','pawarmangesh112203@gmail.com',['pawarmangesh86@gmail.com'])
#   message3 = ('Wlcome user 3', 'Hello User 3 to our platform','pawarmangesh112203@gmail.com',['pawarmangesh80@gmail.com'])
#   message4 = ('Wlcome user 4', 'Hello User 4 to our platform','pawarmangesh112203@gmail.com',['pawarmangesh60@gmail.com'])
#   send_mass_mail((message1,message2,message3,message4), fail_silently=False)
#   return HttpResponse('Email send successfully')


def send_bulk_email(request):
  subject = "Welcome to our platform"
  from_email = "pawarmangesh112203@gmail.com"
  recipient_list = ['pawarmangesh860@gmail.com','pawarmangesh806@gmail.com']
  html_content = render_to_string('welcome_email.html',{'username':'Mangesh'})

  msg =EmailMultiAlternatives(subject, 'welcome to my blog ',from_email,recipient_list)
  msg.attach_alternative(html_content,'text/html')
  msg.send()
  #msg.attach_file('path/to/your/attachment.png') #optional attachment a files and images 

  return HttpResponse('Email send Successfully !')