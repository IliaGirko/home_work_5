from unittest.mock import patch

from src.external_api import currency_conversion


def test_currency_conversion():
    assert (
        currency_conversion([{"operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}}])
        == 31957.58
    )


@patch("requests.get")
def test_currency_conversion_mock(mock_get):
    mock_get.return_value.json.return_value = {"result": 2851298.27}
    assert (
        currency_conversion([{"operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}}}])
        == 2851298.27
    )


@patch("requests.get")
def test_currency_conversion_mock_eur(mock_get):
    mock_get.return_value.json.return_value = {"result": 3000000.00}
    assert (
        currency_conversion([{"operationAmount": {"amount": "31957.58", "currency": {"name": "EUR", "code": "EUR"}}}])
        == 3000000.00
    )


def test_currency_conversion_error():
    assert (
        currency_conversion([{"operation": {"amou": "31957.58", "curre": {"name": "USD", "code": "USD"}}}])
        == "Не корректная транзакция"
    )


def test_currency_conversion_err():
    assert (
        currency_conversion([{"operationAmount": {"amount": "31957.58", "currency": {"name": "EUR", "code": "sace"}}}])
        == "Не корректная валюта"
    )
