from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    kyc_status = Column(String, default="pending")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"))
    receiver = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class KYC(Base):
    __tablename__ = "kyc"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    id_image_url = Column(String)
    address_proof_url = Column(String)
    status = Column(String, default="pending")