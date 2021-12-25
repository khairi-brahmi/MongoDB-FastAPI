from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    section: str = Field(...)
    year: int = Field(..., gt=0, lt=9)


    class Config:
        schema_extra = {
            "example": {
                "fullname": "Khairi Brahmi",
                "email": "khairibrahmi00@gmail.com",
                "section": "Computer Science",
                "year": 2,
        
            }
        }

class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    section: Optional[str]
    year: Optional[int]


    class Config:
        schema_extra = {
            "example": {
                "fullname": "Khairi Brahmi",
                "email": "khairibrahmi00@gmail.com",
                "section": "IT Engineering",
                "year": 3,

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