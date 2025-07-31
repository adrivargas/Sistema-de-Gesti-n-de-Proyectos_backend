from datetime import date
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    project_type_id = Column(Integer, ForeignKey("project_types.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))  # Asegúrate que tengas modelo de usuarios
    status = Column(String)  # Ej: "active", "completed"
    start_date = Column(Date)
    end_date = Column(Date)
    budget = Column(Float)
    created_at = Column(Date, default=date.today)

    project_type = relationship("ProjectType")
    owner = relationship("User")  # Define el modelo User si no está aún
