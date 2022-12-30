# jsonload
#########################################################################################################
# Imports
import json as __json
from ..error import JsonLoad
from typing import Union

#########################################################################################################
# Import json file
def jsonload(filename: str) -> Union[list, dict, str, int, float, bool, None]:
    """
    Imports json data from a file

    Returns data with matching python data type. Assign the output to var

    Enter json file location as str to import.

    [Example Use]

    jsonload('path/to/filename.json')

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    """
    # Import json file
    try:
        with open(filename, 'r') as f:
            return __json.load(f)
    except FileNotFoundError as __err_msg: raise JsonLoad(__err_msg, f'\nFILE: "{filename}"')
    except OSError as __err_msg: raise JsonLoad(__err_msg, f'\nFILE: "{filename}"')
    except TypeError as __err_msg: raise JsonLoad(__err_msg, f'\nFILE: "{filename}"')
    except __json.decoder.JSONDecodeError as __err_msg: raise JsonLoad(__err_msg, f'\nFILE: "{filename}"')
