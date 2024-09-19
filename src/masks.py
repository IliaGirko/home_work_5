import logging

logger = logging.getLogger("masks.py")
logger.setLevel(logging.DEBUG)
logger_handler = logging.FileHandler("logs/masks.log", "w")
logger_formatter = logging.Formatter(
    "Time: %(asctime)s Module name: %(name)s Level message: %(levelname)s Message: %(message)s"
)
logger_handler.setFormatter(logger_formatter)
logger.addHandler(logger_handler)


# number_user_card: str = input("Введите номер карты или счета ")
# Параметр для вызова функций, перед запуском раскомментировать
correct_card_names: list[str] = [
    "Visa Classic",
    "Visa Platinum",
    "Visa Gold",
    "Visa",
    "Maestro",
    "MasterCard",
    "Mastercard",
    "МИР",
    "Discover",
    "American Express",
]


def get_mask_card_number(full_number_card: str) -> str:
    """Функция, которая маскирует 6 цифр номера карты"""
    logger.info("Запуск функции get_mask_card_number")
    logger.info("Разделяем введенный номер карты на название и номер")
    list_split_number_card_and_name: list[str] = full_number_card.split()
    list_word_name_card: list = []
    list_numbers_name_card: list = []
    for number_or_word in list_split_number_card_and_name:
        if number_or_word.isdigit():
            list_numbers_name_card.append(number_or_word)
        else:
            list_word_name_card.append(number_or_word)
    str_word_name_card: str = " ".join(list_word_name_card)
    str_number_card: str = "".join(list_numbers_name_card)
    logger.info("Проверяем корректность введеного номера карты и платежной системы карты")
    for examination in correct_card_names:
        if str_word_name_card in examination and len(str_number_card) == 16:
            logger.info("Завешение работы функции get_mask_card_number")
            return (
                f"{str_word_name_card} {full_number_card[-16:-12]} "
                f"{full_number_card[-12:-10]}{"*" * 2} {"*" * 4} {full_number_card[-4:]}"
            )
        else:
            logger.error("Введен не корректный формат платежной системы карты или ее номер")
            continue
    return "Введен не корректный формат платежной системы карты или ее номер"


def get_mask_account(full_number_card: str) -> str | None:
    """Функция, которая оставляет только 4 последние цифры карты и 2 звездочки перед ними"""
    logger.info("Запуск функции get_mask_account")
    list_split_number_card_and_name = full_number_card.split()
    list_word_name_card: list = []
    list_numbers_name_card: list = []
    logger.info("Разделяем введенный номер карты и название")
    for number_or_word in list_split_number_card_and_name:
        if number_or_word.isdigit():
            list_numbers_name_card.append(number_or_word)
        else:
            list_word_name_card.append(number_or_word)
    str_word_name_card: str = " ".join(list_word_name_card)
    str_number_card: str = "".join(list_numbers_name_card)
    logger.info("Проверяем корректность введенных данных")
    if "Счет" == str_word_name_card and len(str_number_card) == 20:
        logger.info("Завершение работы функции get_mask_account")
        return f"{full_number_card[:4]} {"*" * 2}{full_number_card[-4:]}"
    else:
        logger.error("Введено не корректное название или номер счета")
        return "Введено не корректное название или номер счета"
