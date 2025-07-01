import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Функция находит операции в списке банковских операций по заданной строке"""

    try:
        result = []
        for operation in data:
            if search:
                if re.search(search, operation["description"]):
                    result.append(operation)
                else:
                    continue
        return result
    except:
        return []


def process_bank_operations(data:list[dict], categories:list)->dict:
    """Функция принимает список словарей банковских операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""

    try:
        list_operations = [operation["description"] for operation in data if operation["description"] in categories]
        count_operations = Counter(list_operations)
        return count_operations
    except:
        return {}
