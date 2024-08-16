# number_user_card: str = input("Введите номер карты или счета ")
correct_card_names: list[str] = [
    "Visa Classic",
    "Visa Platinum",
    "Visa Gold",
    "Maestro",
    "MasterCard",
]


def get_mask_card_number(full_number_card: str) -> str | None:
    """Функция, которая маскирует 6 цифр номера карты"""
    list_split_number_card_and_name: list[str] = full_number_card.split()
    list_word_name_card: list = []
    list_numbers_name_card: list = []
    for number_or_word in list_split_number_card_and_name:
        if number_or_word.isdigit() == True:
            list_numbers_name_card.append(number_or_word)
        else:
            list_word_name_card.append(number_or_word)
    str_word_name_card: str = " ".join(list_word_name_card)
    str_number_card: str = "".join(list_numbers_name_card)
    for examination in correct_card_names:
        if str_word_name_card in examination and len(str_number_card) == 16:
            return (
                f"{str_word_name_card} {full_number_card[-16:-12]} "
                f"{full_number_card[-12:-10]}{"*" * 2} {"*" * 4} {full_number_card[-4:]}"
            )
        else:
            continue
    return "Введен не корректный формат платежной системы карты или ее номер"


def get_mask_account(full_number_card: str) -> str | None:
    """Функция, которая оставляет только 4 последние цифры карты и 2 звездочки перед ними"""
    list_split_number_card_and_name = full_number_card.split()
    list_word_name_card: list = []
    list_numbers_name_card: list = []
    for number_or_word in list_split_number_card_and_name:
        if number_or_word.isdigit() == True:
            list_numbers_name_card.append(number_or_word)
        else:
            list_word_name_card.append(number_or_word)
    str_word_name_card: str = " ".join(list_word_name_card)
    str_number_card: str = "".join(list_numbers_name_card)
    if "Счет" == str_word_name_card and len(str_number_card) == 20:
        return f"{full_number_card[:4]} {"*" * 2}{full_number_card[-4:]}"
    else:
        return "Введено не корректное название или номер счета"
