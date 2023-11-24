"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""
from config import API_PREFIX
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..databases.todo import TodoDB
from ..models.todo import TodoSchema

router = APIRouter(prefix=f'{API_PREFIX}/todo', tags=['Todo'])

@router.post(
    '/new',
    response_description="Add a new Todo"
)
def create_todo(
    project_id: str,
    todo: TodoSchema = Body(...)
):
    todo = jsonable_encoder(todo)
    new_todo = TodoDB.add_todo(project_id, todo)
    return new_todo

@router.get(
    '/all',
    response_description="Get all the Todo"
)
def get_all_todo(project_id: str):
    todo_list = TodoDB.get_todo_by_project(project_id)
    return todo_list

@router.delete(
    '/delete',
    response_description='Delete a single Todo'
)
def delete_todo(
    id: str,
    project_id: str
):
    response = TodoDB.delete_todo(id, project_id)
    return response

@router.patch(
    '/update_status',
    response_description='Update the status of a single Todo'
)
def update_todo_status(
    id: str,
    project_id: str,
    status: str
):
    response = TodoDB.update_todo_status(id, project_id, status)
    return response
