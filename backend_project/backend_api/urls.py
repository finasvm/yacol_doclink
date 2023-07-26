from django.urls import path
from . import views
from .views import *
urlpatterns=[
    path('Signup/',views.Signup),
    path('Login/',views.Login),
    path('appointments/',views.Appointments),
    path('all_appointments/',views.all_appointments),
    path('docregister/',DocRegister.as_view()),
    path('results/',views.All_Result),
    path('docdays/',views.Doc_Dates)

]