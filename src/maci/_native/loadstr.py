# loadstr
#########################################################################################################
# Imports
from ..data import MaciDataObj
from ..error import LoadStr, Load

#########################################################################################################
# Import py Data from String
def loadstr(py_str_data: str, *, attr_name_dedup: bool=True) -> 'MaciDataObj':
    """
    Imports python data from a string.

    Returns a class of attributes. Assign the output to var

    Enter python data string as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if empty

    [Example Use]

    loadstr("data1 = 'value1'\\ndata2 = "value2")
    """
    __err_msg_py_str = 'Invalid data type or nothing specified for "py_str_data"'
    __err_msg_attrib = 'Invalid data type or nothing specified for "attr_name_dedup"'

    # Error Checks
    if not isinstance(py_str_data, str): raise LoadStr(__err_msg_py_str, f'\nDATA: "{py_str_data}"')
    if not isinstance(attr_name_dedup, bool): raise LoadStr(__err_msg_attrib, f'\nDATA: {attr_name_dedup}')

    # Check if string empty. Returns None if empty
    if py_str_data == '': return None

    # Syntax/Usage Error Messages
    __err_messages = {
        '_py_syntax_err_msg': "Must have valid Python data types to import, or string's syntax is not formatted correctly",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names in string",
        '_name_reference_does_not_exist_msg': "Name reference does not exist! Must reference attribute names in string that have been defined",
        '_assignment_locked_atrribs_err_msg': "Attribute Name Locked! Cannot be reassigned"
    }

    # Return final import
    try:
        return MaciDataObj(
                '',
                _is_load_request=True,
                _str_data=py_str_data,
                _is_str_parse_request=True,
                attr_name_dedup=attr_name_dedup,
                encoding=None,
                **__err_messages,
            )
    except Load as __err_msg:
        __err_msg.item = __err_msg.item.replace('\nFILE: ""', "")
        raise LoadStr(__err_msg.msg, f'{__err_msg.item}')
