# load
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from os import path as __path
from typing import Union as __Union
from ..data import MaciDataObj
from ..error import Load

#########################################################################################################
# Import py Data from File
def load(filename: str, *, attr_name_dedup: bool=True, encoding: __Union[str, None]=None) -> 'MaciDataObj':
    """
    Imports saved python data from any text file.

    Returns a class of attributes. Assign the output to var

    Enter file location as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if file empty

    [Example Use]
    load('filename.data' or 'path/to/filename.data')

    [Warning]
    Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This also may affect MaciDataObj behavior
    including the ability to overwrite internal dunder names. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.
    """
    __err_msg_file = 'Invalid data type or nothing specified for filename:'
    __err_msg_attrib = 'Invalid data type or nothing specified for attr_name_dedup:'
    
    # Error Checks
    if not isinstance(filename, str): raise Load(__err_msg_file, f'\nFILE: "{filename}"')
    if not isinstance(attr_name_dedup, bool): raise Load(__err_msg_attrib, f'\nDATA: {attr_name_dedup}')

    # Check if file empty. Returns None if empty
    try:
        if __path.getsize(filename) == 0:
            return None
    except FileNotFoundError as __err_msg: raise Load(__err_msg, f'\nFILE: "{filename}"')
    except OSError as __err_msg: raise Load(__err_msg, f'\nFILE: "{filename}"')

    # Syntax/Usage Error Messages
    __err_messages = {
        '_py_syntax_err_msg': "Must have valid Python data types to import, or file's syntax is not formatted correctly",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names in file",
        '_name_reference_does_not_exist_msg': "Name reference does not exist! Must reference attribute names in file that have been defined",
        '_assignment_locked_atrribs_err_msg': "Attribute Name Locked! Cannot be reassigned",
        '_assignment_hard_locked_atrribs_err_msg': "Attribute Name Hard Locked! Cannot be reassigned, deleted, or unlocked"
    }

    # Return Final Import
    return MaciDataObj(
                filename,
                _is_load_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=encoding,
                **__err_messages
            )
