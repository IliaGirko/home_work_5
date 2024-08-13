import random

import pytest

from src.generators import card_number_generator


def test_card_number_generator():
    run_test = card_number_generator(1, 9)
    assert next(run_test) != f"0000 0000 0000 000{random.randint(1, 9)}"


def test_card_number_generator_negative_value():
    run_test = card_number_generator(1, -9)
    with pytest.raises(StopIteration):
        assert next(run_test)
