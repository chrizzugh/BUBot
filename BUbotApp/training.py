import nltk
nltk.download('stopwords') #for first run
nltk.download('punkt') #for first run
nltk.download('wordnet') #for first run
nltk.download('omw-1.4') #for first run

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
 
def prep_ques(txt, abbrev):
    
    #A. converting text to lowercase
    txt = txt.lower()
  
    #C. noise removing where unnecessary symbols will be removed
    import re

    txt = re.sub(r"'ll", " will",txt)
    txt = re.sub(r"'m", " am",txt)
    txt = re.sub(r"'s", " is", txt)
    txt = re.sub(r"\'ve", " have", txt)
    txt = re.sub(r"\'re", " are", txt)
    txt = re.sub(r"\'d", " had", txt)
    txt = re.sub(r"won't", "would not", txt)
    txt = re.sub(r"'t", " not", txt)
    txt = re.sub(r"[^\w\s]", "", txt)
    
    #B. undergoing tokenization or splitting the sentences into words
    
    lst = ''
    for token in txt.split():
        try:
            temp = abbrev[token]
        except:
            temp = token
        lst = lst + ' ' +temp
    txt = lst
    txt = word_tokenize(txt)
    
    #D. removing of stop words
    #nltk.download('stopwords') #for first run
    #nltk.download('punkt') #for first run
    txt = [word for word in txt if not word in stopwords.words()]
  
    #E. stemming or getting the root words
    #removes necessary character, might affect predictions
    
    #F. lemmatization 
    lemmatizer = WordNetLemmatizer()
    #nltk.download('wordnet') #for first run
    #nltk.download('omw-1.4') #for first run
    txt = [lemmatizer.lemmatize(token, pos="v") for token in txt]
   
    return txt

import json
MAX_INPUT_LEN = 69
with open(r"D:/Documents/thesis/BUBot/BUbotApp/training files/input/abbrev.json", 'r') as abbreviations:
    abbrev = json.load(abbreviations)

with open(r'D:/Documents/thesis/BUBot/BUbotApp/training files/output/vocab.json', 'r') as vocabulary:
    vocab = json.load(vocabulary)

del(abbreviations, vocabulary)

inv_vocab = {w:v for v, w in vocab.items()}  

#! TRAINING

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Embedding, LSTM, Input, Bidirectional, Concatenate, Dropout, Attention

import numpy as np
with open(r'D:/Documents/thesis/BUBot/BUbotApp/training files/output/embedded.txt', 'r', encoding="utf8") as emb:
    f = emb.read().split('\n')

embedded_index = {}
for i in range(1, len(f)-1):
  values = f[i].split()
  word = values[0]
  coefs = np.asarray(values[1:])  
  embedded_index[word] = coefs
  if f[i] == '':
    break

len(embedded_index)
VOCAB_SIZE = len(vocab) 

import numpy as np
embedding_matrix = np.zeros((VOCAB_SIZE, 100))

for i in inv_vocab:
    vector = embedded_index.get(inv_vocab[i])
    if vector is not None:
        embedding_matrix[i] = vector

len(embedded_index)

"""
    11. SETUP MODEL AND TRAINING 
    """
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Embedding, LSTM, Input
from keras.initializers import Constant


# EMBEDDING LAYER
embed = Embedding(VOCAB_SIZE, 
                  output_dim=100,
                  input_length=MAX_INPUT_LEN,
                  trainable=False)


# ENCODER LAYER
encoder = Input(shape=(MAX_INPUT_LEN, ))
encoder_embed = embed(encoder)
encoder_lstm = LSTM(400, return_sequences=True, return_state=True)
encoder_output, h, c = encoder_lstm(encoder_embed)
encoder_states = [h, c]


# DECODER LAYER
decoder = Input(shape=(MAX_INPUT_LEN, ))
decoder_embed = embed(decoder)
decoder_lstm = LSTM(400, return_sequences=True, return_state=True)
decoder_output, _, _ = decoder_lstm(decoder_embed, initial_state=encoder_states)


# DENSE LAYER
dense = Dense(len(vocab), activation='softmax')
dense_output = dense(decoder_output)


# MODEL
model = Model([encoder, decoder], dense_output)

import tensorflow as tf
savedmodel = tf.keras.models.load_model(r'D:/Documents/thesis/BUBot/BUbotApp/training files/VanilaBUbot')

model.set_weights(savedmodel.get_weights())

tf.keras.utils.plot_model(model, to_file='D:Documents/thesis/BUBot/BUbotApp/training files/Photos/version1.png',show_layer_names=True, show_shapes=True)

"""
    12. INFERENCE MODEL
"""
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input


#ENCODER MODEL
encoder_model = Model([encoder], encoder_states)


#DECODER MODEL
decoder_state_input_h = Input(shape=(400,))
decoder_state_input_c = Input(shape=(400,))

decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]


decoder_outputs, state_h, state_c = decoder_lstm(decoder_embed , 
                                    initial_state=decoder_states_inputs)


decoder_states = [state_h, state_c]


decoder_model = Model([decoder]+ decoder_states_inputs,
                                      [decoder_outputs]+ decoder_states)

"""
    13. TESTING THE MODEL
"""
import numpy as np
from keras.preprocessing.sequence import pad_sequences 


print("TESTING BUBOT.... \nPlease type your question....\nType 'EXIT' to quit program.") 
print("------------------------------------------------------------")

USER_INPUT = ""
while USER_INPUT != 'EXIT': 

    """
        Get the user input, perform preprocessing
        and necessary operations to transform output into machine-readable input
    """

    USER_INPUT = input("USER : ")
    if USER_INPUT =='EXIT':
      break
    USER_INPUT = prep_ques(USER_INPUT, abbrev)

    user = []
    for token in USER_INPUT: 
        try:
            user.append(vocab[token])
        except:
            user.append(vocab['UNK'])
    user = [user]    
    
    user = pad_sequences(user, MAX_INPUT_LEN, padding='post')
    
    stat = encoder_model.predict( user )
    
    empty_target_seq = np.zeros( ( 1 , 1) ) 
    
    empty_target_seq[0, 0] = vocab['SOS']
    
    decoded_translation = ''
    
    while True :
    
        dec_outputs , h, c= decoder_model.predict([ empty_target_seq] + stat )
        decoder_concat_input = dense(dec_outputs)

    
        sampled_word_index = np.argmax( decoder_concat_input[0, -1, :] )
        
    
        sampled_word = inv_vocab[sampled_word_index] + ' '
    
    
        if sampled_word != 'EOS ':
            decoded_translation += sampled_word  
    
        if sampled_word == 'EOS ' or len(decoded_translation.split()) > MAX_INPUT_LEN:
            break
    
        empty_target_seq = np.zeros( ( 1 , 1 ) )  
        empty_target_seq[ 0 , 0 ] = sampled_word_index

        stat = [h, c]  
    
    print("BUBOT : ", decoded_translation )
    print("============================================================") 
    