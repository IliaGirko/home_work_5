from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор который автоматически регистрирует детали выполнения функций, такие как время вызова,
    имя функции, передаваемые аргументы, результат выполнения и информацию об ошибках"""

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_start: float = time()
            message_start: str = f"Start of function execution {time_start}\n"
            try:
                result: Callable = func(*args, **kwargs)
                log_message: str = f"{func.__name__} ok"
            except Exception as type_error:
                log_message: str = f"{func.__name__} error: {type_error.__class__.__name__}. Inputs: {args}, {kwargs}"
            time_end: float = time()
            message_end: str = f"\nЕnd of function execution {time_end}"
            if filename != None:
                with open(filename, "a", encoding="UTF-8") as file:
                    file.write(f"{message_start}{log_message}{message_end}")
            else:
                return print(f"{message_start}{log_message}{message_end}")
            return result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x: int | float, y: int | float) -> int | float:
    """Функция проверки"""
    return x + y


my_function(2.2, 3)
