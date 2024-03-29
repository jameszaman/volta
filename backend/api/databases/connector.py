"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""
# TODO: I have this class, but it seems that I am not using it.
# I should be using this to connect to the database.
# Right now I am calling this for each database class.

from pymongo import MongoClient, errors
from backend.config import MONGO_DATABASE_URI, MONGO_DB_NAME

client = MongoClient(MONGO_DATABASE_URI, serverSelectionTimeoutMS=5000)
try:
    client.server_info()
    print('Connected to MongoDB server')
except errors.ServerSelectionTimeoutError:
    print('Error: Could not connect to MongoDB server.')
    client.close()
    client = None

db = client[MONGO_DB_NAME] if client else None
