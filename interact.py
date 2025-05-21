import json
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Загрузка переменных из .env
provider_url = os.getenv("WEB3_PROVIDER")
contract_address = os.getenv("CONTRACT_ADDRESS")
private_key = os.getenv("PRIVATE_KEY")
account = os.getenv("ACCOUNT_ADDRESS")

# Подключение к сети Web3
w3 = Web3(Web3.HTTPProvider(provider_url))
assert w3.is_connected(), "Web3 не подключён"

# Загрузка ABI
with open("smart_contract/abi.json", "r") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)

def send_qa_to_chain(question, answer):
    nonce = w3.eth.get_transaction_count(account)
    txn = contract.functions.addQA(question, answer).build_transaction({
        'chainId': 11155111,  # Sepolia
        'gas': 300000,
        'gasPrice': w3.to_wei('10', 'gwei'),
        'nonce': nonce,
    })
    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(f"Вопрос/ответ отправлены: {tx_hash.hex()}")

# Пример
if __name__ == "__main__":
    q = input("Вопрос: ")
    a = input("Ответ: ")
    send_qa_to_chain(q, a)
