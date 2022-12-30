# dumpraw
#########################################################################################################
# Imports
from typing import Any as __Any
from os import path as __path
from ..error import DumpRaw

#########################################################################################################
# Export Data to File
def dumpraw(filename: str, *data: __Any, mode: str='w', byte_data: bool=False):
    """
    Exports a new file with the new data.
    
    Enter new filename as str, Pass any data type for output to file.

    [Options]
    mode: Set to 'a' to append data to file instead. Default is 'w'
    byte_data: Set to True to write byte data. Default False

    [Example Use]
    Normal: dump('path/of/filename', 'data')

    Byte Data: dump('path/of/filename', b'data', byte_data=True)
    """
    # Error Checks
    __err_msg_bytes = "Only bytes is allowed if using 'byte_data' option"
    __err_msg_type_bytes = "Only bool is allowed for 'byte_data'"
    __err_msg_type_str = "Only str is allowed for 'filename'"
    __err_msg_mode = "Only str is allowed for 'mode' option, and must be 'w' or 'a'"

    if not isinstance(byte_data, bool): raise DumpRaw(__err_msg_type_bytes, f'\nDATA: {byte_data}')
    if not isinstance(filename, str): raise DumpRaw(__err_msg_type_str, f'\nFILE: "{filename}"')
    if (not isinstance(mode, str)) or not (mode in ['w', 'a']): 
        raise DumpRaw(__err_msg_mode, f'\nDATA: "{mode}"')

    # Export data 

    ### New File ###
    # Raw Data to File
    if (mode == 'w') and (not byte_data):
        try:
            with open(filename, 'w') as f:
                for data_to_write in data:
                    f.writelines(str(data_to_write))
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nFILE: "{filename}"')
    
    # Byte Data Converted to File
    if (mode == 'w') and (byte_data):
        for data_to_write in data:
            if not isinstance(data_to_write, bytes): raise DumpRaw(__err_msg_bytes, f'\nDATA: "{data_to_write}"')
        try:
            with open(filename, 'wb') as f:
                for data_to_write in data:
                    f.write(data_to_write)
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nFILE: "{filename}"')

    
    ### Append File ###
    __new_line = '\n'

    # Raw Data to File
    if (mode == 'a') and (not byte_data):
        # Check if file empty. Throws error if file not found
        try: 
            if __path.getsize(filename) == 0: __new_line = ''
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nFILE: "{filename}"')

        with open(filename, 'a') as f:
            for data_to_write in data:
                f.writelines(f"{__new_line}{data_to_write}")

    # Byte Data to File
    if (mode == 'a') and (byte_data):
        for data_to_write in data:
            if not isinstance(data_to_write, bytes): raise DumpRaw(__err_msg_bytes, f'\nDATA: "{data_to_write}"')
        # Check if file empty. Throws error if file not found
        try: 
            if __path.getsize(filename) == 0: __new_line = b''
        except FileNotFoundError as __err_msg: raise DumpRaw(__err_msg, f'\nFILE: "{filename}"')

        with open(filename, 'ab') as f:
            for data_to_write in data:
                f.write(b"\n")
                f.write(data_to_write)
