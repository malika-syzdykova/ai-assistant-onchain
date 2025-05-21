import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

provider_url = os.getenv("WEB3_PROVIDER")
contract_address = os.getenv("CONTRACT_ADDRESS")

w3 = Web3(Web3.HTTPProvider(provider_url))

with open("smart_contract/abi.json", "r") as f:
    abi = json.load(f)

contract = w3.eth.contract(address=contract_address, abi=abi)


def read_all_questions():
    try:
        count = contract.functions.getCount().call()
        print(f"Всего записей: {count}\n")

        for i in range(count):
            question, answer = contract.functions.getQA(i).call()
            print(f"--- Запись {i+1} ---")
            print(f"Вопрос: {question}")
            print(f"Ответ: {answer}\n")

    except Exception as e:
        print("Ошибка чтения из контракта:", e)


if __name__ == "__main__":
    read_all_questions()
