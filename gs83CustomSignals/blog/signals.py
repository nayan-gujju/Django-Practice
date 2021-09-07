from django.dispatch import Signal, receiver

#creating signals


notification = Signal(providing_args=['request', 'user'])

#reciver function

@receiver(notification)
def show_notification(sender, **kwargs):
    print(sender)
    print(f'kwargs{kwargs}')
    print('Notification') 
