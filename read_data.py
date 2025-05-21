from web3 import Web3
import json
import os
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER")))
address = Web3.to_checksum_address(os.getenv("CONTRACT_ADDRESS"))

with open("smart_contract/abi.json", "r") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=address, abi=abi)

count = contract.functions.getCount().call()
print(f"Всего QA записей: {count}")

for i in range(count):
    q, a = contract.functions.getQA(i).call()
    print(f"Q: {q}\nA: {a}\n---")
