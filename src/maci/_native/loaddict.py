# loaddict
#########################################################################################################
# Imports
from os import path as _path
from copy import deepcopy as _deepcopy
from typing import Any as _Any
from typing import Optional as _Optional
from typing import Union as _Union
from pathlib import Path as _PathObj
from ..error import LoadDict, Load
from ..data import MaciDataObj as _MaciDataObj

#########################################################################################################
# Import py Data from File
def loaddict(filename: _Union[str, _PathObj], *, attr_name_dedup: bool=False, encoding: _Optional[str]=None) -> _Optional[dict]:
    """
    Loads maci (pythonic) data from a file

    Returns a dict representing your attributes & data values. Returns empty dict if file empty

    [Example: Usage]

    loaddict('path/to/filename.any')

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_filename = "Only str is allowed for 'filename'"
    err_msg_type_attr_name_dedup = "Only bool is allowed for 'attr_name_dedup'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, (str, _PathObj)): raise LoadDict(err_msg_type_filename, f'\nGot: {repr(filename)}')
    if not isinstance(attr_name_dedup, bool): raise LoadDict(err_msg_type_attr_name_dedup, f'\nGot: {repr(attr_name_dedup)}')
    if not isinstance(encoding, (str, type(None))): raise LoadDict(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

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

    # Generate Dict as a Fresh Copy
    try: 
        maci_data = _MaciDataObj(
                filename,
                _is_load_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=encoding,
                _ignore_internal_maci_attr_check=True,
                **err_messages
            )
    except Load as __err_msg: raise LoadDict(__err_msg) from None
    except LookupError: raise LoadDict(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Return Import
    dict_data = _deepcopy(maci_data._MaciDataObjConstructor__assignment_tracker)
    del maci_data
    return dict_data
