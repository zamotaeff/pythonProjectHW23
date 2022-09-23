from typing import Dict, Callable, Iterable

import functions

VALID_CMD_PARAMS: Iterable[str] = ('filter', 'sort', 'map', 'unique', 'limit', 'regex')

CMD_TO_FUNCTION: Dict[str, Callable] = {'filter': functions.filter_query,
                                        'map': functions.map_query,
                                        'unique': functions.unique_query,
                                        'sort': functions.sort_query,
                                        'limit': functions.limit_query,
                                        'regex': functions.search_pic}

FILE_NAME: str = 'data/apache_logs.txt'
