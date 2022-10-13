from sqlalchemy import Boolean, Column,Integer, String, DateTime
from sqlalchemy.orm import relationship
from .model import Base
from app.util import uuidgen
from app.util import now
print(uuidgen)
class Project(Base):
    id = Column(Integer, primary_key=True, default=uuidgen)
    name = Column(String(256), unique=True, index=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=now)
    last_updated_at = Column(DateTime, nullable=True)
    status = Column(Integer)