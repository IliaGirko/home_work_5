import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "number_card, conclusion",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Classic 7000792289606362", "Visa Classic 7000 79** **** 6362"),
        ("Visa Gold 7000792289606352", "Visa Gold 7000 79** **** 6352"),
    ],
)
def test_get_mask_card_number(number_card, conclusion):
    assert get_mask_card_number(number_card) == conclusion


def test_type_get_mask_card_number() -> None:
    with pytest.raises(AttributeError):
        assert get_mask_card_number(["ghgjh", 4, "km"])
