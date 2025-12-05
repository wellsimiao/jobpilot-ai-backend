from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import LoginRequest, LoginResponse
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, service: AuthService = Depends()):
    token = service.login(payload.email, payload.password)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return LoginResponse(access_token=token)
