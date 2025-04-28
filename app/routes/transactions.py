from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/")
def get_transactions(db: Session = Depends(lambda: SessionLocal())):
    return db.query(models.Transaction).all()

@router.post("/send")
def send_transaction(sender_id: int, receiver: str, amount: float, db: Session = Depends(lambda: SessionLocal())):
    tx = models.Transaction(sender_id=sender_id, receiver=receiver, amount=amount)
    db.add(tx)
    db.commit()
    return {"msg": "Transaction sent"}