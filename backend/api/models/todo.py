"""
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
"""

from pydantic import BaseModel, Field
from datetime import datetime

class TodoSchema(BaseModel):
    # TODO: Will be using proper user in the future.
    user: str = Field(default="admin")
    status: str = Field(default="pending")
    todo: str = Field(...)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)