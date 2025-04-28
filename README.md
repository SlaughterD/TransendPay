# TransendPay Backend

FastAPI backend server for **TransendPay** – the next-gen payment platform. 🚀

## Features
- Secure user authentication (JWT)
- KYC (Know Your Customer) document upload
- Transaction history (send/receive)
- QR Code payment support
- Cryptocurrency wallet integration (ETH balance + transactions)

## Tech Stack
- FastAPI
- PostgreSQL (via SQLAlchemy ORM)
- Cloudinary (for file uploads)
- Web3.py (for crypto transactions)
- Render (for deployment)

## Environment Variables
| Variable        | Purpose                       |
| --------------- | ----------------------------- |
| DATABASE_URL    | PostgreSQL connection URL     |
| CLOUDINARY_URL  | Cloudinary API URL             |
| INFURA_URL      | Ethereum Node URL (Infura)     |
| SECRET_KEY      | JWT Token signing secret       |

## How to Run Locally
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run server: `uvicorn main:app --reload`

---

## Deployment
TransendPay backend is Render-ready.

Create a service on [Render](https://render.com) and connect the GitHub repo.

Deploy with Render's **render.yaml** (provided).
