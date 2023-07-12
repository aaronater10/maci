# loaddict
#########################################################################################################
# Imports
from os import path as _path
from copy import deepcopy as _deepcopy
from typing import Any as _Any
from typing import Optional as _Optional
from ..error import LoadDict, Load
from ..data import MaciDataObj as _MaciDataObj

#########################################################################################################
# Import py Data from File
def loaddict(filename: str, *, attr_name_dedup: bool=True, encoding: _Optional[str]=None) -> _Optional[dict]:
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
    # Error Checks
    err_msg_type_filename = "Only str is allowed for 'filename'"
    err_msg_type_attr_name_dedup = "Only bool is allowed for 'attr_name_dedup'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise LoadDict(err_msg_type_filename, f'\nGot: {repr(filename)}')
    if not isinstance(attr_name_dedup, bool): raise LoadDict(err_msg_type_attr_name_dedup, f'\nGot: {repr(attr_name_dedup)}')
    if not isinstance(encoding, (str, type(None))): raise LoadDict(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Check if file empty. Returns None if empty
    try:
        if _path.getsize(filename) == 0:
            return dict()
    except (FileNotFoundError, OSError) as __err_msg: raise LoadDict(__err_msg, f'\nGot: {repr(filename)}')

    # Syntax/Usage Error Messages
    err_messages: _Any = {  # ignore type checker
        '_py_syntax_err_msg': "Must have valid Python data types to import, or file's maci syntax is incorrect",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names in file",
        '_name_reference_does_not_exist_msg': "Map name does not exist! Must map attribute names in file that have been defined",
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
        dict_data = _deepcopy(vars(_MaciDataObj(
                filename,
                _is_load_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=encoding,
                **err_messages
            )))
    except Load as __err_msg: raise LoadDict(__err_msg) from None
    except LookupError: raise LoadDict(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Remove any Internal Keys
    for remove_key in internal_remove_key_list:
        if remove_key in dict_data: # pragma: no branch
            del dict_data[remove_key]

    # Return Final Import
    return dict_data
