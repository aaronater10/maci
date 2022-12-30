# jsondumpstr
#########################################################################################################
# Imports
import json as __json
from ..error import JsonDumpStr
from typing import Union

#########################################################################################################
# Export json str
def jsondumpstr(data: Union[str, int, float, bool, list, dict, tuple, None], indent_level: int=4) -> str:
    """
    Exports python data type to json string

    Returns a json formatted str. Assign the output to var

    [Example Use]

    jsondumpstr(data, [optional] indent_level)

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    
    """
    try:
        # Export dict data to json string
        return __json.dumps(data, indent=indent_level)
    except TypeError as __err_msg: raise JsonDumpStr(__err_msg, f'\nDATA: {data} \nINDENT_LEVEL: {indent_level}')
    except ValueError as __err_msg: raise JsonDumpStr(__err_msg, f'\nDATA: {data} \nINDENT_LEVEL: {indent_level}')

