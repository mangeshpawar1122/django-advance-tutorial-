from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# Create your views here.
# def send_test_email(request):
#   subject = "Welcome to my Blog"
#   message = "Thank You for coming my site"
#   from_email = "pawarmangesh112203@gmail.com"
#   recipient_list = ["pawarmangesh860@gmail.com"]

#   send_mail(subject, message, from_email, recipient_list)
#   return HttpResponse("Test email send successfully")

def send_test_email(request):
    subject = "Welcome to my Blog"
    message = render_to_string('email/welcome_email.html',{
       'username':'mangesh',
       'course': 'Django Tutorial'
    })
    email = EmailMessage(
       subject,
       message,
       "pawarmangesh112203@gmail.com",
       ["pawarmangesh860@gmail.com"],

    )
    email.content_subtype = 'html' # main content is now text/html
    email.send()
    return HttpResponse("Email send Successfully")  
