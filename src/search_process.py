import re


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Функция находит операции в списке банковских операций по заданной строке"""
    result = []
    for operation in data:
        if re.search(search, operation["description"]):
            result.append(operation)
        else:
            continue
    return result
