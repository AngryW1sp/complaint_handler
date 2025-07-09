from sqlalchemy.orm import Session
from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintCreate
from datetime import datetime


def create_complaint(db: Session, complaint: ComplaintCreate, sentiment: str = "unknown", category: str = "другое"):
    complaint_model = Complaint(
        text=complaint.text,
        sentiment=sentiment,
        category=category,
        timestamp=datetime.now())
    db.add(complaint_model)
    db.commit()
    db.refresh(complaint_model)
    return complaint_model
