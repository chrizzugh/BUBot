from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')

def feedback(request):
    return render(request, 'feedback.html')

def about(request):
    return render(request, 'about.html')

def report(request):
    return render(request, 'report.html')
