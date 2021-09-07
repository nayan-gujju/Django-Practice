from django.db import models
from django.db.models.fields import proxy

# Create your models here.

class ExamCenter(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)


class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True
        ordering = ['city']