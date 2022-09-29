from typing import Union
from fastapi import FastAPI
from .config import settings

# uvicorn app.trystack:app --reload
app = FastAPI()

@app.get("/")
def read_root():
     return{"Hello": "World"}
     
@app.get("/info")
async def info():
     return {
          "env": settings.enviroment
     }

