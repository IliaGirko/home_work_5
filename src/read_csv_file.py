from typing import Any

import pandas as pd


def read_csv_file(file_path: str) -> list[dict[Any]] | str:
    """Функция читает файл в формате сsv и возвращает json"""
    try:
        data_frame = pd.read_csv(file_path, delimiter=";")
        return data_frame.to_json(indent=4, orient="records", force_ascii=False)
    except Exception as error:
        return f"Error: {error}"
