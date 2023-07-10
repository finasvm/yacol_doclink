from django.urls import path
from .views import *
urlpatterns=[
    path('userregister/',UserRegister.as_view()),
    path('docregister/',DocRegister.as_view())

]