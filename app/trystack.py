from fastapi import FastAPI
from .resource.apiv1 import project
from app.model import engine
from app.model import Base as ModelBase

ModelBase.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(
     project.router
     )
 

# uvicorn app.trystack:app --reload
# docker run -d --name  mysql  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=test -e MYSQL_DATABASE=trystack mysql:8
# export TRYSTACK_API_DATABASE_URL=mysql+pymysql://root:test@localhost:3306/trystack
# export TRYSTACK_API_DATABASE_URL=mysql+mysqlconnector://root:test@localhost:3306/trystack
# docker exec -it mysql mysql -uroot -ptest --> show databases; use trystack; show tables
# docker build -t wwwsqldesigner .
# docker run -d -p 80:80 --rm --name wwwsqldesigner wwwsqldesigner:latest
# docker run -d -p 8080:80 wwwsqldesigner
# coverage run -m pytest
