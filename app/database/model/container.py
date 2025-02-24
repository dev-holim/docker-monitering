import datetime
from app.database import Base
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class Container(Base):
    __tablename__ = 'container'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    container_logs = relationship("ContainerLogs", back_populates="container_logs")

    class Config:
        orm_mode = True