"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""
from pymongo import MongoClient
from config import MONGO_DATABASE_URI, MONGO_DATABASE_NAME
from ..models.todo import TodoSchema

class TodoDB:
    client = None
    db = None

    @classmethod
    def initialize(cls):
        cls.client = MongoClient(str(MONGO_DATABASE_URI))
        cls.db = cls.client[MONGO_DATABASE_NAME]

    @classmethod
    def add_todo(cls, todo: TodoSchema):
        collection = cls.db['todo']
        new_todo = collection.insert_one(todo)
        return str(new_todo.inserted_id)

    @classmethod
    def get_all_todo(cls):
        collection = cls.db['todo']
        cursor = collection.find({}, {})
        todo_list = []
        for todo in cursor:
            todo["_id"] = str(todo["_id"])
            todo_list.append(todo)
            # todo_list[index]["_id"] = str(todo_list[index]["_id"])
        return todo_list

