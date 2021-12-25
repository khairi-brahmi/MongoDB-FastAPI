from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class sectionSchema(BaseModel):
    section_name: str = Field(...)
    hours: int = Field(...)


    class Config:
        schema_extra = {
            "example": {
                "section_name": "Computer Science",
                "hours": 62,
        
            }
        }

class UpdatesectionModel(BaseModel):
    section_name: Optional[str]
    hours: Optional[int]


    class Config:
        schema_extra = {
            "example": {
                "section_name": "Computer Science",
                "hours": 62,

            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }