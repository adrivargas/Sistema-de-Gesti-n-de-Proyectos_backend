from fastapi import FastAPI
from app.auth import auth_routes
from app.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
