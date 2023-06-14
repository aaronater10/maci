# dumpraw
#########################################################################################################
# Imports
from typing import Any as __Any
from typing import Union as __Union
from os import path as __path
from ..error import DumpRaw

#########################################################################################################
# Export Data to File
def dumpraw(filename: str, *data: __Any, append: bool=False, byte_data: bool=False, encoding: __Union[str, None]=None):
    """
    Exports a new file with the new data.
    
    Enter new filename as str, Pass any data type for output to file.

    [Options]
    append: set to True to append data to a file (Default=False, which writes a new file each time)

    byte_data: Set to True to write byte data. Default False

    [Example Use]
    Normal: dump('path/of/filename', 'data')

    Byte Data: dump('path/of/filename', b'data', byte_data=True)
    """
    # Error Checks
    __err_msg_bytes = "Only bytes is allowed if using 'byte_data' option"
    __err_msg_type_bytes = "Only bool is allowed for 'byte_data'"
    __err_msg_type_str = "Only str is allowed for 'filename'"
    __err_msg_append = "Only bool is allowed for 'append'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(byte_data, bool): raise DumpRaw(__err_msg_type_bytes, f'\nGot: {repr(byte_data)}')
    if not isinstance(filename, str): raise DumpRaw(__err_msg_type_str, f'\nGot: {repr(filename)}')
    if (not isinstance(append, bool)): raise DumpRaw(__err_msg_append, f'\nGot: {repr(append)}')
    if (not isinstance(encoding, (str, type(None)))): raise DumpRaw(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Set Write Mode: 'a' = append, 'w' = write
    mode = 'a' if append else 'w'

    ### Export data ###

    ### New File ###
    # Raw Data to File
    if (mode == 'w') and (not byte_data):
        try:
            with open(filename, 'w', encoding=encoding) as f:
                for data_to_write in data:
                    f.writelines(str(data_to_write))
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nGot: {repr(filename)}')
        except LookupError: raise DumpRaw(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
    
    # Byte Data Converted to File
    if (mode == 'w') and (byte_data):
        for data_to_write in data:
            if not isinstance(data_to_write, bytes): raise DumpRaw(__err_msg_bytes, f'\nGot: {repr(data_to_write)}')
        try:
            with open(filename, 'wb') as f:
                for data_to_write in data:
                    f.write(data_to_write)
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nGot: {repr(filename)}')

    
    ### Append File ###
    __new_line = '\n'

    # Raw Data to File
    if (mode == 'a') and (not byte_data):
        # Check if file empty. Throws error if file not found
        try: 
            if __path.getsize(filename) == 0: __new_line = ''
            with open(filename, 'a', encoding=encoding) as f:
                for data_to_write in data:
                    f.writelines(f"{__new_line}{data_to_write}")
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nGot: {repr(filename)}')
        except LookupError: raise DumpRaw(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Byte Data to File
    if (mode == 'a') and (byte_data):
        for data_to_write in data:
            if not isinstance(data_to_write, bytes): raise DumpRaw(__err_msg_bytes, f'\nGot: {repr(data_to_write)}')
        # Check if file empty. Throws error if file not found
        try: 
            if __path.getsize(filename) == 0: __new_line = b''
            with open(filename, 'ab') as f:
                for data_to_write in data:
                    f.write(b"\n")
                    f.write(data_to_write)
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nGot: {repr(filename)}')
