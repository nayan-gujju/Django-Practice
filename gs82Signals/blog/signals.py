from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete ,post_init, post_save, post_delete, post_migrate, pre_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("------------------")
    print("Logged-in Signal... Run Intro..")
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print('User Password:', user.password)
    print(f'kwargs{kwargs}') 

#user_logged_in.connect(login_success, sender=User)


def log_out(sender, request, user, **kwargs):
    print("------------------")
    print('Logged Out signal...Run Intro...')
    print('sender:', sender)
    print('Request:', request)
    print('User:', user)
    print('User:', user.password)
    print('kwargs:', kwargs)

user_logged_out.connect(log_out, sender=User)

@receiver(user_login_failed)
def login_failed(sender,credentials, request, **kwargs):
    print("------------------")
    print("Logged-in Failed Signal... Run Intro..")
    print('Sender:', sender)
    print( 'credntials:',credentials )
    print('Request:', request)
    print(f'kwargs{kwargs}') 


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print("------------------.....................")
    print("Pre Save Signal...")
    print('Sender:', sender)
    print( 'instance:',instance)
    print(f'kwargs{kwargs}')
#pre_save.connect(at_beginning_save, sender=User)    


@receiver(post_save, sender=User)
def at_ending_save(sender, instance,created, **kwargs):
    if created:
        print("------------------.....................")
        print("Post Save Signal...")
        print("New Recored Is created...")
        print('Sender:', sender)
        print( 'instance:',instance)
        print('created:',created)
        print(f'kwargs{kwargs}')
    else:
        print("------------------.....................")
        print("Post Save Signal...")
        print("Updated...")
        print('Sender:', sender)
        print( 'instance:',instance)
        print('created:',created)
        print(f'kwargs{kwargs}')
#post_save.connect(at_ending_save, sender=User)    

 
 
@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print("-------------- ----.....................")
    print("At Pre Delete.....")
    print('Sender:', sender)
    print( 'instance:',instance)
    print(f'kwargs{kwargs}')
#pre_delete.connect(at_beginning_delete, sender=User)    


@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print("-------------- ----.....................")
    print("At Post Delete.....")
    print('Sender:', sender)
    print( 'instance:',instance)
    print(f'kwargs{kwargs}')

#post_delete.connect(at_ending_delete, sender=User)  
# 
#   
@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print("-------------- ----.....................")
    print("At Pre Init.....")
    print('Sender:', sender)
    print( f'args{args}')
    print(f'kwargs{kwargs}')
#pre_init.connect(at_beginning_init, sender=User)    


@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print("-------------- ----.....................")
    print("At Post init.....")
    print('Sender:', sender)
    print( f'args{args}')
    print(f'kwargs{kwargs}')

#post_delete.init(at_ending_init, sender=User)    

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print('-=========-=============================')
    print('At Beginning request.....')
    print('Sender:',sender)
    print('Environ:',environ)
    print(f'kwargs{kwargs}')
#request_strated.connect(at_beginning_request)

""" @receiver(request_finished)
def at_ending_request(sender, environ, **kwargs):
    print('-=========-=============================')
    print('At Ending request.....')
    print('Sender:',sender)
    print('Environ:',environ)
    print(f'kwargs{kwargs}') """
#request_finished.connect(at_ending_request)

@receiver(got_request_exception)
def at_request_exception(sender,request, **kwargs):
    print('-=========-=============================')
    print('At request exception .....')
    print('Sender:',sender)
    print('Request:',request)
    print(f'kwargs{kwargs}')
#got_request_exception.connect(at_request_exception)

@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('================+++++++++++====++++++++=====++++++=====++++===')
    print('before install app......')
    print('Sender:', sender)
    print('App config: ',app_config)
    print('Verbosity:', verbosity)
    print('Interactive:', interactive)
    print('Using:', using)
    print('Plan:', plan)
    print('Apps:', apps)
    print(f'kwargs:{kwargs}')
#pre_migrate.connect(before_install_app)
@receiver(post_migrate)
def end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('================+++++++++++====++++++++=====++++++=====++++===')
    print('End migrate flush......')
    print('Sender:', sender)
    print('App config: ',app_config)
    print('Verbosity:', verbosity)
    print('Interactive:', interactive)
    print('Using:', using)
    print('Plan:', plan)
    print('Apps:', apps)
    print(f'kwargs:{kwargs}')
#post_migrate.connect(end_migrate_flush)


@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print('-----------------------------------------')
    print('Initial connection to the database........')
    print('Sender:', sender)
    print('Connection:', connection)
    print(f'kwargs:{kwargs}')
#connection_created.connect(conn_db)