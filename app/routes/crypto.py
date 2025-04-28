from fastapi import APIRouter
import os
from web3 import Web3

router = APIRouter(prefix="/crypto", tags=["Crypto"])

INFURA_URL = os.getenv("INFURA_URL")
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

@router.get("/balance/{address}")
def get_balance(address: str):
    balance = w3.eth.get_balance(address)
    return {"balance_eth": w3.from_wei(balance, 'ether')}

@router.post("/send")
def send_eth(from_address: str, to_address: str, private_key: str, amount_eth: float):
    nonce = w3.eth.get_transaction_count(from_address)
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(amount_eth, 'ether'),
        'gas': 21000,
        'gasPrice': w3.to_wei('50', 'gwei'),
    }
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return {"tx_hash": tx_hash.hex()}