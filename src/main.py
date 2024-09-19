import os.path
from typing import Any

from read_csv_file import read_csv_file
from read_excel_file import read_excel_file
from search_operation import (
    counting_quantity,
    filter_by_category,
    func_filter_currency_excel_and_csv_files,
    func_filter_currency_json,
    func_output_result,
    func_sorted_by_date,
    search_by_state,
)
from utils import financial_transaction_data_json


def start_of_the_program():
    """Запуск осносной логиги программы банковского приложения"""
    entrance_in_menu: int = 0

    while entrance_in_menu != 1:
        print(
            "Привет! Добро пожаловать в программу работы "
            "\nс банковскими транзакциями. "
            "\nВыберите необходимый пункт меню:"
        )
        print(
            "1. Получить информацию о транзакциях из JSON-файла"
            "\n2. Получить информацию о транзакциях из CSV-файла"
            "\n3. Получить информацию о транзакциях из XLSX-файла"
        )
        input_file: str = input("Введите 1, 2 или 3: ")
        try:
            if input_file:
                input_file_type = int(input_file)
            else:
                continue
        except ValueError:
            continue
        if input_file_type == 1:
            entrance_in_menu += 1
            print("Для обработки выбран JSON-файл.")
            file_in_format_json = financial_transaction_data_json(os.path.join("data", "operations.json"))
            menu_status: int = 0

            while menu_status != 1:
                print(
                    "Введите статус, по которому необходимо выполнить фильтрацию."
                    "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
                )
                selection_of_operation_status: str = input().upper()
                if selection_of_operation_status == "EXECUTED":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        file_in_format_json, selection_of_operation_status
                    )
                elif selection_of_operation_status == "CANCELED":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        file_in_format_json, selection_of_operation_status
                    )
                elif selection_of_operation_status == "PENDING":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        file_in_format_json, selection_of_operation_status
                    )

        elif input_file_type == 2:
            entrance_in_menu += 1
            print("Для обработки выбран CSV-файл.")
            csv_file_in_format_json: list[dict[Any]] = read_csv_file(os.path.join("transactions.csv"))
            menu_status: int = 0
            while menu_status != 1:
                print(
                    "Введите статус, по которому необходимо выполнить фильтрацию."
                    "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
                )
                selection_of_operation_status: str = input().upper()
                if selection_of_operation_status == "EXECUTED":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        csv_file_in_format_json, selection_of_operation_status
                    )
                elif selection_of_operation_status == "CANCELED":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        csv_file_in_format_json, selection_of_operation_status
                    )
                elif selection_of_operation_status == "PENDING":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        csv_file_in_format_json, selection_of_operation_status
                    )

        elif input_file_type == 3:
            entrance_in_menu += 1
            print("Для обработки выбран CSV-файл.")
            excel_file_in_format_json: list[dict[Any]] = read_excel_file(os.path.join("transactions_excel.xlsx"))
            menu_status: int = 0
            while menu_status != 1:
                print(
                    "Введите статус, по которому необходимо выполнить фильтрацию."
                    "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
                )
                selection_of_operation_status: str = input().upper()
                if selection_of_operation_status == "EXECUTED":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        excel_file_in_format_json, selection_of_operation_status
                    )
                elif selection_of_operation_status == "CANCELED":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        excel_file_in_format_json, selection_of_operation_status
                    )
                elif selection_of_operation_status == "PENDING":
                    menu_status += 1
                    sorting_data_by_status: list[dict[Any]] = search_by_state(
                        excel_file_in_format_json, selection_of_operation_status
                    )
        else:
            print("Введен не корректный номер из пункта меню")

    filter_date: int = 0
    while filter_date != 1:
        print("Отсортировать операции по дате? Да/Нет")
        sort_by_date: str = input().title()
        if sort_by_date == "Да":
            filter_date += 1
            choice: int = 0
            while choice != 1:
                print("Отсортировать по возрастанию или по убыванию?")
                choice_of_increasing_or_decreasing: str = input().lower()
                if choice_of_increasing_or_decreasing == "по возрастанию":
                    choice += 1
                    flag_revers: bool = False
                    result_sorted_date: list[dict[Any]] = func_sorted_by_date(sorting_data_by_status, flag_revers)
                elif choice_of_increasing_or_decreasing == "по убыванию":
                    choice += 1
                    flag_revers: bool = True
                    result_sorted_date: list[dict[Any]] = func_sorted_by_date(sorting_data_by_status, flag_revers)
        elif sort_by_date == "Нет":
            filter_date += 1
            result_sorted_date: list[dict[Any]] = sorting_data_by_status

    filter_currency: int = 0
    while filter_currency != 1:
        print("Выводить только рублевые тразакции? Да/Нет")
        input_sort_currency: str = input().title()
        if input_sort_currency == "Да":
            if input_file_type == 1:
                filter_currency += 1
                code: str = "RUB"
                result_filter_by_currency: list[dict[Any]] = func_filter_currency_json(result_sorted_date, code)
            else:
                filter_currency += 1
                code: str = "RUB"
                result_filter_by_currency: list[dict[Any]] = func_filter_currency_excel_and_csv_files(
                    result_sorted_date, code
                )
        elif input_sort_currency == "Нет":
            filter_currency += 1
            result_filter_by_currency: list[dict[Any]] = result_sorted_date

    filter_word: int = 0
    while filter_word != 1:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        sort_by_word: str = input().title()
        if sort_by_word == "Да":
            filter_word += 1
            input_word_for_filtering: str = input("Введите слово для поиска: ")
            result: list[dict[Any]] = filter_by_category(result_filter_by_currency, input_word_for_filtering)
            dict_input_word_for_filtering: dict[str, Any] = {"key": input_word_for_filtering}
            for counting_description in sorting_data_by_status:
                counting_quantity(counting_description, dict_input_word_for_filtering)
        elif sort_by_word == "Нет":
            filter_word += 1
            result: list[dict[Any]] = result_filter_by_currency

    if result == []:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(result)}")
        end_result: dict[str, list[Any]] = func_output_result(result)
        counter: int = 0
        for dict_ in result:
            if input_file_type == 1:
                operation_amount: float = round(float(dict_.get("operationAmount").get("amount")))
                end_result["amount"].append(operation_amount)
                currency_code: str = dict_.get("operationAmount").get("currency").get("code")
                end_result["currency_code"].append(currency_code)
            else:
                amount: float = round(float(dict_.get("amount")))
                end_result["amount"].append(amount)
                currency_code: str = dict_.get("currency_code")
                end_result["currency_code"].append(currency_code)
        while len(end_result["date_operation"]) > counter:
            print(
                f"{end_result["date_operation"][counter]} {end_result["description"][counter]}"
                f"\n{end_result["card_from"][counter]} -> {end_result["card_to"][counter]}"
                f"\nСумма: {end_result["amount"][counter]} {end_result["currency_code"][counter]}\n"
            )
            counter += 1
