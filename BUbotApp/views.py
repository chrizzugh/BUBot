import json
from ntpath import realpath
import os
from posixpath import dirname
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from importlib_metadata import metadata
import tensorflow as tf
from tensorflow import keras
from .forms import *
# from django.views.decorators.csrf import csrf_protect
# Create your views here.

def landing(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


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



def chat(request):
    if request.method == "POST":
        userQuery = request.POST['userInput']
        # response = {"test": userQuery}
        # print(userQuery)
        # botModel = r"D:/Documents/thesis/BUBot/saved_model.pb"
        # model = tf.keras.models.load_model(botModel)
        # model = os.path.join(dirname(realpath(__file__)), "saved_model.pb")
        # bubotResponse = model(userQuery)
        # print(bubotResponse)
        
        return JsonResponse(userQuery,safe=False)

    return render(request, "chat.html")




