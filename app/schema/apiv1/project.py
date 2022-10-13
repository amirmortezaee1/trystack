from importlib.metadata import metadata
from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from datetime import date

class ProjectBase(BaseModel):
     id : int
     name : str
     created_at : date
     last_updated_at : date
     status : int


class Project(ProjectBase):
     class Config:
          orm_mode = True