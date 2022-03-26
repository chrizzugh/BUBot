import io
from xmlrpc import client
import pymongo, gridfs
from gridfs import GridFS
from pymongo import MongoClient
from bson import ObjectId
import json
from bson.json_util import dumps, loads


client = MongoClient("mongodb+srv://chriz:MbtFE28WQXjPenjV@cluster0.zdxg5.mongodb.net/bubotdatabase?retryWrites=true&w=majority")
db = client['bubotdatabase']
vocab_collection = db['bubotvocab']
abbrev_collection = db['bubotabbrev']



def import_json():
    with open(r'D:/Documents/thesis/BUBot/BUbotApp/models/vocab.json') as vocab_json:
        vocab = json.load(vocab_json)
    with open(r'D:/Documents/thesis/BUBot/BUbotApp/models/abbrev.json') as abbrev_json:
        abbrev = json.load(abbrev_json)


    vocab_collection.insert_one(vocab)
    abbrev_collection.insert_one(abbrev)


def retrieve_json():
    cursor_vocab = vocab_collection.find()
    cursor_abbrev = abbrev_collection.find()

    # Converting cursor to the list of dictionaries
    list_curVocab = list(cursor_vocab)
    list_curAbbrev = list(cursor_abbrev)

    # Converting to the JSON
    json_vocab = dumps(list_curVocab, indent = 4) 
    abbrev_json = dumps(list_curAbbrev, indent = 4) 

    # Writing data to file data.json
    with open(r'D:/Documents/thesis/BUBot/BUbotApp/models/vocab.json', 'w') as file:
        file.write(json_vocab)

    with open(r'D:/Documents/thesis/BUBot/BUbotApp/models/abbrev.json', 'w') as file:
        file.write(abbrev_json)

client.close()




