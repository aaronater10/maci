# cleanformat
#########################################################################################################
# Imports
from typing import Union as __Union
from ..error import CleanFormat

#########################################################################################################
# Format/Prep Dictionary, List, Tuple, or Set Data for Export
def cleanformat(datatype: __Union[dict,list,tuple,set], indent_level: int=1) -> str:
    """
    Formats a (single) dictionary, list, tuple, or set, to have a clean multiline output for exporting to a file.

    Returned output will be a str

    Note: Higher indent levels will decrease performance. Indentation is applied to the main data set only.

    Tip: Changing indent level to 0 increases cleaning performance by 5%, but output will have no indentation (Default = 1).

    Accepted data types: dict, list, tuple, set 

    [Example Use]
    
    var = cleanformat(datatype)
    """
    __err_indent = 'Only int is allowed for indent level.'
    __err_type = """Only dict, list, tuple, or set are allowed.
    If tuple, it must be empty, have a single value with a "," [e.g. (1,)], or have >= 2 values"""

    # Error Checks, Set indent level
    if not isinstance(indent_level, int):
        raise CleanFormat(__err_indent, f'\nGot: {repr(indent_level)}')
    indent_level = '    '*indent_level

    if not isinstance(datatype, (dict,list,tuple,set)):
        raise CleanFormat(__err_type, f'\nGot: {repr(datatype)}')


    # Format Data Type and Return as str
    __build_data = ""

    # Dict
    if isinstance(datatype, dict):
        for key,value in datatype.items():
            __build_data += f"\n{indent_level}{repr(key)}: {repr(value)},"
        __build_data = f"{{{__build_data}\n}}"
        return __build_data

    # List
    if isinstance(datatype, list):
        for value in datatype:
            __build_data += f"\n{indent_level}{repr(value)},"
        __build_data = f"[{__build_data}\n]"
        return __build_data

    # Tuple
    if isinstance(datatype, tuple):
        for value in datatype:
            __build_data += f"\n{indent_level}{repr(value)},"
        __build_data = f"({__build_data}\n)"
        return __build_data

    # Set
    if isinstance(datatype, set):
        for value in datatype:
            __build_data += f"\n{indent_level}{repr(value)},"
        __build_data = f"{{{__build_data}\n}}"
        return __build_data
