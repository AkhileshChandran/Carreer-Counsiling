from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from home.forms import AdminRegistrationForm,AdminSigninForm,CollegeForm,QuestionForm
from home.models import College,Question


# Create your views here.;
class AdminRegistrationView(View):
    def get(self,request,*args,**kwargs):
        form = AdminRegistrationForm()
        return render(request,"home/adminreg.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = AdminRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            form.save()
            print(form.cleaned_data)

        else:
            print("Error found,Please check it.....")
        form = AdminRegistrationForm()
        return render(request,"home/adminreg.html",{"form":form})
    

class AdminSigninView(View):
    def get(self,request,*args,**kwargs):
        form = AdminSigninForm()
        return render(request,"home/adminsignin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = AdminSigninForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_name=form.cleaned_data.get("Username")
            pass_word=form.cleaned_data.get("Password")
            User_obj=authenticate(request,username=user_name,password=pass_word)
            if User_obj:
                print(User_obj)
                print("Valid Credential")
                login(request,User_obj)
                return redirect("adminreg")
            else:
                print("Invalid Credential")
        else:
            print("Error found..Please checkout it...")
        return render(request,"home/adminsignin.html",{"form":form})
    
class AdminSignout(View):
    def get(self,request):
        logout(request)
        return redirect("adminsignin")
    

    
def conduct_test(request):
    questions = Question.objects.all()
    return render(request, 'home/test.html', {'questions': questions})

def submit_answer(request):
    if request.method == 'POST':
        user_answers = {}
        correct_answers = {}
        for key, value in request.POST.items():
            if key.startswith('question_'):
                user_answers[key] = value
                question_id = int(key.split('_')[1])
                correct_answers[question_id] = Question.objects.get(pk=question_id).correct_answer
        score = calculate_score(user_answers, correct_answers)
        return render(request, 'home/result.html', {'score': score})

def calculate_score(user_answers, correct_answers):
    score = 0
    for question_id, correct_answer in correct_answers.items():
        user_answer = user_answers.get(f'question_{question_id}_answer')
        if user_answer and user_answer.strip().lower() == correct_answer.lower():
            score += 1
    return score

# Other views remain unchanged


def show_recommendations(request):
    colleges = College.objects.filter(required_score__lte=calculate_score)
    return render(request, 'home/recommendations.html', {'colleges': colleges})

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_question')
    else:
        form = QuestionForm()
    return render(request, 'home/add_question.html', {'form': form})

def add_college(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_college')
    else:
        form = CollegeForm()
    return render(request, 'home/add_college.html', {'form': form})






