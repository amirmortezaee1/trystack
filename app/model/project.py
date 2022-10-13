from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL=mysql+pymysql://root:test@localhost:3306/trystack

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




# sudo docker run -d --name  mysql  -p 3306:3306 -e MYSQL_ROOT_PASSWORD=test -e MYSQL_DATABASE=trystack mysql:8
# export TRYSTACK_API_DATABASE_URL=mysql+pymysql://root:test@localhost:3306/trystack
# docker build -t wwwsqldesigner .
# docker run -d -p 80:80 --rm --name wwwsqldesigner wwwsqldesigner:latest
# docker run -d -p 8080:80 wwwsqldesigner