import json

from src.utils import financial_transaction_data_json


def test_financial_transaction_data_json():
    assert financial_transaction_data_json() == []


def test_financial_transaction_data():
    with open("C:/Users/ggggg/PycharmProjects/home_work_5/data/operations.json", "r", encoding="utf-8") as file_test:
        file_data_test = json.load(file_test)
    assert (
        financial_transaction_data_json("C:/Users/ggggg/PycharmProjects/home_work_5/data/operations.json")
        == file_data_test
    )
