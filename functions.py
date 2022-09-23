import re
from typing import List, Any


def filter_query(param: str, data: List[str]) -> List[str]:
    """Функция фильтрации данных."""
    return list(filter(lambda x: param in x, data))


def map_query(param: str, data: List[str]) -> List[str]:
    """Функция получает номер колонки и выводит списком данные этой колонки."""
    col_number: int = int(param)
    return list(map(lambda x: x.split(' ')[col_number], data))


def unique_query(data: List[str], *args: Any, **kwargs: Any) -> List[str]:
    """Функция создает список из уникальных позиций."""
    return list(set(data))


def sort_query(param: str, data: List[str]) -> List[str]:
    """ Функция сортировки данных."""
    reverse: bool = False if param == 'asc' else True
    return sorted(data, reverse=reverse)


def limit_query(param: str, data: List[str]) -> List[str]:
    """Функция создает список позиций в заданном количестве."""
    limit: int = int(param)
    return list(data)[:limit]


def search_pic(param: str, data: List[str]) -> List[str]:
    """Поиск по регулярному выражению"""
    pattern: re.Pattern = re.compile(param)
    return list(filter(lambda y: pattern.search(y), data))
