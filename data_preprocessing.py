import json
import numpy as np
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import langdetect as ld


intents= open("intents.json", encoding="utf-8").read()
intents = json.loads(intents)

words = []
classes = []
documents = []
stemmer = PorterStemmer()
stemming = []
ignore_words = ['?']


#!intents tokenizing
for intent in intents['intents']:
    for pattern in intent['patterns']:
        #tokenize each word
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        #add documents in the corpus
        documents.append((w, intent['tag']))
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#!printing tokenized intents
# print(words)
# print(classes)
# print(documents)


#!lemma, lower case and removing of punctuations the intents
#stemmed intents
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words or w not in string.punctuation]
#lemmatized intents
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
# sort classes
classes = sorted(list(set(classes)))

#!printing lemma and lower cased intents
# documents = combination between patterns and intents
print(len(documents), "documents")
# classes = intents
print(len(classes), "classes", classes)
# words = all words, vocabulary
print(len(words), "unique lemmatized words", words)
# pickle.dump(words,open('words.pkl','wb'))
# pickle.dump(classes,open('classes.pkl','wb'))
