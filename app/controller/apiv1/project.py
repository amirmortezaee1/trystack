import email
from app.util import jsonify
from app.schema.apiv1 import ProjectCreate as ProjectSchema
from app.crud.project import get_items, create_item, get_item_by_name
from app.dependencies.project import get_db
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# from app.model import SessionLocal
# from app.dependencies import get_db
# from sqlalchemy.orm import Session
# from app.model import Project as ProjectModel

    
class ProjectController:
     def get_project(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
          items = get_items(db, skip=skip, limit=limit)
          return items
          # projects = get_items()
          # project_schema = ProjectSchema()
          # return jsonify(
          #      {"prjects": project_schema.dump(projects)}
          # )
 
     def get_project(project_id):
          return jsonify(status=501)
          

     def create_project(self, name,item, db):
          db_item = get_item_by_name(db , name=item.name)
          print(db_item)
          if db_item is not None: 
               raise HTTPException(status_code=400, detail="The name already used.")
          return create_item(name = name, db=db, item=item)
          
          
     def update_project(project_id):
          return jsonify(status=501)

     def delete_project(project_id):
          return jsonify(status=501)