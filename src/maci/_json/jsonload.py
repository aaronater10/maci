# jsonload
#########################################################################################################
# Imports
import json as _json
from typing import Union as _Union
from pathlib import Path as _PathObj
from ..error import JsonLoad

#########################################################################################################
# Import json file
def jsonload(filename: _Union[str, _PathObj], *, encoding: _Union[str, None]=None) -> _Union[list, dict, str, int, float, bool, None]:
    """
    Loads json data from a file

    Returns data with matching python data type

    [Example: Usage]

    jsonload('path/to/filename.json')

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_file_type = "Only str is allowed for 'filename'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, (str, _PathObj)): raise JsonLoad(err_msg_file_type, f'\nGot: {repr(filename)}')
    if not isinstance(encoding, (str, type(None))): raise JsonLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Import json file
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return _json.load(f)
    except (FileNotFoundError, OSError) as __err_msg: raise JsonLoad(__err_msg, f'\nGot: {repr(filename)}')
    except _json.decoder.JSONDecodeError as __err_msg: raise JsonLoad(__err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise JsonLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
