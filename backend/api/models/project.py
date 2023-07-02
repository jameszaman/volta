"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from .todo import TodoSchema
from typing import List

class ProjectSchema(BaseModel):
    # TODO: Will be using proper user in the future.
    user: str = Field(default="admin")
    name: str = Field(...)
    todos: List[TodoSchema] = Field(default=[])
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)