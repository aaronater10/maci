# loadstrdict
#########################################################################################################
# Imports
from copy import deepcopy as _deepcopy
from typing import Any as _Any
from typing import Optional as _Optional
from ..error import LoadStrDict, Load
from ..data import MaciDataObj as _MaciDataObj

#########################################################################################################
# Import py Data from String
def loadstrdict(maci_str_data: str, *, attr_name_dedup: bool=True) -> _Optional[dict]:
    """
    Imports pythonic data from a string.

    Returns a dict. Assign the output to var

    Enter pythonic data string as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if empty

    [Example Use]

    loadstrdict("data1 = 'value1'\\ndata2 = "value2")
    """
    # Error Checks
    err_msg_type_maci_str_data = "Only str is allowed for 'maci_str_data'"
    err_msg_type_attr_name_dedup = "Only bool is allowed for 'attr_name_dedup'"

    if not isinstance(maci_str_data, str): raise LoadStrDict(err_msg_type_maci_str_data, f'\nGot: {repr(maci_str_data)}')
    if not isinstance(attr_name_dedup, bool): raise LoadStrDict(err_msg_type_attr_name_dedup, f'\nGot: {repr(attr_name_dedup)}')

    # Check if string empty. Returns None if empty
    if maci_str_data.strip() == '': return dict()

    # Syntax/Usage Error Messages
    __err_messages: _Any = {  # ignore type checker
        '_py_syntax_err_msg': "Must have valid Python data types to import, or string's maci syntax is incorrect",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names in string",
        '_name_reference_does_not_exist_msg': "Map name does not exist! Must map attribute names in string that have been defined",
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
                '',
                _is_load_request=True,
                _str_data=maci_str_data,
                _is_str_parse_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=None,
                **__err_messages,
            )))
    except Load as __err_msg:
        __err_msg.item = __err_msg.item.replace("\nFile: ''", "")
        raise LoadStrDict(__err_msg.msg, f'{__err_msg.item}') from None

    # Remove any Internal Keys
    for remove_key in internal_remove_key_list:
        if remove_key in dict_data: # pragma: no branch
            del dict_data[remove_key]

    # Return Final Import
    return dict_data
