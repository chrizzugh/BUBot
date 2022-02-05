# Libraries Imported
import json
import string
import logging
import pandas as pd
from gensim.models import Word2Vec
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Important variables
wnl = WordNetLemmatizer()
stop = stopwords.words('english')

# Accessing json file
json_file = 'intents.json'
with open('intents.json','r',encoding="utf-8") as f:
    # Loading the json file
    data = json.load(f)

# Converting the Contents of the json file into Data frames
df = pd.DataFrame(data)
df['patterns'] = df['patterns'].apply(', '.join)

# Printing the Dataframes as a csv file but can also be as txt file
df.to_csv('data.csv')
#print(df)

# Data Preprocessing Starts Here
# 1. Converting all the letters into lowercase
df['patterns'] = df['patterns'].apply(lambda x:' '.join(x.lower() for x in x.split()))

# 2. Removing all the Punctuations
df['patterns']= df['patterns'].apply(lambda x: ' '.join(x for x in x.split() if x not in string.punctuation))

# 3. Removing Symbols (Match all characters that DO NOT (^) match (\w alphanumeric characters) and \s (white space and tab) and - (hyphen) and replace them with "")
df['patterns']= df['patterns'].str.replace('[^\w\s]','', regex=True)

# 4. Removing non-integer characters
df['patterns']= df['patterns'].apply(lambda x: ' '.join(x for x in x.split() if  not x.isdigit()))

# 5. Removing Stopwords
df['patterns'] = df['patterns'].apply(lambda x:' '.join(x for x in x.split() if not x in stop))

# 6. Lemmatization
df['patterns'] = df['patterns'].apply(lambda x: " ".join([wnl.lemmatize(word) for word in x.split()]))

# Storing all data into a list
bigger_list=[]
for i in df['patterns']:
    li = list(i.split(" "))
    bigger_list.append(li)
#print(bigger_list)

# Word Embedding with Word2Vec starts here
# min_count: It will ignore all the words with a total frequency lower than this.
# vector_size: It tells the dimensionality of the word vectors.
# workers: These are the threads to train the model
model = Word2Vec(bigger_list, min_count=1,vector_size=100,workers=4)
#print(model)

# Saving the Model
model.save("word2vec.model")
model.save("model.bin")
# Printing the vector values in txt file in non-binary form 
model.wv.save_word2vec_format('vectors.txt', binary=False)

# Loading the model
model = Word2Vec.load('model.bin')
# For printing the vocabulary
vocab = list(model.wv.key_to_index)

# Helpful References
# https://social.msdn.microsoft.com/Forums/en-US/a4ad1fad-f345-484b-af58-07a5f349d1bc/about-regexreplacestrinput-quotwsquot-quotquot?forum=csharplanguage
# https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html#pandas.Series.str.replace
# https://github.com/RaRe-Technologies/gensim/wiki/Migrating-from-Gensim-3.x-to-4