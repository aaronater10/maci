# jsondump
#########################################################################################################
# Imports
import json as _json
from .._native.dumpraw import dumpraw as _dumpraw
from typing import Union as _Union
from ..error import JsonDump

#########################################################################################################
# Export json file
def jsondump(
    filename: str,
    data: _Union[dict, list, tuple, str, int, float, bool, None],
    *,
    append: bool=False,
    indent_level: int=4,
    encoding: _Union[str, None]=None
) -> None:
    """
    Exports a new file from python data type to json data.
    
    Enter new filename as str. Pass data for output to file
    
    [Example Use]

    jsondump('path/to/filename.json', data)    

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    """
    # Error Checks
    err_msg_file_type = "Only str is allowed for 'filename'"
    err_msg_parser = "Only dict|list|tuple|str|int|float|bool|None is allowed for 'data'"
    err_msg_type_append = "Only bool is allowed for 'append'"
    err_msg_type_indent = "Only int is allowed for 'indent_level'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise JsonDump(err_msg_file_type, f'\nGot: {repr(filename)}')
    if not isinstance(data, (list, dict, tuple, str, int, float, bool, type(None))): raise JsonDump(err_msg_parser, f'\nGot: {repr(data)}')
    if not isinstance(append, bool): raise JsonDump(err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(indent_level, int): raise JsonDump(err_msg_type_indent, f'\nGot: {repr(indent_level)}')
    if not isinstance(encoding, (str, type(None))): raise JsonDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    try:
        # Export data to json file
        with open(filename, write_mode, encoding=encoding) as f:
            _json.dump(data, f, indent=indent_level)
            if write_mode == 'a': _dumpraw(filename, '', append=True)
    except TypeError as __err_msg: raise JsonDump(__err_msg, f'\nGot: {repr(data)}')
    except (FileNotFoundError, OSError) as __err_msg: raise JsonDump(__err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise JsonDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
