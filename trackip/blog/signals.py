from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User



def login_success(sender, request, user, **kwargs):
    print('=++++++++++++++++++++++++++++++++++++++')
    print('Logged in signals......Run Intro.... ')
    ip = request.META.get('REMOTE_ADDR')
    print('Client IP :', ip)
    print('=++++++++++++++++++++++++++++++++++++++')
    request.session['ip'] =  ip

    """ print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print(f'kwargs:{kwargs}')   """ 
user_logged_in.connect(login_success, sender=User)
