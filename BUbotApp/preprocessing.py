'''
    
    !DATA PREPROCESSING
    
'''
import nltk
#! uncomment if first run
# nltk.download('stopwords') #for first run
# nltk.download('punkt') #for first run
# nltk.download('wordnet') #for first run
# nltk.download('omw-1.4') #for first run

from nltk.corpus import stopwords
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
tk = WhitespaceTokenizer()
import re
import string
import json

def prep_ques(txt):
    
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

    #E. stemming or getting the root words
    #removes necessary character, might affect predictions
    
    #F. lemmatization 
    lemmatizer = WordNetLemmatizer()
    txt = [lemmatizer.lemmatize(token, pos="v") for token in txt]

    return txt
