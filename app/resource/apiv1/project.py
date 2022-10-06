from crypt import methods
from typing_extensions import Self
from fastapi import APIRouter
from app.controller.apiv1 import ProjectController, project

router = APIRouter(
     prefix="/api/v1",
     responses={400: {"description": "not found"}},
)


@router.get("/", tags=["admin"])
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

@router.post("/", tags=["admin"])
def create():
     """
          POST /project --> create new project
          POST /projects/<project_id> --> not allowed

     """
     return ProjectController.create_project()

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