from fastapi import APIRouter, Depends
from typing import List
from app.schemas.jobs import JobCreate, JobUpdate, JobResponse
from app.services.jobs_service import JobService

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobResponse)
def create_job(payload: JobCreate, service: JobService = Depends()):
    return service.create_job(payload)

@router.get("/", response_model=List[JobResponse])
def list_jobs(service: JobService = Depends()):
    return service.list_jobs()

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, service: JobService = Depends()):
    return service.get_job(job_id)

@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, payload: JobUpdate, service: JobService = Depends()):
    return service.update_job(job_id, payload)

@router.delete("/{job_id}")
def delete_job(job_id: int, service: JobService = Depends()):
    service.delete_job(job_id)
    return {"detail": "Vaga removida com sucesso"}
