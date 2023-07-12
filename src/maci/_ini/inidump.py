# inidump
#########################################################################################################
# Imports
from configparser import ConfigParser as _ConfigParser
from typing import Union as _Union
from ..error import IniDump

#########################################################################################################
# Export ini file
def inidump(filename: str, data: _ConfigParser, *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Exports a new file from a ini data (ConfigParser) obj

    Enter new filename as str. Pass ini data for output to file
    
    [Example Use]

    inidump('path/to/filename.ini', data)

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """
    # Error Checks
    err_msg_file_type = "Only str is allowed for 'filename'"
    err_msg_parser = "Only ConfigParser is allowed for 'data'"
    err_msg_type_append = "Only bool is allowed for 'append'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise IniDump(err_msg_file_type, f'\nGot: {repr(filename)}')
    if not isinstance(data, _ConfigParser): raise IniDump(err_msg_parser, f'\nGot: {repr(data)}')
    if not isinstance(append, bool): raise IniDump(err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(encoding, (str, type(None))): raise IniDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    # Write Ini Data
    try:
        with open(filename, write_mode, encoding=encoding) as f:
            data.write(f)
    except (FileNotFoundError, OSError) as _err_msg: raise IniDump(_err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise IniDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
