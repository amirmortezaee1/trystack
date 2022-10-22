from importlib.metadata import metadata
from pydantic import BaseModel
from pydantic.schema import schema
from datetime import date

class ProjectBase(BaseModel):
     name : str
     status : int

class ProjectCreate(ProjectBase):
     pass

class Project(ProjectBase):
     id : int
     created_at : date
     last_updated_at : date
     
     class Config:
          orm_mode = True