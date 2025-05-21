import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

provider_url = os.getenv("WEB3_PROVIDER")
contract_address = os.getenv("CONTRACT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
account = os.getenv("ACCOUNT_ADDRESS")

w3 = Web3(Web3.HTTPProvider(provider_url))

with open("smart_contract/abi.json", "r") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)

def store_on_chain(question, answer):
    try:
        nonce = w3.eth.get_transaction_count(account)
        txn = contract.functions.addQA(question, answer).build_transaction({
            'chainId': 11155111,  # Sepolia
            'gas': 300000,
            'gasPrice': w3.to_wei('10', 'gwei'),
            'nonce': nonce
        })
        signed_txn = w3.eth.account.sign_transaction(txn, private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

        # 🔥 Ждем подтверждение
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

        print("Tx successful:", receipt.transactionHash.hex())
        return receipt.transactionHash.hex()
    except Exception as e:
        print("Ошибка при отправке в блокчейн:", e)
        return None
