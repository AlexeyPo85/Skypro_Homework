import math
import re

from src.processing import filter_by_state, sort_by_date
from src.read_csv_xlsx_file import read_csv_file, read_xlsx_file
from src.utils import get_list_transactions
from src.widget import get_date, mask_account_card


def main():
    """Основная функция виджета банковских операций.
    Функция считывает операции из указанного файла и
    выводит список операций по значениям, указанным пользователем."""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    list_of_transactions = []
    list_file_type = ["1", "2", "3"]
    list_filtered_by_state = []
    list_filtered_by_date = []
    list_filtered_by_currency = []
    result_list = []

    file_type = input("""Выберите необходимый пункт меню:
                    1. Получить информацию о транзакциях из JSON-файла
                    2. Получить информацию о транзакциях из CSV-файла
                    3. Получить информацию о транзакциях из XLSX-файла
                    \n""")

    while file_type not in list_file_type:
        print("Неверно введёно значение")
        file_type = input("""Выберите необходимый пункт меню:
                            1. Получить информацию о транзакциях из JSON-файла
                            2. Получить информацию о транзакциях из CSV-файла
                            3. Получить информацию о транзакциях из XLSX-файла
                            \n""")
    if file_type == "1":
        list_of_transactions = get_list_transactions("operations.json")
        print("\nДля обработки выбран JSON-файл.\n")
    elif file_type == "2":
        list_of_transactions = read_csv_file("transactions.csv")
        print("\nДля обработки выбран CSV-файл.\n")
    elif file_type == "3":
        list_of_transactions = read_xlsx_file("transactions_excel.xlsx")
        print("\nДля обработки выбран XLSX-файл.\n")

    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    filter_status = input("""Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    \n""").upper()
    list_filter_status = ["EXECUTED", "CANCELED", "PENDING"]
    while filter_status not in list_filter_status:
        print(f"\nСтатус операции '{filter_status}' недоступен.\n")
        filter_status = input("""Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
    \n""").upper()
    list_filtered_by_state = filter_by_state(list_of_transactions, filter_status)
    print(f"\nОперации отфильтрованы по статусу {filter_status}\n")

    sorting_by_date = input("""Отсортировать операции по дате? Да/Нет
    \n""").lower()
    if sorting_by_date == "да":
        list_filtered_by_date = sort_by_date(list_filtered_by_state)
    else:
        list_filtered_by_date = list_filtered_by_state

    currency_code = input("""\nВыводить только рублевые транзакции? Да/Нет
    \n""").lower()
    if currency_code == "да":
        if file_type == "1":
            list_filtered_by_currency = [operation for operation in list_filtered_by_date
                                         if operation.get("operationAmount").get("currency").get("code") == "RUB"]
        elif file_type == "2":
            list_filtered_by_currency = [operation for operation in list_filtered_by_date
                                         if operation.get("currency_code") == "RUB"]
        elif file_type == "3":
            list_filtered_by_currency = [operation for operation in list_filtered_by_date
                                         if operation.get("currency_code") == "RUB"]
    else:
        list_filtered_by_currency = list_filtered_by_state

    filter_by_description = input("""\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет
    \n""").lower()
    if filter_by_description == "да":
        pattern = input("""\nВведите слово
        \n""").lower()
        for operation in list_filtered_by_currency:
            if re.search(pattern, operation["description"].lower()):
                result_list.append(operation)
    else:
        result_list = list_filtered_by_currency

    if result_list:

        print("\nРаспечатываю итоговый список транзакций...\n")

        print(f"Всего банковских операций в выборке: {len(result_list)}\n")
        if file_type == "1":
            for operation in result_list:
                print(f"{get_date(operation['date'])} {operation['description']}")
                if "from" in operation:
                    print(f"{" ".join(operation['from'].split()[:-1])} {mask_account_card(operation['from'])}"
                          f" -> {" ".join(operation['to'].split()[:-1])} {mask_account_card(operation['to'])}")
                else:
                    print(f"{" ".join(operation['to'].split()[:-1])} {mask_account_card(operation['to'])}")
                print(f"Сумма: {operation['operationAmount']['amount']} "
                        f"{operation['operationAmount']['currency']['name']}\n")
        else:
            for operation in result_list:
                print(f"{get_date(operation['date'])} {operation['description']}")
                if operation["from"]:
                    print(f"{" ".join(operation['from'].split()[:-1])} {mask_account_card(operation['from'])}"
                          f" -> {" ".join(operation['to'].split()[:-1])} {mask_account_card(operation['to'])}")
                else:
                    print(f"{" ".join(operation['to'].split()[:-1])} {mask_account_card(operation['to'])}")
                print(f"Сумма: {operation['amount']} "
                      f"{operation['currency_name']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
