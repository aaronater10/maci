# load
#########################################################################################################
# Imports
from os import path as _path
from typing import Any as _Any
from typing import Optional as _Optional
from ..error import Load, GeneralError
from ..data import MaciDataObj as _MaciDataObj
from .build import build as _build

#########################################################################################################
# Import py Data from File
def load(filename: str, *, attr_name_dedup: bool=True, encoding: _Optional[str]=None, _ignore_maci_attr_check: bool=False) -> _MaciDataObj:
    """
    Imports saved python data from any text file.

    Returns a class of attributes. Assign the output to var

    Enter file location as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns empty object if file empty

    [Example Use]
    load('filename.data' or 'path/to/filename.data')

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
    err_msg_type__ignore_maci_attr_check = "Only bool is allowed for '_ignore_maci_attr_check'"
    
    if not isinstance(filename, str): raise Load(err_msg_type_filename, f'\nGot: {repr(filename)}')
    if not isinstance(attr_name_dedup, bool): raise Load(err_msg_type_attr_name_dedup, f'\nGot: {repr(attr_name_dedup)}')
    if not isinstance(encoding, (str, type(None))): raise Load(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
    if not isinstance(_ignore_maci_attr_check, bool): raise Load(err_msg_type__ignore_maci_attr_check, f'\nGot: {repr(_ignore_maci_attr_check)}')

    # Check if file empty. Returns None if empty
    try:
        if _path.getsize(filename) == 0:
            return _build()
    except (FileNotFoundError, OSError) as __err_msg: raise Load(__err_msg, f'\nGot: {repr(filename)}')

    # Syntax/Usage Error Messages
    __err_messages: _Any = {  # ignore type checker
        '_py_syntax_err_msg': "Must have valid Python data types to import, or file's maci syntax is incorrect",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names in file",
        '_name_reference_does_not_exist_msg': "Map name does not exist! Must map attribute names in file that have been defined",
        '_assignment_locked_atrribs_err_msg': "Attribute Name Locked! Cannot be reassigned",
        '_assignment_hard_locked_atrribs_err_msg': "Attribute Name Hard Locked! Cannot be reassigned, deleted, or unlocked"
    }

    # Return Final Import
    try:
        return _MaciDataObj(
                    filename,
                    _is_load_request=True,
                    _ignore_internal_maci_attr_check=_ignore_maci_attr_check,
                    attr_name_dedup=attr_name_dedup,
                    encoding=encoding,
                    **__err_messages
                )
    except GeneralError as err: raise Load(err) from None
    except LookupError: raise Load(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
