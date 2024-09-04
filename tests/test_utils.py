from src.utils import financial_transaction_data_json


def test_financial_transaction_data_json():
    assert financial_transaction_data_json() == []
