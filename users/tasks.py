from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None

# @shared_task
# def send_email_task():
#     #sleep(10)
#     send_mail('CELERY TASK WORKED!',
#     'tHIS IS A PROOF THAT IT WORKED!',
#     'support@lyon.org',
#     ['yankson.kojo@yahoo.com'])

#     return None

