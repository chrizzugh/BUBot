import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View
import tensorflow as tf
from tensorflow import keras
from BUbotApp.forms import qaform
from django.contrib import messages
import re

#!rendering landing, about, and categories
def landing(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def categories(request):
    return render(request, 'categories.html')

def login(request):
    return render(request, 'login.html')

def admin(request):
    return render(request, 'admin.html')

from BUbotApp.models import parallel_corpus
def admin(request):
    data =  parallel_corpus.objects.all()
    qa = {
        "qa_num": data
    }
    return render(request, "admin.html", qa)

def edit(request, id):
    disp = parallel_corpus.objects.get(id=id)
    return render(request, "update.html", {"parallel_corpus": disp} )


def update(request, id):
    update = parallel_corpus.objects.get(id=id)
    form = qaform(request.POST, instance=update)


    if form.is_valid:
        form.save()
        data = parallel_corpus.objects.all()
        qa = {
            "qa_num": data
        }
        return render(request, "admin.html", qa)
class reportView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "report.html")

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = SaveReportForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                
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
                return redirect('/')
        return render(request, "feedback.html")

from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
tk = WhitespaceTokenizer()
import re
import string

def remove_noise(txt, vocab):
    lst = []
    for item in txt.split():
        if item in vocab:
            lst.append(item)
        else:
            pass

    return ' '.join(lst)

def prep_ques(txt, abbrev):
    txt = txt.lower()
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
    txt = tk.tokenize(txt)
    txt = [word for word in txt if not word in stopwords.words()]
    lemmatizer = WordNetLemmatizer()
    txt = [lemmatizer.lemmatize(token, pos="v") for token in txt]
    return ' '.join(txt)

def connects(txt):
    txt = txt.replace('[unk]','')
    return txt
from collections import Counter
import math

def length_similarity(l1, l2):
    lenc1 = 4
    lenc2 = 6
    return min(lenc1, lenc2) / float(max(lenc1, lenc2))

def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)

def similarity_score(l1, l2):
    c1, c2 = Counter(l1), Counter(l2)
    return length_similarity(len(l1), len(l2)) * counter_cosine_similarity(c1, c2)


import tensorflow as tf
import logging
import tensorflow_text
logging.getLogger('tensorflow').setLevel(logging.ERROR)

#------load necessary files------------------------------
import json
with open('BUbotApp/assets/abbrev.json', 'r', encoding="utf8") as abbreviations:
    abbrev = json.loads(abbreviations.read())

#Bubot vocab
with open("BUbotApp/assets/vocab.json", "r") as vocab_file:
    vocab = json.loads(vocab_file.read())

Bubot = tf.saved_model.load('BUbotApp/assets/Bubot')

with open('BUbotApp/assets/PAPER ESSENTIALS/preprocessed_questions.txt', 'r') as ques:
    questions = ques.read().split('\n')

#Bubot one_tokens
with open("BUbotApp/assets/s_vocab.json", "r") as vocab_file:
    one = json.loads(vocab_file.read())

single_tokens_dict = {}

for key in one.keys():
    single_tokens_dict [key] = ''.join((one[key]).split())

#! chat
def chat(request):
    if request.method == "POST":
        query = request.POST ['userInput']
        bubotResponse = ''
        flag = 0
        temp = query.lower()
        temp = temp.translate(str.maketrans('', '', string.punctuation))

        if ''.join(temp.split()) in single_tokens_dict.values():
            predicted = Bubot(query).numpy()
            bubotResponse = predicted.decode()
            flag = 1

        else:
            
            query = prep_ques(query, abbrev)
            query = remove_noise(query, vocab)

            if len(query.split()) == 0:
                bubotResponse = 'Sorry, but can you retype your question because I cannot understand you? Thank you.'

            elif len(query.split()) > 0:
                
                score = 0
            
                for line in questions:
                    temp2 = line.split()
                    similarity = similarity_score(query.split(), temp2)
                    if(similarity > score):
                        score = similarity
                    
                if score > 0.41:
                    predicted = Bubot(query).numpy()
                    bubotResponse = predicted.decode()
                    flag = 1
                else:
                    bubotResponse = 'Sorry, can\'t understand you.'

        if flag == 1:
            bubotResponse = ''.join(bubotResponse.split(' '))
            bubotResponse = ' '.join(bubotResponse.split('+'))      

        data =  parallel_corpus.objects.all()
        
        for d in data:
            a = d.answer
            a = ''.join(a.split())
            a = a.replace('ñ', 'n')
            a = a.translate(str.maketrans('', '', string.punctuation))
            b = bubotResponse
            b = ''.join(b.split())
            b = b.translate(str.maketrans('', '', string.punctuation))

            if a == b:
                bubotResponse = d.final_answer
                break   

        return JsonResponse(bubotResponse, safe=False)
    return render(request, "chat.html")