import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "number_card_or_check, conclusion",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Classic 7000792289606362", "Visa Classic 7000 79** **** 6362"),
        ("Visa Gold 7000792289606352", "Visa Gold 7000 79** **** 6352"),
        ("Счет 70007922896063222261", "Счет **2261"),
        ("Счет 70007922896063222262", "Счет **2262"),
        ("Счет 70007922896062222352", "Счет **2352"),
    ],
)
def test_mask_account_card(number_card_or_check: str, conclusion: str):
    assert mask_account_card(number_card_or_check) == conclusion


def test_type_mask_account_card() -> None:
    with pytest.raises(AttributeError):
        assert mask_account_card(number_card_or_check_client=["ghgjh", 4, "km"])
