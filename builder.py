import functions
from constants import FILE_NAME, CMD_TO_FUNCTION


def build_query(cmd, param, data):
    """Функция создания запроса."""
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
