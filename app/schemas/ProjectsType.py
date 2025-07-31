# app/schemas/ProjectsType.py
from pydantic import BaseModel

class ProjectTypeBase(BaseModel):
    name: str
    description: str | None = None
    color: str | None = None
    icon: str | None = None

class ProjectTypeCreate(ProjectTypeBase):
    pass

class ProjectType(ProjectTypeBase):
    id: int

    class Config:
        orm_mode = True
