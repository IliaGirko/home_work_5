from src.masks import correct_card_names, get_mask_account, get_mask_card_number

# number_user_card
# user_input_date: str = input('Введите дату в формате: "гггг-мм-ддT02:26:18.671407" ')


def mask_account_card(number_card_or_check_client: str) -> str | None:
    """Функция обрабатывающая информацию о карте и счете"""
    list_split_number_card_and_name: list[str] = number_card_or_check_client.split()
    list_word_name_card: list = []
    for number_or_word in list_split_number_card_and_name:
        if number_or_word.isdigit() == True:
            continue
        else:
            list_word_name_card.append(number_or_word)
    str_word_name_card: str = " ".join(list_word_name_card)
    if "Счет" in str_word_name_card:
        return f"{get_mask_account(number_card_or_check_client)}"
    elif str_word_name_card in correct_card_names:
        return f"{get_mask_card_number(number_card_or_check_client)}"
    else:
        return "Введен не корректный номер карты или счета"


def get_date(full_date: str) -> str:
    """Функция обрабатывающая дату и редактирующая ее"""
    if full_date == "" or len(full_date) < 11:
        return "Введена не корректная дата"
    year: int = int(full_date[:4])
    month: int = int(full_date[5:7])
    day: int = int(full_date[8:10])
    if full_date == "":
        return "Введена не корректная дата"
    elif 0 > year < 2025 or 0 > month < 13 or 0 > day < 32:
        return "Введена не корректная дата"
    else:
        return f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"


# print(mask_account_card(number_user_card))
# print(get_date(user_input_date))
