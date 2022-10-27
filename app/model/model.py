from email.policy import default
from sqlalchemy import Column,Integer, String, DateTime, VARCHAR, CHAR
from .project import Base
from app.util import uuidgen
from app.util import now

class Project(Base):
    __tablename__ = "projects"

    id = Column(VARCHAR(256), primary_key=True, default=uuidgen)
    name = Column(VARCHAR(256), index=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=now)
    last_updated_at = Column(DateTime, nullable=True, default=now)
    status = Column(Integer, nullable=True, default=0)