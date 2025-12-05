from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database import get_db
from app.models.users import User
from app.schemas.users import UserCreate, UserUpdate

class UserRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create(self, payload: UserCreate):
        new = User(name=payload.name, email=payload.email, password=payload.password)
        self.db.add(new)
        self.db.commit()
        self.db.refresh(new)
        return new

    def list_all(self):
        return self.db.query(User).all()

    def get(self, id: int):
        return self.db.query(User).filter_by(id=id).first()

    def get_by_email(self, email: str):
        return self.db.query(User).filter_by(email=email).first()

    def update(self, id: int, payload: UserUpdate):
        user = self.get(id)
        if payload.name:
            user.name = payload.name
        if payload.email:
            user.email = payload.email
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, id: int):
        user = self.get(id)
        self.db.delete(user)
        self.db.commit()
