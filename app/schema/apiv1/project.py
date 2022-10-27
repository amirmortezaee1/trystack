from importlib.metadata import metadata
from pydantic import BaseModel
from pydantic.schema import schema
from datetime import date

class ProjectBase(BaseModel):
     name : str
     class Config:
          orm_mode = True

class ProjectCreate(ProjectBase):
     pass

class Project(ProjectBase):
     last_updated_at : date
     created_at : date
     id : str
     status : int

     class Config:
          orm_mode = True