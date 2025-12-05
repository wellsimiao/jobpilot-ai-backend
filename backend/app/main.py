from fastapi import FastAPI
from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.users import router as users_router
from app.api.v1.routes.jobs import router as jobs_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(jobs_router)


