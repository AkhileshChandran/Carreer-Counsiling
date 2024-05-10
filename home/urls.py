from django.urls import path
from home.views import AdminRegistrationView,AdminSigninView,AdminSignout,add_college,add_question,submit_answer,conduct_test,show_recommendations

urlpatterns = [

   path("adminreg/",AdminRegistrationView.as_view(),name="adminreg"),
   path("adminsignin/",AdminSigninView.as_view(),name="adminsignin"),
   path("adminsignout/",AdminSignout.as_view(),name="adminsignout"),
   path('test/', conduct_test, name='test'),
   path('submit_answer/', submit_answer, name='submit_answer'),
   path('recommendations/', show_recommendations, name='recommendations'),
   path('add_question/', add_question, name='add_question'),
   path('add_college/', add_college, name='add_college'),
    
]
