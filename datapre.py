import json
from nltk import stem
import numpy as np
import random
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

intents = json.loads(open('D:\Documents\BUBot\intents.json', encoding="utf-8").read())

words = []
classes = []
documents = []
stop_words = stopwords.words('english')
stemmer = PorterStemmer()
stemming = []

#f = open("D:\Documents\BUBot\original.txt", "w")
#f1 = open("D:\Documents\BUBot\lowered.txt", "w")
#f2 = open("D:\Documents\BUBot\punctuation.txt", "w")
#f3 = open("D:\Documents\BUBot\itokenized.txt", "w")
#f4 = open(D:\Documents\BUBot\stopwords_removed.txt", "w")
#f5 = open(D:\Documents\BUBot\processed.txt", "w")

for intent in intents['intents']:
    for pattern in intent['patterns']:
        #f.write(pattern + "\n")
        # Preprocessing Step 1 - Conversion to lowercase
        lowercase = pattern.lower()
        #f1.write(lowercase)

        # Preprocessing Step 2 - Removing Punctuation
        punc_remove = "".join([char for char in lowercase if char not in string.punctuation])
        #f2.write(punc_remove)

        # Preprocessing Step 3 - Tokenization
        word_list = word_tokenize(punc_remove)
        words.append(word_list)

        # Preprocessing Step 4 - Removing Stop Words
        stop_words = stopwords.words('english')
        stopw_remove = [word for word in words if word not in stop_words]

        #stemmed = [stemmer.stem(word) for word in stopw_remove]
        #stemming.append(stemmed)

        documents.append((stopw_remove, intent['tag']))

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#f.close()
#f1.close()
#f2.close()
#for element in word_list:
#    f3.write(str(word_list))

#for element in word_list:
#    f4.write(str(stopw_remove))

#for element in documents:
#    f5.write(str(documents))

#f3.close()
#f4.close()
#f5.close()

#print(documents)