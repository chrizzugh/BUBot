from django.urls import path
from . import views

urlpatterns =[
    path('', views.landing, name="landing"),
    path('chat/', views.chat, name="chat"),
    path('feedback/', views.feedback, name="feedback"),
    path('about/', views.about, name="about"),
    path('report/', views.report, name="report"),
]