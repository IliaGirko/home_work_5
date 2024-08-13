import pytest

from src.generators import transaction_descriptions, transactions


def test_transaction_descriptions():
    run_test = transaction_descriptions(transactions)
    assert next(run_test) == "Перевод организации"

    assert next(run_test) == "Перевод со счета на счет"

    assert next(run_test) == "Перевод со счета на счет"

    assert next(run_test) == "Перевод с карты на карту"

    assert next(run_test) == "Перевод организации"

    with pytest.raises(StopIteration):
        next(run_test)


def test_transaction_descriptions_zero_transactions():
    run_test = transaction_descriptions(transaction=[])
    with pytest.raises(StopIteration):
        next(run_test)
