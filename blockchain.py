from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("RPC_URL")))

PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT = w3.eth.account.from_key(PRIVATE_KEY)

def send_eth(amount, to_address):
    nonce = w3.eth.get_transaction_count(ACCOUNT.address)

    tx = {
        "nonce": nonce,
        "to": to_address,
        "value": w3.to_wei(amount, "ether"),
        "gas": 21000,
        "gasPrice": w3.to_wei("20", "gwei"),
        "chainId": 11155111
    }

    signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    return w3.to_hex(tx_hash)

def get_balance(address):
    return w3.eth.get_balance(address)