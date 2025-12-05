from app.core.config import settings
import jwt
from datetime import datetime, timedelta

def create_token(data: dict, expires_delta: int = 60):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    payload.update({"exp": expire})
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
from app.core.config import settings
import jwt
from datetime import datetime, timedelta

def create_token(data: dict, expires_delta: int = 60):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    payload.update({"exp": expire})
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
