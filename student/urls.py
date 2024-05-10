from django.urls import path
from student.views import StudentRegistrationView,Student_SigninView
from student import views
urlpatterns = [
    path("studentreg/",views.StudentRegistrationView.as_view(),name="studreg"),
    path("studentsignin/",views.Student_SigninView.as_view(),name="studsignin"),
    path("studentsignout/",views.StudentSignout.as_view(),name="studsignout"),
    path('studenthome',views.StudentHome.as_view(),name="sthome"),
    
]