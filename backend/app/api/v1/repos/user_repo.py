from sqlalchemy.orm import Session
from app.models.users import User
from app.api.v1.schemas.user_schema import UserCreate

class UserRepository:

    @staticmethod
    def create(db: Session, obj: UserCreate):
        user = User(
            email=obj.email,
            password=obj.password,  # depois colocaremos hash!
            full_name=obj.full_name
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
