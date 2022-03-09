from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from importlib_metadata import metadata
# Create your views here.

def landing(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')

def about(request):
    return render(request, 'about.html')


# feedback save in database
from .forms import *

class reportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "report.html")
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SaveReportForm(request.POST, request.FILES)
            if form.is_valid():
                form.save() 
                # print(request.POST)
                return redirect('/')
            
        return render(request, "report.html")

class feedbackView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "feedback.html")
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            feedback = SaveFeedbackForm(request.POST)
            if feedback.is_valid():
                feedback.save() 
                # print(request.POST) 
                return redirect('/')
        return render(request, "feedback.html")

def get_queryset(self):
    userQuestion = self.request.GET.get('userInput', None)
    self.queryset = Post.objects.filter(title__icontains=userQuestion)
    return self.queryset

import pickle
def displayResponse(request, bubotReply):
    model = pickle.load(open("saved_model.pb", "rb"))
    metadata = pickle.load(open("keras_metadata1.pb", "rb"))
