from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.ProjectsType import ProjectType as ProjectTypeModel
from app.schemas.ProjectsType import ProjectType as ProjectTypeSchema, ProjectTypeCreate

router = APIRouter(prefix="/project-types", tags=["Project Types"])

@router.post("", response_model=ProjectTypeSchema)
def create_project_type(data: ProjectTypeCreate, db: Session = Depends(get_db)):
    pt = ProjectTypeModel(**data.dict())
    db.add(pt)
    db.commit()
    db.refresh(pt)
    return pt

@router.get("", response_model=list[ProjectTypeSchema])
def get_all(db: Session = Depends(get_db)):
    return db.query(ProjectTypeModel).all()

@router.get("/{type_id}", response_model=ProjectTypeSchema)
def get_project_type(type_id: int, db: Session = Depends(get_db)):
    type_ = db.query(ProjectTypeModel).filter(ProjectTypeModel.id == type_id).first()
    if not type_:
        raise HTTPException(status_code=404, detail="Project type not found")
    return type_

@router.put("/{type_id}", response_model=ProjectTypeSchema)
def update_project_type(type_id: int, updated_type: ProjectTypeCreate, db: Session = Depends(get_db)):
    type_ = db.query(ProjectTypeModel).filter(ProjectTypeModel.id == type_id).first()
    if not type_:
        raise HTTPException(status_code=404, detail="Project type not found")
    for key, value in updated_type.dict().items():
        setattr(type_, key, value)
    db.commit()
    db.refresh(type_)
    return type_

@router.delete("/{type_id}", status_code=204)
def delete_project_type(type_id: int, db: Session = Depends(get_db)):
    type_ = db.query(ProjectTypeModel).filter(ProjectTypeModel.id == type_id).first()
    if not type_:
        raise HTTPException(status_code=404, detail="Project type not found")
    db.delete(type_)
    db.commit()
    return Response(status_code=204)
