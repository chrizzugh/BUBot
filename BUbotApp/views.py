from pdb import post_mortem
from urllib import request
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

# from BUbotApp.model.main import decoder
from django.http import JsonResponse
# class chatView(View):

# class chatView(View):
    # def get(self, request):
    #     # chat(request)
    #     # return render(request, "chat.html")
    #     return HttpResponse(request.GET.get("userInput"))
    
def chat(request):
    userInput= {}
    print(request.GET.get("userInput"))
    if request.method == "GET":
        get_get = request.GET.get("userInput")
        data  = {"test": get_get}
        # return render(request.GET.get("userInput"), "chat.html")
        print(get_get)
        return JsonResponse(data)
    # return render(request, "chat.html")

        
            # userQuestion = request.GET.get('userQuestion')
            # query = post_mortem.objects.filter(title__icontains=userQuestion)
                # # print(userQuestion, "userQ")
                # print(self.query)
                # print(userQuestion, "userQuestion")
                # if request.GET.get('chat'):
                #     message = 'You submitted: %r' % request.GET['chat']
                # else:
                #     message = 'You submitted nothing!'
                    
                # print(message)
                # if request.is_ajax():
                #     if request.method == 'POST':
                #         print ('Raw Data: "%s"' % request.body)

                #     decoded= decoder(request)

                # return decoded




