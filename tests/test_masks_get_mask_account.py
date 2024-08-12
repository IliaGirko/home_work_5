import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "number_check, conclusion",
    [
        ("Счет 70007922896063222261", "Счет **2261"),
        ("Счет 70007922896063222262", "Счет **2262"),
        ("Счет 70007922896062222352", "Счет **2352"),
    ],
)
def test_get_mask_account(number_check, conclusion):
    assert get_mask_account(number_check) == conclusion


def test_type_get_mask_account() -> None:
    with pytest.raises(AttributeError):
        assert get_mask_account(["ghgjh", 4, "km"])
