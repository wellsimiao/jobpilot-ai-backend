from fastapi import Depends
from app.repositories.users_repository import UserRepository
from app.core.security import verify_password, create_token

class AuthService:

    def __init__(self, repo: UserRepository = Depends()):
        self.repo = repo

    def login(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return create_token({"sub": str(user.id)})
