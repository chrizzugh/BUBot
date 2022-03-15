from BUbotApp.model.main import *
from BUbotApp.model.attention import *
import json
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Embedding, LSTM, Input, Bidirectional, Concatenate, Dropout, Attention
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import ModelCheckpoint
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences


#PARAMETERS
DICTIONARY_SIZE = 0
MAX_INPUT_LEN = 0

if __name__ == "__main__":
    
    """  
        1. access and open the json file
        """
    with open('final_intents.json', 'r', encoding="utf8") as access_to_json:
        json_data = json.loads(access_to_json.read())
    
    """  
        2. acess json_data
        """
    data = json_data['intents']
    
    """
        3. separate the answers and questions in two different lists
        """
    questions = []
    answers = []
    for d in data:
        if len(d['patterns']) > 1:
            for pattern in d['patterns']:
                lst = []
                lst.append(pattern)
                questions.append(lst)
                answers.append(d['responses'])
        else:
            questions.append(d['patterns'])
            answers.append(d['responses'])
    
    #delete unnecessesary variables    
    del(access_to_json, d, data, json_data, lst, pattern)          
    
    """
        4.perform preprocessing on dataset
        """
        
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer
     
    def prep_ques(txt):
        
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
        txt = word_tokenize(txt)
        
        #D. removing of stop words
        txt = [word for word in txt if not word in stopwords.words()]
      
        #E. stemming or getting the root words
        #removes necessary character, might affect predictions
        
        #F. lemmatization 
        lemmatizer = WordNetLemmatizer()
        txt = [lemmatizer.lemmatize(token, pos="v") for token in txt]
       
        return txt

    def prep_ans(txt):
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
        #txt = re.sub(r"[^\w\s]", "", txt)
        #B. undergoing tokenization or splitting the sentences into words
        txt = 'SOS ' + txt + ' EOS'
        #txt = word_tokenize(txt)
        txt = txt.split()
      
        return txt
    
    
    final_questions = []
    final_answers = []
    
    for line in questions:
        text = (prep_ques(line[0]))
        final_questions.append(text)
    
    
    for line in answers:
        text = (prep_ans(line[0]))
        final_answers.append(text)
    
    #delete unnecessesary variables
    del(answers, questions, line, text)
    
    
    """
        5. Create vocabulary and inverse dictionary
    """
    def create_vocab(ques, ans):
        vocab = {}
        word_num = 0
        for line in ques:
            for word in line:
                if word not in vocab:
                    vocab[word] = word_num
                    word_num += 1
                    
        for line in ans:
            for word in line:
                if word not in vocab:
                    vocab[word] = word_num
                    word_num += 1
                    
        return vocab


    vocab = create_vocab(final_questions, final_answers)
    
    #adding additional and necessary tokens
    tokens = ['PAD', 'UNK']
    #UNK stands for UNKNOWN words, meaning words that are not learned by the model
    
    x = len(vocab)
    for token in tokens:
        vocab[token] = x
        x += 1
    
    DICTIONARY_SIZE = len(vocab)   
    #delete unnecessesary variables
    del(token, tokens, x)
    
    #inverse answers dict
    inverse_vocab = {index:word for word, index in vocab.items()}
    
    
    """
        6. Find the maximum length of the strings in answers and questions
    """
    if len(max(final_answers, key=len)) >= len(max(final_questions, key=len)):   
        MAX_INPUT_LEN = len(max(final_answers, key=len))
    else:
        MAX_INPUT_LEN = len(max(final_questions, key=len))
            
    print(MAX_INPUT_LEN)
    
    
    """
       7. Create encoder and decoder inputs and decoder outputs 
    """

    from tensorflow.keras.utils import to_categorical

    encoder_inputs = []
    for line in final_questions:
        lst = []
        for word in line:
                lst.append(vocab[word])
        encoder_inputs.append(lst)
    
    decoder_inputs = []
    for line in final_answers:
        lst = []
        for word in line:
                lst.append(vocab[word])        
        decoder_inputs.append(lst)
    
    
    encoder_inputs = pad_sequences(encoder_inputs, MAX_INPUT_LEN, padding='post')
    decoder_inputs = pad_sequences(decoder_inputs, MAX_INPUT_LEN, padding='post')
    
    decoder_final_outputs = []
    for i in decoder_inputs:
        decoder_final_outputs.append(i[1:]) 
    
    decoder_final_outputs = pad_sequences(decoder_final_outputs, 69, padding='post', truncating='post')
    

    decoder_final_outputs = to_categorical(decoder_final_outputs, len(vocab))
    
    #delete unnecessesary variables
    del(line, lst, word, i)
    
    """
        8. Using Word2vec to create embedding weights for answers and questions dataset,
        create embedding matrix
    """
    from gensim.models import Word2Vec

    
    def embed(questions, answers):
     
        inp = questions + answers
        filename = "embedded.txt"
        dec = Word2Vec(inp, window=5, min_count=1, workers=4)
        dec.wv.save_word2vec_format(filename, binary = False)
    
    embed(final_questions, final_answers)
    
    
    embedded_index = {}

    with open('embedded.txt', 'r', encoding="utf8") as emb:
        f = emb.read().split('\n')
    
    for i in range(1, len(f)-1):
        values = f[i].split()
        word = values[0]
        coefs = np.asarray(values[1:])
        
        embedded_index[word] = coefs
    
    #delete unnecessesary variables
    del(i, f, values, word, coefs, emb) 
        
    
    embedding_matrix = np.zeros((len(vocab), 100))
    
    for i in inverse_vocab:
        vector = embedded_index.get(inverse_vocab[i])
        if vector is not None:
            embedding_matrix[i] = vector

    """
        Saving necessary files
    """
    #vocab
    #vocab_file = open("json/vocab.json", "w")
    #vocab_file = json.dump(vocab, vocab_file)
    
    """
        9. TRAINING SETUP
    """
    
    #EMBEDDING LAYER
    embed = Embedding(DICTIONARY_SIZE, 
                  100,    
                  input_length=MAX_INPUT_LEN,
                  trainable=True)

    embed.build((None,))
    embed.set_weights([embedding_matrix])
    
    
    #ENCODER LAYER
    encoder = Input(shape=(69, ))
    encoder_embedded = embed(encoder)
    encoder_lstm = Bidirectional(LSTM(400, return_state=True, dropout=0.05, return_sequences = True))
    encoder_outputs, forward_h, forward_c, backward_h, backward_c = encoder_lstm(encoder_embedded)
    state_h = Concatenate()([forward_h, backward_h])
    state_c = Concatenate()([forward_c, backward_c])
    encoder_states = [state_h, state_c]
    
    
    #DECODER LAYER
    decoder = Input(shape=(69, ))
    decoder_embedded = embed(decoder)
    decoder_lstm = LSTM(400*2, return_state=True, return_sequences=True, dropout=0.05)
    output, _, _ = decoder_lstm(decoder_embedded, initial_state=encoder_states)
    
    
    #ATTENTION LAYER
    attention_layer = AttentionLayer()
    attention_output, attention_state = attention_layer([encoder_outputs, output])
    decoder_concatenated_input = Concatenate(axis=-1)([output, attention_output])
    
    
    #DENSE LAYER
    decoder_dense = Dense(DICTIONARY_SIZE, activation='softmax')
    final_output = decoder_dense(decoder_concatenated_input)
    
    
    #MODEL
    model = Model([encoder, decoder], final_output)
    model.summary()
    #tf.keras.utils.plot_model(model, to_file='photos/version.png',show_layer_names=True, show_shapes=True)
    
    #compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
    
    
    #model callbacks
    es = EarlyStopping(monitor='loss', mode = 'min',verbose=1, patience=50)   
    mc = ModelCheckpoint('models/best_model.h5', monitor='accuracy', mode='max', verbose=1, save_best_only=True)
    
    
    #fit model
    history = model.fit([encoder_inputs, decoder_inputs], 
                    decoder_final_outputs, 
                    epochs=1000,
                    callbacks=[es,mc])
    
    #plot the training loss and accuracy
    loss_train = history.history['loss']
    acc = history.history['acc']   
    import matplotlib.pyplot as plt
    
    epochs = range(1,507)
    
    plt.plot(epochs, loss_train, 'r', label='Training loss')
    plt.plot(epochs, acc, 'b', label='Accuracy')
    plt.title('Training loss and Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Loss and Accuracy')
    plt.legend()
    plt.show()
    plt.savefig('Version2.png')
    
    #finally, saved the trained model
    tf.keras.models.save_model(model, 'models/bubot' )
    
    
    """
        10. Inference model
    """
    
    encoder_model = tf.keras.models.Model(encoder, [encoder_outputs, encoder_states])


    decoder_state_input_h = tf.keras.layers.Input(shape=( 800,))
    decoder_state_input_c = tf.keras.layers.Input(shape=( 800,))
    
    decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
    
    
    decoder_outputs, dec_state_h, dec_state_c = decoder_lstm(decoder_embedded , initial_state=decoder_states_inputs)
    
    
    decoder_states = [dec_state_h, dec_state_c]
    
    dec_dense = Dense(DICTIONARY_SIZE, activation='softmax')
    
    decoder_model = tf.keras.models.Model([decoder, decoder_states_inputs],
                                          [decoder_outputs] + decoder_states)
    
    
    
    print("TESTING BUBOT.... \nPlease type your question....\nType 'EXIT' to quit program.") 
    print("------------------------------------------------------------")
    
    from BUbotApp.views import get_query
    
    while True: 
    
        """
            Get the user input, perform preprocessing
            and necessary operations to transform output into machine-readable input
        """
        USER_INPUT = get_query()
        # if USER_INPUT == 'EXIT':
        #     break
        print(USER_INPUT)
        USER_INPUT = prep_ques(USER_INPUT)

        user = []
        for token in USER_INPUT: 
            try:
                user.append(vocab[token])
            except:
                user.append(vocab['OUT'])
        user = [user]    

        user = pad_sequences(user, 69, padding='post', truncating = 'post')
    
        encoder_model_outputs, states = encoder_model.predict( user )
    
        target_response = np.zeros((1,1)) 
    
        target_response[0, 0] = vocab['SOS']

        decoded = ''
    
        while True :
    
            decoder_model_outputs , h, c= decoder_model.predict([ target_response] + states )
    
    
            attention_op, attention_state = attention_layer([encoder_model_outputs, decoder_model_outputs])
            decoder_concat_input = Concatenate(axis=-1)([decoder_model_outputs, attention_op])
            decoder_concat_input = dec_dense(decoder_concat_input)
    
    
            predicted = np.argmax( decoder_concat_input[0, -1, :] )
    
    
            predicted_word = inverse_vocab[predicted] + ' '
    
    
            if predicted_word != 'EOS ':
                decoded += predicted_word 
    
            if predicted_word == 'EOS ' or len(decoded.split()) > 70:
                break
    
            target_response = np.zeros( ( 1 , 1 ) )  
            target_response[ 0 , 0 ] = predicted
    
            stat = [h, c]  
    
        print("BUBOT : ", decoded)
        print("============================================================") 
    
    
