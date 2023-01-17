# inidump
#########################################################################################################
# Imports
from configparser import ConfigParser as __ConfigParser
from typing import NewType as __NewType
from ..error import IniDump

#########################################################################################################
# Export ini file

# Hinting reference name for "ini_data" to denote ini data needs to be dumped
IniData = __NewType('ini_data', __ConfigParser)

def inidump(filename: str, data: IniData) -> None:
    """
    Exports a new file from a ini data (ConfigParser) obj
    
    Enter new filename as str. Pass ini data for output to file
    
    [Example Use]

    inidump('path/to/filename.ini', data)

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """
    __err_msg_parser = f"Invalid data to export, type, or nothing specified"
        
    if not isinstance(data, __ConfigParser):
        raise IniDump(__err_msg_parser, f'\nFILE: "{filename}" \nDATA: {data}')
    try:
        with open(filename, 'w') as f:
            data.write(f)
    except TypeError as __err_msg: raise IniDump(__err_msg, f'\nFILE: "{filename}" \nDATA: {data}')
    except ValueError as __err_msg: raise IniDump(__err_msg, f'\nFILE: "{filename}" \nDATA: {data}')
    except FileNotFoundError as __err_msg: raise IniDump(__err_msg, f'\nFILE: "{filename}"')
