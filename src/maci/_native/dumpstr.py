# dumpstr
#########################################################################################################
# Imports
from typing import Union as __Union
from typing import NewType as __NewType
from ..error import DumpStr
from ..data import __dump_data
from ..data import MaciDataObj as __MaciDataObj

#########################################################################################################
# Dump Data to String

# Hinting reference name for "CustomClass" to denote a CustomClass can be used to dump data
CustomClass = __NewType('CustomClass', object)

def dumpstr(
    data: __Union['__MaciDataObj', dict, CustomClass], 
    *,
    indent_level: int=1,
    indentation_on: bool=True,
    multi_line_str: bool=False,
    private_attrs: bool=False,
    private_under_attrs: bool=False,
    private_dunder_attrs: bool=False,
    class_attrs: bool=False,
    private_init_attrs: bool=False,
    private_init_under_attrs: bool=False,
    private_init_dunder_attrs: bool=False,
    private_class_attrs: bool=False,
    private_class_under_attrs: bool=False,
    private_class_dunder_attrs: bool=False,
    use_symbol_glyphs: bool=False,
    ) -> str:
    """
    Dumps your attributes or key/value pair data to a string

    Pass MaciDataObj, dict, or Custom Class data type for output to str

    [Importing Data Back] Functions:

    loadstr: Import data from str returning a class of attributes with Maci features

    [Options]

    indent_level: set indent level for types list, dict, tuple, set (Default 1)

    indentation_on: set to False to turn OFF indentation on types list, dict, tuple, set (Default ON)

    [Example Use]
    Normal: dumpstr(data)

    Indent OFF: dumpstr(data, indentation_on=False)
    """
    # Error Checks
    _err_messages = {
        '__err_msg_no_attrs_found': "Cannot dump string. No attributes found in the object passed",
    }
    __err_msg_type_int_indent_level = "Only int is allowed for 'indent_level'"
    __err_msg_type_bool_indentation_on = "Only bool is allowed for 'indentation_on'"

    if not isinstance(indent_level, int): raise DumpStr(__err_msg_type_int_indent_level, f'\nDATA: {indent_level}')
    if not isinstance(indentation_on, bool): raise DumpStr(__err_msg_type_bool_indentation_on, f'\nDATA: {indentation_on}')

    # Return built/dumped string
    return __dump_data(
        _is_string_request=True,
        data=data,
        filename='',
        indent_level=indent_level,
        indentation_on=indentation_on,
        multi_line_str=multi_line_str,
        class_attrs=class_attrs,
        private_attrs=private_attrs,
        private_under_attrs=private_under_attrs,
        private_dunder_attrs=private_dunder_attrs,
        private_init_attrs=private_init_attrs,
        private_init_under_attrs=private_init_under_attrs,
        private_init_dunder_attrs=private_init_dunder_attrs,
        private_class_attrs=private_class_attrs,
        private_class_under_attrs=private_class_under_attrs,
        private_class_dunder_attrs=private_class_dunder_attrs,
        use_symbol_glyphs=use_symbol_glyphs,
        **_err_messages
    )
