from fastapi import Depends
from app.repositories.users_repository import UserRepository
from app.schemas.users import UserCreate, UserUpdate

class UserService:

    def __init__(self, repo: UserRepository = Depends()):
        self.repo = repo

    def create_user(self, payload: UserCreate):
        return self.repo.create(payload)

    def list_users(self):
        return self.repo.list_all()

    def get_user(self, user_id: int):
        return self.repo.get(user_id)

    def update_user(self, user_id: int, payload: UserUpdate):
        return self.repo.update(user_id, payload)

    def delete_user(self, user_id: int):
        self.repo.delete(user_id)
