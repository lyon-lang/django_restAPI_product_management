from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import PasswordResetView
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from .serializers import UserCreateSerializer
from rest_framework.decorators import api_view, permission_classes

from .tasks import sleepy

# Create your views here.


def myfistTask(request):
    #send_email_task()
   
    return HttpResponse('<h3>Email has been sent!</h3>')




class MyPasswordResetView(PasswordResetView):
    
    

  # forcing to use HTML email template (param: html_email_template_name)
    def form_valid(self, form):
      sleepy(10)
      opts = {
          'use_https': self.request.is_secure(),
          'token_generator': self.token_generator,
          'from_email': self.from_email,
          'email_template_name': self.email_template_name,
          'subject_template_name': self.subject_template_name,
          'request': self.request,
          'html_email_template_name': 'registration/password_reset_email.html',
          'extra_email_context': self.extra_email_context,
      }
      form.save(**opts)
      return HttpResponseRedirect(self.get_success_url())
