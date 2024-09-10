import json
import logging
import os
from typing import Any

from dotenv import load_dotenv

logger = logging.getLogger("utils.py")
logger.setLevel(logging.DEBUG)
logger_handler = logging.FileHandler("logs/utils.log", "w")
logger_formatter = logging.Formatter(
    "Time: %(asctime)s Module name: %(name)s Level message: %(levelname)s Message: %(message)s"
)
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)

load_dotenv()
path_to_file_json = os.getenv("PATH_TO_FILE")


def financial_transaction_data_json(data: str = None) -> list[dict[str | Any]]:
    """Функция возвращает список словарей с транзакциями"""
    logger.info("Запуск функции financial_transaction_data_json")
    try:
        logger.info("Прочтение информации о транзакциях из json-файл")
        with open(data, "r", encoding="utf-8") as file:
            file_data = json.load(file)
            logger.info("Завершение работы функции financial_transaction_data_json")
            return file_data
    except Exception as error_message:
        logger.error(f"Завершение работы функции с ошибкой {error_message}")
        return []
