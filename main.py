from fastapi import FastAPI
from app.routes import auth, kyc, transactions, crypto

app = FastAPI()

app.include_router(auth.router)
app.include_router(kyc.router)
app.include_router(transactions.router)
app.include_router(crypto.router)

@app.get("/")
def root():
    return {"msg": "Welcome to TransendPay API"}