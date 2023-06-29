# iniload
#########################################################################################################
# Imports
from typing import Union as _Union
from configparser import ConfigParser as _ConfigParser
from configparser import ExtendedInterpolation as _ExtendedInterpolation
from ..error import IniLoad

#########################################################################################################
# Import ini file
def iniload(filename: str, *, encoding: _Union[str, None]=None) -> _ConfigParser:
    """
    Imports ini data from a file.

    Returns a ConfigParser obj. Assign the output to var

    Enter ini file location as str to import.

    [Example Use]

    iniload('path/to/filename.ini')

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """
    # Error Checks
    err_msg_file_type = "Only str is allowed for 'filename'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise IniLoad(err_msg_file_type, f'\nGot: {repr(filename)}')
    if not isinstance(encoding, (str, type(None))): raise IniLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Load file data
    try:
        with open(filename, 'r', encoding=encoding): pass
    except (FileNotFoundError, OSError) as _err_msg: raise IniLoad(_err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise IniLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    _parser = _ConfigParser(interpolation=_ExtendedInterpolation())
    _parser.read(filename, encoding=encoding)
    return _parser
