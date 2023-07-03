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
from bson import ObjectId
from fastapi import HTTPException
class TodoDB:
    client = None
    db = None

    @classmethod
    def initialize(cls):
        cls.client = MongoClient(str(MONGO_DATABASE_URI))
        cls.db = cls.client[MONGO_DATABASE_NAME]

    @classmethod
    def add_todo(cls, project_id: str, todo: TodoSchema):
        collection = cls.db['project']
        # First we get the project where we will insert the new todo.
        project = collection.find_one({"_id": ObjectId(project_id)})

        # Must make sure that we found a project.
        if project:
            # Add the todo to the project.
            project["todos"].append(todo)

            # Update the project database.
            project["_id"] = str(project["_id"])
            collection.update_one(
                {"_id": ObjectId(project_id)},
                {"$set": {"todos": project["todos"]}}
            )
            return project
        else:
            raise HTTPException(status_code=404, detail="Invalid Project Id. Please provide correct project ID.")

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
    
    @classmethod
    def delete_todo(cls, id: int):
        collection = cls.db['todo']
        response = collection.delete_one({'_id': ObjectId(id)})
        if response.deleted_count == 1:
            return {"message": "Todo deleted successfully"}
        else:
            return {"message": "Unable to delete Todo"}


