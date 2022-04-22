import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import tensorflow as tf
from tensorflow import keras
from .forms import *

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

from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
tk = WhitespaceTokenizer()
import re
import string


def prep_ques(txt, abbrev):

    #A. converting text to lowercase
    txt = txt.lower()

    #C. noise removing where unnecessary symbols will be removed
    txt = re.sub(r"'ll", " will",txt)
    txt = re.sub(r"'m", " am",txt)
    txt = re.sub(r"'s", " is", txt)
    txt = re.sub(r"\'ve", " have", txt)
    txt = re.sub(r"\'re", " are", txt)
    txt = re.sub(r"\'d", " had", txt)
    txt = re.sub(r"won't", "would not", txt)
    txt = re.sub(r"'t", " not", txt)
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    
    lst = ''
    for token in txt.split():
        try:
            temp = abbrev[token]
        except:
            temp = token
        lst = lst + ' ' +temp
    txt = lst
    
    #B. undergoing tokenization or splitting the sentences into words
    txt = tk.tokenize(txt)
    
    #D. removing of stop words
    txt = [word for word in txt if not word in stopwords.words()]
    
    #F. lemmatization 
    lemmatizer = WordNetLemmatizer()
    txt = [lemmatizer.lemmatize(token, pos="v") for token in txt]

    return ' '.join(txt)

#--------code for the website starts here------------
import nltk 
# nltk.download('stopwords') #for first run
# nltk.download('punkt') #for first run
# nltk.download('wordnet') #for first run
# nltk.download('omw-1.4') #for first run

import tensorflow as tf
import logging
import tensorflow_text  
logging.getLogger('tensorflow').setLevel(logging.ERROR) 

import json
with open('D:/Documents/thesis/BUBot/BUbotApp/models/abbrev.json', 'r', encoding="utf8") as abbreviations:
    abbrev = json.loads(abbreviations.read())

Bubot = tf.saved_model.load('D:/Documents/thesis/BUBot/BUbotApp/models/VanilaBUbot')


# from langdetect import detect
import langid
#! chat
def chat(request): 
    if request.method == "POST":
        userQuery = request.POST ['userInput']
        lang = langid.classify(userQuery)[0]
        # lang = detect(userQuery)
        print(lang)
        if lang != "en":
            bubotResponse = "I apologize but I can only answer question in English language. Can you retype your question in that language?"
        else:
            userQuery = prep_ques(userQuery, abbrev)
            predicted = Bubot(userQuery).numpy()
            bubotResponse = predicted.decode()
        return JsonResponse(bubotResponse, safe=False)
    
    return render(request, "chat.html")
