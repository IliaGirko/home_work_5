from unittest.mock import patch

import pytest

from src.read_csv_file import read_csv_file


def test_read_csv_file_TypeError():
    with pytest.raises(TypeError):
        assert read_csv_file()


# @patch("src.read_csv_file.pd.read_csv")
# def test_read_csv_file_mock(mock_get):
#     mock_get.return_value.to_json.return_value = {"hi": "hello"}
#     assert read_csv_file("hello") == {"hi": "hello"}


def test_read_csv_file():
    assert read_csv_file("../transactions.csv") is not None
