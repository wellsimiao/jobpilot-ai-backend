from fastapi import Depends
from app.repositories.jobs_repository import JobRepository
from app.schemas.jobs import JobCreate, JobUpdate

class JobService:

    def __init__(self, repo: JobRepository = Depends()):
        self.repo = repo

    def create_job(self, payload: JobCreate):
        return self.repo.create(payload)

    def list_jobs(self):
        return self.repo.list_all()

    def get_job(self, job_id: int):
        return self.repo.get(job_id)

    def update_job(self, job_id: int, payload: JobUpdate):
        return self.repo.update(job_id, payload)

    def delete_job(self, job_id: int):
        self.repo.delete(job_id)
