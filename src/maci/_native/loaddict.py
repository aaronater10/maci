# loaddict
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from os import path as __path
from copy import deepcopy as _deepcopy
from typing import Union as __Union
from ..data import MaciDataObj
from ..error import LoadDict, Load

#########################################################################################################
# Import py Data from File
def loaddict(filename: str, *, attr_name_dedup: bool=True, encoding: __Union[str, None]=None) -> dict:
    """
    Imports pythonic data from any text file

    Returns a dict. Assign the output to var

    Enter file location as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if file empty

    [Example Use]
    loaddict('path/to/filename.data')

    [Warning]
    Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This also may affect MaciDataObj behavior
    including the ability to overwrite internal dunder names. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.
    """
    err_msg_file = 'Invalid data type or nothing specified for filename:'
    err_msg_attrib = 'Invalid data type or nothing specified for attr_name_dedup:'

    # Error Checks
    if not isinstance(filename, str): raise LoadDict(err_msg_file, f'\nFILE: "{filename}"')
    if not isinstance(attr_name_dedup, bool): raise LoadDict(err_msg_attrib, f'\nDATA: {attr_name_dedup}')

    # Check if file empty. Returns None if empty
    try:
        if __path.getsize(filename) == 0:
            return None
    except FileNotFoundError as __err_msg: raise LoadDict(__err_msg, f'\nFILE: "{filename}"')
    except OSError as __err_msg: raise LoadDict(__err_msg, f'\nFILE: "{filename}"')

    # Syntax/Usage Error Messages
    err_messages = {
        '_py_syntax_err_msg': "Must have valid Python data types to import, or file's syntax is not formatted correctly",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names in file",
        '_name_reference_does_not_exist_msg': "Name reference does not exist! Must reference attribute names in file that have been defined",
        '_assignment_locked_atrribs_err_msg': "Attribute Name Locked! Cannot be reassigned",
        '_assignment_hard_locked_atrribs_err_msg': "Attribute Name Hard Locked! Cannot be reassigned, deleted, or unlocked"
    }

    # Internal Key List to Remove from Dict
    internal_remove_key_list = {
        '_MaciDataObjConstructor__assignment_locked_attribs',
        '_MaciDataObjConstructor__assignment_hard_locked_attribs' ,
        '_MaciDataObjConstructor__assigned_src_reference_attr_map',
        '_MaciDataObjConstructor__assigned_dst_reference_attr_map',
        '_MaciDataObjConstructor__attrib_name_dedup',
        '__maci_obj_format_id__',
        '_MaciDataObjConstructor__assignment_locked_atrribs_err_msg',
        '_MaciDataObjConstructor__assignment_hard_locked_atrribs_err_msg',
        '_MaciDataObjConstructor__ignore_internal_maci_attr_check',
    }

    # Generate Dict as a Fresh Copy
    try: 
        dict_data = _deepcopy(vars(MaciDataObj(
                filename,
                _is_load_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=encoding,
                **err_messages
            )))
    except Load as __err_msg: raise LoadDict(__err_msg) from None
    
    # Remove any Internal Keys
    for remove_key in internal_remove_key_list:
        if remove_key in dict_data:
            del dict_data[remove_key]

    # Return Final Import
    return dict_data
