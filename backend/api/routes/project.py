"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from config import API_PREFIX
from ..models.project import ProjectSchema
from ..databases.project import ProjectDB

router = APIRouter(prefix=f'{API_PREFIX}/project')

@router.post('/new', response_description="Add a new Project")
def create_project(project: ProjectSchema = Body(...)):
    project = jsonable_encoder(project)
    new_project = ProjectDB.add_project(project)
    return new_project

@router.get('/all', response_description="Get all the Project")
def get_all_project():
    project_list = ProjectDB.get_all_project()
    return project_list

@router.delete('/delete', response_description='Delete a single Project')
def delete_project(id: str):
    response = ProjectDB.delete_project(id)
    return response