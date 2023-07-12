# loadraw
#########################################################################################################
# Imports
from typing import Union as _Union
from os import path as _path
from ..error import LoadRaw

#########################################################################################################
# Import raw data from file
def loadraw(filename: str, *, byte_data: bool=False, encoding: _Union[str, None]=None) -> _Union[str, bytes]:
    """
    Imports any raw data from a file.

    Returns a str. Assign the output to var

    [Options]
    byte_data: Set to True if importing byte data

    [Example Use]

    loadraw('path/to/filename')
    """
    # Error Checks
    err_msg_type_filename = "Only str is allowed for 'filename'"
    err_msg_type_byte_data = "Only bool is allowed for 'byte_data'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise LoadRaw(err_msg_type_filename, f'\nGot: {repr(filename)}')
    if not isinstance(byte_data, bool): raise LoadRaw(err_msg_type_byte_data, f'\nGot: {repr(byte_data)}')
    if not isinstance(encoding, (str, type(None))): raise LoadRaw(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Validate file exists. Import File then return the raw data
    if not byte_data:
        try:
            with open(filename, 'r', encoding=encoding) as f:
                if _path.getsize(filename) == 0:
                    return ''
                return f.read()
        except (FileNotFoundError, OSError) as __err_msg: raise LoadRaw(__err_msg, f'\nGot: {repr(filename)}')
        except LookupError: raise LoadRaw(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
    
    if byte_data: # pragma: no branch
        try:
            with open(filename, 'rb') as f:
                if _path.getsize(filename) == 0:
                    return b''
                return f.read()
        except (FileNotFoundError, OSError) as __err_msg: raise LoadRaw(__err_msg, f'\nGot: {repr(filename)}')
