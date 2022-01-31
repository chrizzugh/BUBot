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

# print(intents)

words = []
classes = []
documents = []
stemmer = PorterStemmer()
stemming = []
ignore_words = ['?']

pre_processed_data = open("pre_processed_data.txt", "w")
pre_processed_intents = open("pre_processed_intents.txt", "w")
processed_data = open("processed_data.txt", "w")

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
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
#lemmatized intents
words = [lemmatizer.lemmatize(w) for w in words if w not in string.punctuation]
# words = "".join([w.lower() for w in words if w not in string.punctuation])
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

# pre_processed_intents.write(str(classes))
# pre_processed_data.write(str(words))


#!saving and printing preprocessed data in txt file

for element in words:
    # words =  [' '.join(i) for i in words] 
    # words  = " ".join([char for char in words if char not in string.punctuation])
    # words  = "".join([char for char in words])
    # words = "".join([w.lower() for w in words if w not in string.punctuation])
    # words = ' '.join(word[0] for word in words)
    words = ["".join(i) for i in words]
    pre_processed_data.write(str(words))

for element in classes:
    pre_processed_intents.write(str(classes))

for element in documents:
    processed_data.write(str(documents))

pre_processed_intents.close()
pre_processed_data.close()
processed_data.close()

# print(documents)