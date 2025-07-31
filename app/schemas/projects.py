from pydantic import BaseModel
from datetime import date
from typing import Optional
from .ProjectsType import ProjectType

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    project_type_id: int
    owner_id: int
    status: str
    start_date: date
    end_date: date
    budget: float

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: date
    project_type: ProjectType

    class Config:
        orm_mode = True
