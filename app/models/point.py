from sqlalchemy import Column, String, Float
from app.core.database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    city = Column(String, nullable=True)