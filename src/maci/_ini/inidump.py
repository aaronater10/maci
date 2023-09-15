# inidump
#########################################################################################################
# Imports
from configparser import ConfigParser as _ConfigParser
from typing import Union as _Union
from pathlib import Path as _PathObj
from ..error import IniDump

#########################################################################################################
# Export ini file
def inidump(filename: _Union[str, _PathObj], data: _ConfigParser, *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Dumps ini data to a file from a ConfigParser object

    [Example: Usage]

    inidump('path/to/filename.ini', data)

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_file_type = "Only str is allowed for 'filename'"
    err_msg_parser = "Only ConfigParser is allowed for 'data'"
    err_msg_type_append = "Only bool is allowed for 'append'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, (str, _PathObj)): raise IniDump(err_msg_file_type, f'\nGot: {repr(filename)}')
    if not isinstance(data, _ConfigParser): raise IniDump(err_msg_parser, f'\nGot: {repr(data)}')
    if not isinstance(append, bool): raise IniDump(err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(encoding, (str, type(None))): raise IniDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    # Write Ini Data
    try:
        with open(filename, write_mode, encoding=encoding) as f:
            data.write(f)
    except (FileNotFoundError, OSError) as _err_msg: raise IniDump(_err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise IniDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
