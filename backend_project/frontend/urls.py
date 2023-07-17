from django.urls import path
from .views import *
urlpatterns=[
    path('',Login.as_view(),name='login'),
    path('appoint/',Appointments.as_view(),name='appoint'),
    path('orderchange/',OrderChange.as_view(),name='orderchange'),
    path('results/',All_Results.as_view(),name='results'),
    path('sendresult/',SendResult.as_view(),name='sendres'),
    path('report/',Reports.as_view(),name='report'),

]