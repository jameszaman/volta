from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from config import API_PREFIX
from ..models.todo import TodoSchema
from ..databases.todo import TodoDB

router = APIRouter(prefix=f'{API_PREFIX}/todo')

@router.post('/new', response_description="Add a new Todo")
def create_todo(todo: TodoSchema = Body(...)):
    todo = jsonable_encoder(todo)
    new_todo = TodoDB.add_todo(todo)
    return new_todo

@router.get('/all', response_description="Get all the Todo")
def get_all_todo():
    todo_list = TodoDB.get_all_todo()
    return todo_list