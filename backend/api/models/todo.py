"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class TodoSchema(BaseModel):
    # TODO: Will be using proper user in the future.
    project_id: str = Field(...)
    user: str = Field(default="admin")
    status: str = Field(default="pending")
    todo: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    priority: int = Field(default=0)


class TodoUpdateSchema(BaseModel):
    # TODO: Will be using proper user in the future.
    project_id: str = Field(...)
    user: str = Field(default="admin")
    todo: str = Field(...)
    todo_id: str = Field(...)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class TodoPositionUpdateRequest(BaseModel):
    project_id: str = Field(...)
    previous_position: int = Field(...)
    new_position: int = Field(...)
