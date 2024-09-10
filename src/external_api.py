import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
api_key_conversion = os.getenv("API_KEY")


def currency_conversion(transaction: dict[str | Any]) -> float | str:
    """Функция возвращающяя сумму операции в рублях, если валюта доллар или евро, то конвертирует в рубли"""
    headers: dict = {"apikey": api_key_conversion}
    for i in transaction:
        try:
            code_currency: str = i.get("operationAmount").get("currency").get("code")
            transaction_amount: str = i.get("operationAmount").get("amount")
            if code_currency == "RUB":
                return float(transaction_amount)
            elif code_currency == "USD":
                url: str = (
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount={transaction_amount}"
                )
                response = requests.get(url, headers=headers)
                repo = response.json()
                result = round(repo.get("result"), 2)
                return float(result)
            elif code_currency == "EUR":
                url = (
                    f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount={transaction_amount}"
                )
                response = requests.get(url, headers=headers)
                repo = response.json()
                result = round(repo.get("result"), 2)
                return float(result)
            else:
                return "Не корректная валюта"
        except KeyError:
            continue
        except AttributeError:
            continue
    return "Не корректная транзакция"
