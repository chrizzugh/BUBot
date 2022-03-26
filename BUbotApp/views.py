import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import tensorflow as tf
from tensorflow import keras
from .forms import *
# import preprocessing
from . import preprocessing
# from . import main


#!rendering landing and about
def landing(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


#!Report and feedback class-based view 
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

#! chat
def chat(request): 
    userQuery = []
    # userQuery = json.loads(request.body) 
    if request.method == "POST":
        userQuery = request.POST['userInput']
        
        # load vocab
        # json_file_path = "D:/Documents/thesis/BUBot/BUbotApp/training files/output/vocab.json"
        # with open(json_file_path, 'r') as j:
        #     vocab = json.loads(j.read())
            
        with open('D:/Documents/thesis/BUBot/BUbotApp/models/vocab.json', 'r') as vocabulary:
            vocab = json.load(vocabulary)

        with open('D:/Documents/thesis/BUBot/BUbotApp/models/abbrev.json', 'r', encoding="utf8") as abbreviations:
            abbrev = json.loads(abbreviations.read())
        
        
        
        
        # userQuery = preprocessing.prep_ques(userQuery)
        userQuery = preprocessing.prep_ques(userQuery)
        user = []
        for token in userQuery: 
            try:
                user.append(vocab[token])
            except:
                user.append(vocab['OUT'])
        user = [user]   
        print(userQuery)
        print(user)
        
        model_path = r"D:/Documents/thesis/BUBot/BUbotApp/models/VanilaBUbot"
        model = tf.keras.models.load_model(model_path)
        # model.summary()
        
        # target_response = np.zeros((1,1)) 
        
        # target_response[0, 0] = vocab['SOS']
        
        # inverse_vocab = {index:word for word, index in vocab.items()}
        
        # bubotResponse = ''
        
        # bubotResponse = model.predict(user, batch_size=None, verbose=0, steps=None, callbacks=None)
        # print(bubotResponse)
        
        
        return JsonResponse(userQuery, safe=False)
    
    return render(request, "chat.html")




