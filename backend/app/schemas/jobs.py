from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    description: str

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class JobResponse(JobBase):
    id: int

    class Config:
        orm_mode = True
