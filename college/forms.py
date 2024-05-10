from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from college.models import CollegeModel


class CollegeRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']

class CollegeSigninform(forms.Form):
    Username=forms.CharField()
    Password=forms.CharField()

class CollegeProfileForm(forms.ModelForm):
    class Meta:
        model = CollegeModel
        fields = '__all__'
        
