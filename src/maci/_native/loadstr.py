# loadstr
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Optional as _Optional
from ..error import LoadStr, Load
from ..data import MaciDataObj as _MaciDataObj
from .build import build as _build

#########################################################################################################
# Import py Data from String
def loadstr(maci_str_data: str, *, attr_name_dedup: bool=True) -> _Optional[_MaciDataObj]:
    """
    Imports python data from a string.

    Returns a class of attributes. Assign the output to var

    Enter python data string as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns empty object if string empty

    [Example Use]

    loadstr("data1 = 'value1'\\ndata2 = "value2")
    """
    # Error Checks
    err_msg_type_maci_str_data = "Only str is allowed for 'maci_str_data'"
    err_msg_type_attr_name_dedup = "Only bool is allowed for 'attr_name_dedup'"

    if not isinstance(maci_str_data, str): raise LoadStr(err_msg_type_maci_str_data, f'\nGot: {repr(maci_str_data)}')
    if not isinstance(attr_name_dedup, bool): raise LoadStr(err_msg_type_attr_name_dedup, f'\nGot: {repr(attr_name_dedup)}')

    # Check if string empty. Returns None if empty
    if maci_str_data.strip() == '': return _build()

    # Syntax/Usage Error Messages
    __err_messages: _Any = {  # ignore type checker
        '_py_syntax_err_msg': "Must have valid Python data types to import, or string's maci syntax is incorrect",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names in string",
        '_name_reference_does_not_exist_msg': "Map name does not exist! Must map attribute names in string that have been defined",
        '_assignment_locked_atrribs_err_msg': "Attribute Name Locked! Cannot be reassigned",
        '_assignment_hard_locked_atrribs_err_msg': "Attribute Name Hard Locked! Cannot be reassigned, deleted, or unlocked"
    }

    # Return final import
    try:
        return _MaciDataObj(
                '',
                _is_load_request=True,
                _str_data=maci_str_data,
                _is_str_parse_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=None,
                **__err_messages,
            )
    except Load as __err_msg:
        __err_msg.item = __err_msg.item.replace("\nFile: ''", "")
        raise LoadStr(__err_msg.msg, f'{__err_msg.item}')
