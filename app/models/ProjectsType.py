from sqlalchemy import Column, Integer, String
from app.database import Base

class ProjectType(Base):
    __tablename__ = "project_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    color = Column(String)  # Ej: "#FF0000"
    icon = Column(String)   # Ej: "fa-rocket"
