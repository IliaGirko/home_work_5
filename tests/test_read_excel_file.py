from unittest.mock import patch

import pytest

from src.read_excel_file import read_excel_file


def test_read_excel_file_TypeError():
    with pytest.raises(TypeError):
        assert read_excel_file()


# @patch("src.read_csv_file.pd.read_excel")
# def test_read_excel_file_mock(mock_get):
#     mock_get.return_value.to_json.return_value = {"hi": "hello"}
#     assert read_excel_file("hello") == {"hi": "hello"}


def test_read_excel_file():
    assert read_excel_file("../transactions_excel.xlsx") is not None
