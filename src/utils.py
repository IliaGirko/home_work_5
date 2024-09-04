import json
import os
from typing import Any

from dotenv import load_dotenv

load_dotenv()
path_to_file_json = os.getenv("PATH_TO_FILE")


def financial_transaction_data_json(data: str = None) -> list[dict[str | Any]]:
    """Функция возвращает список словарей с транзакциями"""
    try:
        with open(data, "r", encoding="utf-8") as file:
            file_data = json.load(file)
            return file_data
    except Exception:
        return []
