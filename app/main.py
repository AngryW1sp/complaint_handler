from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.schemas.complaint import ComplaintCreate, ComplaintResponse
from app.services.crud import create_complaint

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Complaint Service is running"}


@app.post("/complaints/", response_model=ComplaintResponse)
def submit_complaint(complaint: ComplaintCreate, db: Session = Depends(get_db)):
    complaint_ = create_complaint(db, complaint)
    return complaint_
