from django.shortcuts import render,redirect
from college.models import CollegeModel
from django.views.generic import View
from college.forms import CollegeSigninform,CollegeRegistrationForm,CollegeProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
class CollegeRegistrationView(View):
    def get(self,request,*args,**kwargs):
        form = CollegeRegistrationForm()
        return render(request,"collage/collegereg.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = CollegeRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            form.save()
            print(form.cleaned_data)

        else:
            print("Error found,Please check it.....")
        form = CollegeRegistrationForm()
        return render(request,"collage/collegereg.html",{"form":form})
    

class CollegeSigninView(View):
    def get(self,request,*args,**kwargs):
        form = CollegeSigninform()
        return render(request,"collage/collegesignin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = CollegeSigninform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user_name=form.cleaned_data.get("Username")
            pass_word=form.cleaned_data.get("Password")
            User_obj=authenticate(request,username=user_name,password=pass_word)
            if User_obj:
                print(User_obj)
                print("Valid Credential")
                login(request,User_obj)
                return redirect("c_reg")
            else:
                print("Invalid Credential")
        else:
            print("Error found..Please checkout it...")
        return render(request,"collage/collegesignin.html",{"form":form})
    
class CollegeSignout(View):
    def get(self,request):
        logout(request)
        return redirect("c_signin")
    
