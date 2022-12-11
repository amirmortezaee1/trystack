from fastapi import APIRouter
from app.controller.apiv1 import ProjectController
from app.schema.apiv1 import Project as ProjectSchema
from app.dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

router = APIRouter(
     prefix="/api/v1",
     responses={400: {"description": "not found"}},
)



@router.get("/", tags=["admin"], response_model=list[ProjectSchema])
def get(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
     """
          GET /project --> create project
     """
     return ProjectController().get_projects(skip, limit, db)
     

@router.get("/{item_id}", tags=["users"], response_model=ProjectSchema)
def get(item_id: str, db: Session = Depends(get_db)):
     """
          GET /project/id --> get project info
     """
     return ProjectController().get_project(item_id, db)

@router.post("/", tags=["admin"], response_model= ProjectSchema)
def create(name: str, db: Session= Depends(get_db)):
     """
          POST /project --> create new project
          POST /projects/<project_id> --> not allowed

     """ 
     return ProjectController().create_project(name, db)

@router.patch("/{item_id}", tags=["users"])
def update(item_id: str, status: int, db: Session= Depends(get_db)):
     """
        PATCH /projects --> not allowedSession
        PATCH /projects/<project_id> --> delete projects
     """
     return ProjectController().update_project(item_id, status, db)

@router.delete("/{item_id}", tags=["users"])
def delete(item_id: str , db: Session= Depends(get_db)):
     """
        DELETE /projects --> not allowed
        DELETE /projects/<project_id> --> delete projects
     """
     return ProjectController().delete_project(item_id, db)