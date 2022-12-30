# iniload
#########################################################################################################
# Imports
from configparser import ConfigParser as __ConfigParser
from configparser import ExtendedInterpolation as __ExtendedInterpolation
from ..error import IniLoad

#########################################################################################################
# Import ini file
def iniload(filename: str) -> __ConfigParser:
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
    try:
        with open(filename, 'r') as f: pass
    except TypeError as __err_msg: raise IniLoad(__err_msg, f'\nFILE: "{filename}"')
    except ValueError as __err_msg: raise IniLoad(__err_msg, f'\nFILE: "{filename}"')
    except FileNotFoundError as __err_msg: raise IniLoad(__err_msg, f'\nFILE: "{filename}"')

    __parser = __ConfigParser(interpolation=__ExtendedInterpolation())
    __parser.read(filename)
    return __parser
