"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""
from fastapi import HTTPException
from pymongo import MongoClient
from config import MONGO_DATABASE_URI, MONGO_DATABASE_NAME
from ..models.project import ProjectSchema
from bson import ObjectId

class ProjectDB:
    client = None
    db = None

    @classmethod
    def initialize(cls):
        cls.client = MongoClient(str(MONGO_DATABASE_URI))
        cls.db = cls.client[MONGO_DATABASE_NAME]

    @classmethod
    def add_project(cls, project: ProjectSchema):
        collection = cls.db['project']
        new_project = collection.insert_one(project)
        return str(new_project.inserted_id)

    @classmethod
    def get_all_project(cls):
        collection = cls.db['project']
        cursor = collection.find({}, {})
        project_list = []
        for project in cursor:
            project_list.append({"_id": str(project["_id"]), "name": project["name"]})
        return project_list
    
    @classmethod
    def update_project(cls, payload: ProjectSchema):
        collection = cls.db['project']
        project = collection.find_one({'_id': ObjectId(payload["project_id"])})
        
        if project:
            try:
                update_result = collection.update_one(
                    {'_id': ObjectId(payload["project_id"])},
                    {'$set': {
                        "name": payload["project_name"],
                        "updated_at": payload["updated_at"]
                    }}
                )
                if update_result.modified_count > 0:
                    # Fetch and return the updated project after the update
                    updated_project = collection.find_one({'_id': ObjectId(payload["project_id"])})
                    updated_project["_id"] = str(updated_project["_id"])
                    return updated_project
                else:
                    # If no documents were modified, it means the update didn't happen
                    raise HTTPException(status_code=400, detail="Update failed. The document does not exist.")
            except Exception as e:
                raise HTTPException(status_code=500, detail="Internal server error")
        else:
            raise HTTPException(status_code=404, detail="Project not found")

    
    @classmethod
    def delete_project(cls, id: int):
        collection = cls.db['project']
        response = collection.delete_one({'_id': ObjectId(id)})
        if response.deleted_count == 1:
            return {"message": "Project deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Project not found")


