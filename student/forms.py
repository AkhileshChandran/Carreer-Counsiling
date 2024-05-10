from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from student.models import StudentModel

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']


class StudentsigninForm(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField()


class Studentprofile(forms.ModelForm):
    class Meta:
        model = StudentModel
        exclude =("user",)
        fields = '__all__'
