from django import forms
from django.contrib.auth.models import User
from home.models import College,Question


class AdminRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class AdminSigninForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField()


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'correct_answer']

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['name', 'location', 'required_score'] 