import nltk
from nltk.stem.lancaster import  LancasterStemmer
stemmer = LancasterStemmer()
import numpy as np
import tensorflow as tf
import tflearn
import random
import json
import pandas as pd
import pickle
import langdetect as ld


#opening dataset
intents = pd.read_json('intents.json')
intents.head()

#tokenizing
words = []
classes = []
documents = []
ignore = ['?']
#loop through each sentence in the intent's patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

#stemming
words = [stemmer.stem(w.lower()) for w in words if w not in ignore]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print(len(documents),"documents")
print(len(classes), "classes", classes)
print(len(words), "unique stemmed words", words)


# #language detection
# words = ld.detect_langs(words)


# #creating training data
# training = []
# output = []
# output_empty = [0] * len(classes)

# for doc in documents: 
#     bag = []
#     pattern_words = doc[0]
#     pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
#     for w in words:
#         bag.append(1) if w in pattern_words else bag.append(0)

#     output_row = list(output_empty)
#     output_row[classes.index(doc[1])] = 1
#     training.append([bag,output_row])

# random.shuffle(training)
# training = np.array(training)

# train_x = list(training[:,0])
# train_y = list(training[:,1])

# #creating model and training
# tf.compat.v1.reset_default_graph()
# net = tflearn.input_data(shape=[None, len(train_x[0])])
# net = tflearn.fully_connected(net, 10)
# net = tflearn.fully_connected(net, 10)
# net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
# net = tflearn.regression(net)
# model = tflearn.lstm(net, tensorboard_dir='tflearn_logs') #change to lstm
# model.fit(train_x, train_y, n_epoch = 1000, batch_size=8, show_metric=True)

# model.save('model.tflearn')
# pickle.dump({'words' : words, 'classes':classes, 'train_x': train_x, 'train_y' : train_y}, open("training_data", "wb"))