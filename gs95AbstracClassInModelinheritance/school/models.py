from django.db import models

# Create your models here.

class CommanInformation(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Student(CommanInformation):
    fees = models.IntegerField()
    date = None

class Teacher(CommanInformation):
    salary = models.IntegerField()

class Construction(CommanInformation):
    date = models.DateTimeField()
    payment = models.IntegerField()