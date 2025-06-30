import os

import pandas as pd
from pandas.errors import EmptyDataError


def read_csv_file(file: str) -> list[dict]:
    """Функция принимает путь к файлу csv и возвращает список словарей данных"""

    path = os.path.dirname(__file__)
    path_to_file = os.path.join(path, "..", file)

    try:
        file_data = pd.read_csv(path_to_file)
        return file_data.to_dict(orient="records")
    except FileNotFoundError:
        return []
    except EmptyDataError:
        return []
    except Exception:
        return []


def read_xlsx_file(file: str) -> list[dict]:
    """Функция принимает путь к файлу xlsx и возвращает список словарей данных"""

    path = os.path.dirname(__file__)
    path_to_file = os.path.join(path, "..", file)

    try:
        file_data = pd.read_excel(path_to_file)
        return file_data.to_dict(orient="records")
    except FileNotFoundError:
        return []
    except EmptyDataError:
        return []
    except Exception:
        return []
