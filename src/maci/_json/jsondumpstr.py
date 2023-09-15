# jsondumpstr
#########################################################################################################
# Imports
import json as _json
from typing import Union as _Union
from ..error import JsonDumpStr

#########################################################################################################
# Export json str
def jsondumpstr(data: _Union[dict, list, tuple, str, int, float, bool, None], *, indent_level: int=4) -> str:
    """
    Dumps json data to a str from python data

    Returns a json formatted str

    [Example: Usage]

    jsondumpstr(data)

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_data = "Only dict|list|tuple|str|int|float|bool|None is allowed for 'data'"
    err_msg_type_indent = "Only int is allowed for 'indent_level'"

    if not isinstance(data, (list, dict, tuple, str, int, float, bool, type(None))): raise JsonDumpStr(err_msg_type_data, f'\nGot: {repr(data)}')
    if not isinstance(indent_level, int): raise JsonDumpStr(err_msg_type_indent, f'\nGot: {repr(indent_level)}')

    try:
        # Export dict data to json string
        return _json.dumps(data, indent=indent_level)
    except TypeError as __err_msg: raise JsonDumpStr(__err_msg, f'\nGot: {data} \nINDENT_LEVEL: {indent_level}')
