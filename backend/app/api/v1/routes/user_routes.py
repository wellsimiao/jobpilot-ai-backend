from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.api.v1.schemas.user_schema import UserCreate, UserResponse
from app.api.v1.services.user_service import UserService

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", response_model=UserResponse)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        user = UserService.register(db, payload)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
