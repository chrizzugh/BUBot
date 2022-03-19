from django.urls import path
from . import views

urlpatterns =[
    path('', views.landing, name="index"),
    path('chat/', views.chat, name="chat"),
    path('feedback/', views.feedbackView.as_view(), name="feedback"),
    path('about/', views.about, name="about"),
    path('report/', views.reportView.as_view(), name="report"),
]