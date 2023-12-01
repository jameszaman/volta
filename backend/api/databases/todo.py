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
    def add_todo(cls, payload: TodoSchema):
        collection = cls.db['project']
        # First we get the project where we will insert the new todo.
        project = collection.find_one({"_id": ObjectId(payload["project_id"])})

        # Must make sure that we found a project.
        if project:
            payload["_id"] = str(ObjectId())
            # Add the todo to the project.
            project["todos"].append(payload)

            # Update the project database.
            collection.update_one(
                {"_id": ObjectId(payload["project_id"])},
                {"$set": {"todos": project["todos"]}}
            )
            return project['todos'][-1]
        else:
            raise HTTPException(status_code=404, detail="Invalid Project Id. Please provide correct project ID.")


    @classmethod
    def update_todo(cls, payload: TodoSchema):
        collection = cls.db['project']
        # First we get the project where we will insert the new todo.
        project = collection.find_one({"_id": ObjectId(payload["project_id"])})

        # Must make sure that we found a project.
        if project:
            # Find the specific todo
            for todo_item in project["todos"]:
                if todo_item["_id"] == payload["todo_id"]:
                    todo_item["todo"] = payload["todo"]
                    todo_item["updated_at"] = payload["updated_at"]
                    todo_item["user"] = payload["user"]
                    # Update the project database.
                    collection.update_one(
                        {"_id": ObjectId(payload["project_id"])},
                        {"$set": {"todos": project["todos"]}}
                    )

                    return todo_item
        else:
            raise HTTPException(status_code=404, detail="Invalid Project Id. Please provide correct project ID.")


    @classmethod
    def get_todo_by_project(cls, project_id: str):
        collection = cls.db['project']
        # First we get the project where we will insert the new todo.
        project = collection.find_one({"_id": ObjectId(project_id)})

        if project:
            return project["todos"]
        else:
            raise HTTPException(status_code=404, detail="Invalid Project Id. Please provide correct project ID.")


    @classmethod
    def delete_todo(cls, id: str, project_id: str):
        collection = cls.db['project']
        # First we get the project where we will insert the new todo.
        project = collection.find_one({"_id": ObjectId(project_id)})
        if project:
            # We found the project, now we must find the todo.
            for todo in project["todos"]:
                if todo["_id"] == id:
                    # We found the todo, now we must delete it.
                    project["todos"].remove(todo)
                    # Update the project database.
                    collection.update_one(
                        {"_id": ObjectId(project_id)},
                        {"$set": {"todos": project["todos"]}}
                    )
                    return {"message": "Todo deleted successfully"}
            raise HTTPException(status_code=404, detail="Unable to delete resource. Resource not found.")
        else:
            raise HTTPException(status_code=404, detail="Invalid Project Id. Please provide correct project ID.")


    @classmethod
    def update_todo_status(cls, id: str, project_id: str, status: str):
        collection = cls.db['project']
        # First we get the project where we will insert the new todo.
        project = collection.find_one({"_id": ObjectId(project_id)})
        if project:
            # We found the project, now we must find the todo.
            for todo in project["todos"]:
                if todo["_id"] == id:
                    # We found the todo, now we must delete it.
                    print(project["todos"])
                    todo["status"] = status
                    # Update the project database.
                    collection.update_one(
                        {"_id": ObjectId(project_id)},
                        {"$set": {"todos": project["todos"]}}
                    )
                    return {"message": "Todo updated successfully", "status": "success"}
            raise HTTPException(status_code=404, detail="Unable to delete resource. Resource not found.")
        else:
            raise HTTPException(status_code=404, detail="Invalid Project Id. Please provide correct project ID.")
