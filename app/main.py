from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth import auth_routes
from app.database import Base, engine
from app.routers import project_types, projects, users

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(project_types.router)
app.include_router(projects.router)
app.include_router(users.router)
