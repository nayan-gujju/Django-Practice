from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Page(models.Model):
    """ user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    when we use CASECADE then we delete the user automatically delele the page """
    """ user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    when we use PROTECT the we delete the user but not delete the user,its protect the user because he made the page """ 
    """ user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, limit_choices_to={'is_staff':True})
    if staff is qual to true then only staff user can create the page other user not create the page  """
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, limit_choices_to={'is_staff':True})
    page_name = models.CharField(max_length=50)
    page_cat =  models.CharField(max_length=50)
    page_publish_date = models.DateField()