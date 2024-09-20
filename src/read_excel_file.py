import json
from typing import Any

import pandas as pd


def read_excel_file(file_path: str) -> list[dict[Any]] | str:
    """Функция читает файл в формате excel и возвращает json"""
    try:
        data_frame = pd.read_excel(file_path)
        return json.loads(data_frame.to_json(indent=4, orient="records", force_ascii=False))
    except Exception as error:
        return f"Error: {error}"
