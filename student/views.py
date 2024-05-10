from django.shortcuts import render,redirect
from django.views.generic import View
from student.models import StudentModel
from student.forms import StudentsigninForm,Studentprofile,StudentRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class StudentRegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = StudentRegistrationForm()
        return render(request, "Studentreg.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can perform additional actions after user creation if needed
            print("User created successfully:", user.username)
            return redirect("success_url_name")  # Redirect to a success page or any other URL
        else:
            print("Error found, Please check it.....")
            # If there are errors, render the form again with error messages
            return render(request, "Studentreg.html", {"form": form})

@login_required
def your_view(request):
    username = request.user.username
    return render(request, 'studenthome.html', {'username': username})

class Student_SigninView(View):
    def get(self,request,*args,**kwargs):
        form = StudentsigninForm()
        return render(request,"StudentSignin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = StudentsigninForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_name=form.cleaned_data.get("Username")
            pass_word=form.cleaned_data.get("Password")
            User_obj=authenticate(request,username=user_name,password=pass_word)
            if User_obj:
                print(User_obj)
                print("Valid Credential")
                login(request,User_obj)
                return redirect("sthome")
            else:
                print("Invalid Credential")
        else:
            print("Error found..Please checkout it...")
        return render(request,"StudentSignin.html",{"form":form})
    

class StudentSignout(View):
    def get(self,request):
        logout(request)
        return redirect("studsignin")


class StudentHome(View):
    def get(self,request):
        return render(request,"studenthome.html")
