from fastapi import APIRouter ,FastAPI
from .config import settings
from .resource.apiv1 import project
from .model import SessionLocal, engine, Project
from .schema import
# uvicorn app.trystack:app --reload
app = FastAPI()
router = APIRouter()

app.include_router(
     project.router
     )

