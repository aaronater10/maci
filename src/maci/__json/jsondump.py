# jsondump
#########################################################################################################
# Imports
import json as __json
from ..error import JsonDump
from typing import Union

#########################################################################################################
# Export json file
def jsondump(filename: str, data: Union[str, int, float, bool, list, dict, tuple, None]) -> None:
    """
    Exports a new file from python data type to json data.
    
    Enter new filename as str. Pass data for output to file
    
    [Example Use]

    jsondump('path/to/filename.json', data)    

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    
    """
    try:
        # Export data to json file
        with open(filename, 'w') as f:
            __json.dump(data, f)
    except TypeError as __err_msg: raise JsonDump(__err_msg, f'\nFILE: "{filename}" \nDATA:{data}')
    except ValueError as __err_msg: raise JsonDump(__err_msg, f'\nFILE: "{filename}" \nDATA:{data}')
    except FileNotFoundError as __err_msg: raise JsonDump(__err_msg, f'\nFILE: "{filename}"')
