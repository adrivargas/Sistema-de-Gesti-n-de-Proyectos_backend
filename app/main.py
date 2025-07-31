from fastapi import FastAPI
from app.auth import auth_routes
from app.database import Base, engine
from app.routers import project_types, projects

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(project_types.router)
app.include_router(projects.router)
