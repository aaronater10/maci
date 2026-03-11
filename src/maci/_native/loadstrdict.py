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
def loadstrdict(maci_str_data: str, *, attr_name_dedup: bool=False) -> _Optional[dict]:
    """
    Loads maci (pythonic) data from a string

    Returns a dict representing your attributes & data values. Returns empty dict if string empty

    [Example: Usage]

    loadstrdict('string with maci data')

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a string that has already been created.

    Maci docs: https://docs.macilib.org
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

    # Generate Dict as a Fresh Copy
    try:
        maci_data = _MaciDataObj(
                '',
                _is_load_request=True,
                _str_data=maci_str_data,
                _is_str_parse_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=None,
                _ignore_internal_maci_attr_check=True,
                **__err_messages,
            )
    except Load as __err_msg:
        __err_msg.item = __err_msg.item.replace("\nFile: ''", "")
        raise LoadStrDict(__err_msg.msg, f'{__err_msg.item}') from None

    # Return Import
    dict_data = _deepcopy(maci_data._MaciDataObjConstructor__assignment_tracker)
    del maci_data
    return dict_data
