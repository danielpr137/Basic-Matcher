from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:job_title>/',views.find_candidate)
]
