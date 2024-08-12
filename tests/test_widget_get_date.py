import pytest

from src.widget import get_date


@pytest.mark.parametrize(
    "date, conclusion",
    [
        ("2011-11-20T02:26:18.671407", "20.11.2011"),
        ("2012-11-20T02:26:18.671407", "20.11.2012"),
        ("2013-11-20T02:26:18.671407", "20.11.2013"),
    ],
)
def test_get_date(date, conclusion):
    assert get_date(date) == conclusion


def test_type_get_date() -> None:
    with pytest.raises(TypeError):
        assert get_date(4)
