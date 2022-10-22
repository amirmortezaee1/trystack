
from fastapi import APIRouter
from app.controller.apiv1 import ProjectController
from app.schema.apiv1 import ProjectCreate as ProjectSchema
from app.dependencies import get_db



from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from app.crud.project import get_items, create_item, get_item_by_name


router = APIRouter(
     prefix="/api/v1",
     responses={400: {"description": "not found"}},
)



@router.get("/", tags=["admin"], response_model=ProjectSchema)
def get():
     """
          GET /project --> create project
     """
     return ProjectController().get_project()
     

@router.get("/{project_id}", tags=["users"])
def get():
     """
          GET /project/id --> get project info
     """
     return ProjectController().get_project()

@router.post("/", tags=["admin"],response_model= ProjectSchema)
def create(name: str, item: ProjectSchema, db: Session= Depends(get_db)):
     """
          POST /project --> create new project
          POST /projects/<project_id> --> not allowed

     """ 
     # return ProjectController().create_project(name, item, db)
     db_item = get_item_by_name(db , name=item.name)
     print(db_item)
     if db_item is not None: 
          raise HTTPException(status_code=400, detail="The name already used.")
     return create_item(name=name, db=db, item=item)

@router.patch("/{project_id}", tags=["users"])
def update(project_id):
     """
        PATCH /projects --> not allowed
        PATCH /projects/<project_id> --> delete projects
     """
     return ProjectController.update_project(project_id)

@router.delete("/{project_id}", tags=["users"])
def delete(project_id):
     """
        DELETE /projects --> not allowed
        DELETE /projects/<project_id> --> delete projects
     """
     return ProjectController.delete_project(project_id)