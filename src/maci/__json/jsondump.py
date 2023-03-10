# jsondump
#########################################################################################################
# Imports
import json as __json
from ..error import JsonDump
from ..__native.dumpraw import dumpraw as _dumpraw
from typing import Union

#########################################################################################################
# Export json file
def jsondump(
    filename: str,
    data: Union[str, int, float, bool, list, dict, tuple, None],
    *,
    append: bool=False,
    indent_level: int=4,
    encoding: Union[str, None]=None
) -> None:
    """
    Exports a new file from python data type to json data.
    
    Enter new filename as str. Pass data for output to file
    
    [Example Use]

    jsondump('path/to/filename.json', data)    

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    """
    __err_msg_type_str_append = "Only bool is allowed for 'append'"

    if not isinstance(append, bool): raise JsonDump(__err_msg_type_str_append, f'\nFILE: "{filename}" \nDATA: {append}')

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    try:
        # Export data to json file
        with open(filename, write_mode, encoding=encoding) as f:
            __json.dump(data, f, indent=indent_level)
            if write_mode == 'a': _dumpraw(filename, '', append=True)
    except TypeError as __err_msg: raise JsonDump(__err_msg, f'\nFILE: "{filename}" \nDATA:{data}')
    except ValueError as __err_msg: raise JsonDump(__err_msg, f'\nFILE: "{filename}" \nDATA:{data}')
    except FileNotFoundError as __err_msg: raise JsonDump(__err_msg, f'\nFILE: "{filename}"')
