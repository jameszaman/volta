from pymongo import MongoClient, errors
from config import MONGO_URI, MONGO_DB_NAME

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
try:
    client.server_info()
    print('Connected to MongoDB server')
except errors.ServerSelectionTimeoutError:
    print('Error: Could not connect to MongoDB server.')
    client.close()
    client = None

db = client[MONGO_DB_NAME] if client else None
