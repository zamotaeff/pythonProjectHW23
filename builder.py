from typing import List, Optional

from constants import FILE_NAME, CMD_TO_FUNCTION


def build_query(cmd: str, param: str, data: Optional[List[str]]) -> List[str]:
    """Функция создания запроса."""
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data: List[str] = list(map(lambda x: x.strip(), file))
    else:
        prepared_data = data

    return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)
