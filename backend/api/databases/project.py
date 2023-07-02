"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""
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
            project["_id"] = str(project["_id"])
            project_list.append(project)
        return project_list
    
    @classmethod
    def delete_project(cls, id: int):
        collection = cls.db['project']
        response = collection.delete_one({'_id': ObjectId(id)})
        if response.deleted_count == 1:
            return {"message": "Project deleted successfully"}
        else:
            return {"message": "Unable to delete Project"}


