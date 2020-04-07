from enum import Enum

token = "1191954274:AAHshq4wCr4vsTsy6W3KUl46so4X9rQe7Vc"
db_file = "database.vdb"
db_file_users = "users.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_ID = "1"
    S_ENTER_QUESTION = "2"
    