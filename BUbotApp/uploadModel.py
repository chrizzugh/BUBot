import io
import pymongo, gridfs
from gridfs import GridFS
from pymongo import MongoClient

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_DB = "bubotdatabase"

myclient = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
bubotdatabase = myclient[MONGO_DB]
fs = gridfs.GridFS(bubotdatabase)
model_name = 'saved_model.pb'
# model_name = "keras_metadata.pb"

with io.FileIO(model_name, 'r') as fileObject:
    docId = fs.put(fileObject, filename=model_name)