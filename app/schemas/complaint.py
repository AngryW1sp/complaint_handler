from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ComplaintCreate(BaseModel):
    text: str


class ComplaintResponse(BaseModel):
    id: int
    status: str
    sentiment: str
    category: str

    class Config:
        orm_mode = True
