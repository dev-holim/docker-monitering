import datetime
from app.database import Base
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class ContainerLogs(Base):
    __tablename__ = 'container_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    container_id = Column(Integer, ForeignKey('container.id'), index=True)
    path = Column(String, nullable=False)
    is_main = Column(Boolean, nullable=False, default=False)
    category = Column(Integer, ForeignKey('artist_category.id'), index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

    artist_category = relationship("ArtistCategory", back_populates="artists")

    class Config:
        orm_mode = True