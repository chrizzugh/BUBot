from django.urls import path
from . import views

urlpatterns =[
    path('', views.landing, name="index"),
    path('chat/', views.chat, name="chat"),
    path('feedback/', views.feedbackView.as_view(), name="feedback"),
    path('about/', views.about, name="about"),
    path('report/', views.reportView.as_view(), name="report"),
    path('categories/', views.categories, name="categories"),
    path('login/', views.login, name="login"),
    path('admin/', views.admin, name="admin"),
    path('edit/<int:id>', views.edit, name = 'edit'),
	path('update/<int:id>', views.update, name = 'edit')
]