import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key_conversion = os.getenv("API_KEY")


def currency_conversion(transaction: dict[str | Any] = None) -> float | str:
    """Функция возвращающяя сумму операции в рублях, если валюта доллар или евро, то конвертирует в рубли"""
    headers: dict = {"apikey": api_key_conversion}
    for i in range(len(transaction)):
        try:
            code_currency: str = transaction[i]["operationAmount"]["currency"]["code"]
            transaction_amount: str = transaction[i]["operationAmount"]["amount"]
            if code_currency == "RUB":
                return transaction_amount
            elif code_currency == "USD":
                url: str = (
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={transaction_amount}"
                )
                response = requests.request("GET", url, headers=headers)
                repo = response.json()
                result = round(repo["result"], 2)
                return result
            elif code_currency == "EUR":
                url = (
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={transaction_amount}"
                )
                response = requests.request("GET", url, headers=headers)
                repo = response.json()
                result = round(repo["result"], 2)
                return result
            else:
                return "Не корректная валюта"
        except KeyError:
            continue
    return "Не корректная транзакция"
