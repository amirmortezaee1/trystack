from sqlalchemy.orm import Session
from app.model import Project as ProjectModel
from app.schema.apiv1 import ProjectCreate as ProjectSchema
from fastapi import HTTPException

def get_item_by_id(db: Session, id: str):
    return db.query(ProjectModel).filter(ProjectModel.id == id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100,):
    return db.query(ProjectModel).offset(skip).limit(limit).all()

def get_item_by_name(db: Session, name: str):
    return db.query(ProjectModel).filter(ProjectModel.name == name).first()


def create_item(db: Session, name: str):
    db_item = ProjectModel(name = name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item