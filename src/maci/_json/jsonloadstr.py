# jsonloadstr
#########################################################################################################
# Imports
import json as _json
from typing import Union as _Union
from ..error import JsonLoadStr

#########################################################################################################
# Import json string
def jsonloadstr(json_str_data: str) -> _Union[list, dict, str, int, float, bool, None]:
    """
    Imports json data from a string

    Returns data with matching python data type. Assign the output to var

    Enter json string as str to import.

    [Example Use]

    jsonloadstr('string with json data')

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    """
    # Error Checks
    err_msg_data_type = "Only str is allowed for 'json_str_data'"

    if not isinstance(json_str_data, str): raise JsonLoadStr(err_msg_data_type, f'\nGot: {repr(json_str_data)}')

    # Import json string    
    try:
        return _json.loads(json_str_data)
    except _json.decoder.JSONDecodeError as __err_msg: raise JsonLoadStr(__err_msg, f'\nGot: {json_str_data}')
