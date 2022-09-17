import functions

VALID_CMD_PARAMS = ('filter', 'sort', 'map', 'unique', 'limit', 'regex')

CMD_TO_FUNCTION = {'filter': functions.filter_query,
                   'map': functions.map_query,
                   'unique': functions.unique_query,
                   'sort': functions.sort_query,
                   'limit': functions.limit_query}

FILE_NAME = 'data/apache_logs.txt'
