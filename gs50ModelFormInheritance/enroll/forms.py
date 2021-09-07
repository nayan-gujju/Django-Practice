from django import forms
from enroll.models import User
class Student(forms.ModelForm):
    class Meta:
        model = User
        fields = ('student_name', 'email', 'password')

class Teacher(Student):
    class Meta(Student.Meta):
        fields = ('teacher_name','email', 'password' )