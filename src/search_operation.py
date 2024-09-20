import re
from collections import Counter
from typing import Any

from widget import get_date, mask_account_card


def search_by_state(dictionary: list[dict[Any]], search_string: str) -> list[dict[Any]]:
    """Функция фильтрует список словарей по заданному статусу операции в поиске"""
    result: list[dict[Any]] = []
    for trans in dictionary:
        operation = trans.get("state")
        if operation:
            filter_list = re.findall(search_string, operation, flags=re.IGNORECASE)
            if filter_list:
                result.append(trans)
    return result


def func_sorted_by_date(dictionary: list[dict[Any]], search_string: bool) -> list[dict[Any]]:
    """Функция производит сортировку по дате, в зависимоти от переданного флага- по убыванию или по уменьшению"""
    sorted_list_of_dictionaries_date = sorted(dictionary, key=lambda x: x["date"], reverse=search_string)
    return sorted_list_of_dictionaries_date


def func_filter_currency_json(dictionary: list[dict[Any]], search_string: str) -> list[dict[Any]]:
    """Функция фильтрует список словарей по валюте RUB"""
    result: list[dict[Any]] = []
    for trans in dictionary:
        if trans.get("operationAmount").get("currency").get("code") == search_string:
            result.append(trans)
    return result


def func_filter_currency_excel_and_csv_files(dictionary: list[dict[Any]], search_string: str) -> list[dict[Any]]:
    """Функция фильтрует список словарей по валюте RUB"""
    result: list[dict[Any]] = []
    for trans in dictionary:
        if trans.get("currency_code") == search_string:
            result.append(trans)
    return result


def filter_by_category(dictionary: list[dict[Any]], search_string: str) -> list[dict[Any]]:
    """Функция фильтрует список словарей по заданному слову в описании транзакции в поиске"""
    result: list = []
    for trans in dictionary:
        operation = trans.get("description")
        if operation:
            ret = re.findall(search_string, operation, flags=re.IGNORECASE)
            if ret:
                result.append(trans)
    return result


def func_output_result(dictionary: list[dict[Any]]) -> dict[str, list[Any]]:
    """Функция составдяющая итоговую отфильтрованную информацию в читаемый вид"""
    result_dict = {
        "date_operation": [],
        "description": [],
        "card_from": [],
        "card_to": [],
        "amount": [],
        "currency_code": [],
    }
    for dict_ in dictionary:
        date_operation: list = get_date(dict_)
        result_dict["date_operation"].append(date_operation)
        descriptions: str = dict_.get("description")
        result_dict["description"].append(descriptions)
        card_from: str = mask_account_card(dict_.get("from"))
        result_dict["card_from"].append(card_from)
        card_to: str = mask_account_card(dict_.get("to"))
        result_dict["card_to"].append(card_to)
    return result_dict


def counting_quantity(transaction_list: dict[Any], dictionary: dict[str, Any]) -> dict[Any, int]:
    """Функция для подсчета количества банковских операций определенного типа"""
    counted = Counter(transaction_list)
    if dictionary["key"] in counted:
        return {dictionary["key"]: counted[dictionary["key"]]}


# print(counting_quantity(["Перевод", "ысуф","сывс","высы", "Перевод"], {"key":"Перевод"}))
