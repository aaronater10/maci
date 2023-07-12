# cleanformat
#########################################################################################################
# Imports
from typing import Union as _Union
from ..error import CleanFormat

#########################################################################################################
# Format/Prep Dictionary, List, Tuple, or Set Data for Export
def cleanformat(data: _Union[dict,list,tuple,set], indent_level: int=1) -> str:
    """
    Formats a (single) dictionary, list, tuple, or set, to have a clean multiline output for exporting to a file.

    Returned output will be a str

    Note: Higher indent levels will decrease performance. Indentation is applied to the main data set only.

    Tip: Changing indent level to 0 increases cleaning performance by 5%, but output will have no indentation (Default = 1).

    Accepted data types: dict, list, tuple, set 

    [Example Use]
    
    var = cleanformat(data)
    """
    err_type = "Only dict|list|tuple|set is allowed for 'data'"
    err_indent = "Only int is allowed for 'indent_level'"

    # Error Checks, Set indent level
    if not isinstance(indent_level, int):
        raise CleanFormat(err_indent, f'\nGot: {repr(indent_level)}')
    indent_level = '    '*indent_level

    if not isinstance(data, (dict,list,tuple,set)):
        raise CleanFormat(err_type, f'\nGot: {repr(data)}')


    # Format Data Type and Return as str
    build_data = ""

    # Dict
    if isinstance(data, dict):
        for key,value in data.items():
            build_data += f"\n{indent_level}{repr(key)}: {repr(value)},"
        build_data = f"{{{build_data}\n}}"
        return build_data

    # List
    if isinstance(data, list):
        for value in data:
            build_data += f"\n{indent_level}{repr(value)},"
        build_data = f"[{build_data}\n]"
        return build_data

    # Tuple
    if isinstance(data, tuple):
        for value in data:
            build_data += f"\n{indent_level}{repr(value)},"
        build_data = f"({build_data}\n)"
        return build_data

    # Set
    if isinstance(data, set): # pragma: no branch
        for value in data:
            build_data += f"\n{indent_level}{repr(value)},"
        build_data = f"{{{build_data}\n}}"
        return build_data
