from django.urls import path
from .views import *
urlpatterns=[
    path('',Login.as_view(),name='login'),
    path('appoint/',Appointments.as_view(),name='appoint'),
    path('report/',Reports.as_view(),name='report'),

]