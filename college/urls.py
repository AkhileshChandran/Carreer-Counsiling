from django.urls import path
from college.views import CollegeRegistrationView,CollegeSigninView,CollegeSignout

urlpatterns = [
    path("collegereg/",CollegeRegistrationView.as_view(),name="c_reg"),
    path("collegesignin/",CollegeSigninView.as_view(),name="c_signin"),
    path("collegesignout/",CollegeSignout.as_view(),name="c_signout"),
]