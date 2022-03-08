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


import pickle
import time
class getQuery(View):
    # def get(self, request, userQuestion, *args, **kwargs):
    #     userQuestion = request.GET('userQuestion')
    #     if userQuestion != None:
    #         print(userQuestion)
    #     print("EMPTY")
        
    #     return userQuestion
    
    def post(self, request, *args, **kwargs):
        if request.method == 'GET':
            current_time = time.strftime("%I:%M %p")
            bubbleDiv = request.POST['userQuestion']
            context = {
                "current_time": current_time,
                "bubbleDiv": bubbleDiv
            }
            if bubbleDiv.is_valid():
                print(bubbleDiv)
                # context.save()
                return render(request, 'chat. html', context)
            
        return render(request, 'chat.html')

# def post(self, request, *args, **kwargs):
#     userInput = request.POST.get['userQuestion']
#     print(userInput)
#     return render(request, 'chat.html')

    

def displayResponse(request, bubotReply):
    model = pickle.load(open("saved_model.pb", "rb"))
    metadata = pickle.load(open("keras_metadata1.pb", "rb"))
