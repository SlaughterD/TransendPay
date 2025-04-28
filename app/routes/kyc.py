from fastapi import APIRouter, UploadFile, File, Form, Depends
import cloudinary.uploader
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app import models

router = APIRouter(prefix="/kyc", tags=["KYC"])

@router.post("/")
def upload_kyc(user_id: int = Form(...), id_image: UploadFile = File(...), address_proof: UploadFile = File(...), db: Session = Depends(lambda: SessionLocal())):
    id_upload = cloudinary.uploader.upload(id_image.file)
    address_upload = cloudinary.uploader.upload(address_proof.file)
    kyc = models.KYC(user_id=user_id, id_image_url=id_upload['url'], address_proof_url=address_upload['url'])
    db.add(kyc)
    db.commit()
    return {"msg": "KYC submitted"}