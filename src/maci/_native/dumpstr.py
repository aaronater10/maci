# dumpstr
#########################################################################################################
# Imports
from typing import Union as _Union
from typing import Any as _Any
from typing import NewType as _NewType
from typing import Optional as _Optional
from ..error import DumpStr
from ..data import __dump_data
from ..data import MaciDataObj as _MaciDataObj
from ..hint import __ClassObject  # type: ignore  # ignoring attr export

#########################################################################################################
# Dump Data to String
def dumpstr(
    data: _Union['_MaciDataObj', dict, __ClassObject], 
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
    ) -> _Optional[str]:
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
    err_msg_type_indent_level = "Only int is allowed for 'indent_level'"
    err_msg_type_indentation_on = "Only bool is allowed for 'indentation_on'"
    err_msg_type_data = "Only MaciDataObj|dict|custom ClassObject is allowed for 'data'"
    err_msg_type_indent_level = "Only int is allowed for 'indent_level'"
    err_msg_type_indentation_on = "Only bool is allowed for 'indentation_on'"
    err_msg_type_multi_line_str = "Only bool is allowed for 'multi_line_str'"
    err_msg_type_private_attrs = "Only bool is allowed for 'private_attrs'"
    err_msg_type_private_under_attrs = "Only bool is allowed for 'private_under_attrs'"
    err_msg_type_private_dunder_attrs = "Only bool is allowed for 'private_dunder_attrs'"
    err_msg_type_class_attrs = "Only bool is allowed for 'class_attrs'"
    err_msg_type_private_init_attrs = "Only bool is allowed for 'private_init_attrs'"
    err_msg_type_private_init_under_attrs = "Only bool is allowed for 'private_init_under_attrs'"
    err_msg_type_private_init_dunder_attrs = "Only bool is allowed for 'private_init_dunder_attrs'"
    err_msg_type_private_class_attrs = "Only bool is allowed for 'private_class_attrs'"
    err_msg_type_private_class_under_attrs = "Only bool is allowed for 'private_class_under_attrs'"
    err_msg_type_private_class_dunder_attrs = "Only bool is allowed for 'private_class_dunder_attrs'"
    err_msg_type_use_symbol_glyphs = "Only bool is allowed for 'use_symbol_glyphs'"


    filter_data_object_types = (str, int, float, bool, list, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)

    if isinstance(data, filter_data_object_types): raise DumpStr(err_msg_type_data, f'\nGot: {repr(data)}')
    if not isinstance(indent_level, int): raise DumpStr(err_msg_type_indent_level, f'\nGot: {repr(indent_level)}')
    if not isinstance(indentation_on, bool): raise DumpStr(err_msg_type_indentation_on, f'\nGot: {repr(indentation_on)}')
    if not isinstance(multi_line_str, bool): raise DumpStr(err_msg_type_multi_line_str, f'\nGot: {repr(multi_line_str)}')
    if not isinstance(private_attrs, bool): raise DumpStr(err_msg_type_private_attrs, f'\nGot: {repr(private_attrs)}')
    if not isinstance(private_under_attrs, bool): raise DumpStr(err_msg_type_private_under_attrs, f'\nGot: {repr(private_under_attrs)}')
    if not isinstance(private_dunder_attrs, bool): raise DumpStr(err_msg_type_private_dunder_attrs, f'\nGot: {repr(private_dunder_attrs)}')
    if not isinstance(class_attrs, bool): raise DumpStr(err_msg_type_class_attrs, f'\nGot: {repr(class_attrs)}')
    if not isinstance(private_init_attrs, bool): raise DumpStr(err_msg_type_private_init_attrs, f'\nGot: {repr(private_init_attrs)}')
    if not isinstance(private_init_under_attrs, bool): raise DumpStr(err_msg_type_private_init_under_attrs, f'\nGot: {repr(private_init_under_attrs)}')
    if not isinstance(private_init_dunder_attrs, bool): raise DumpStr(err_msg_type_private_init_dunder_attrs, f'\nGot: {repr(private_init_dunder_attrs)}')
    if not isinstance(private_class_attrs, bool): raise DumpStr(err_msg_type_private_class_attrs, f'\nGot: {repr(private_class_attrs)}')
    if not isinstance(private_class_under_attrs, bool): raise DumpStr(err_msg_type_private_class_under_attrs, f'\nGot: {repr(private_class_under_attrs)}')
    if not isinstance(private_class_dunder_attrs, bool): raise DumpStr(err_msg_type_private_class_dunder_attrs, f'\nGot: {repr(private_class_dunder_attrs)}')
    if not isinstance(use_symbol_glyphs, bool): raise DumpStr(err_msg_type_use_symbol_glyphs, f'\nGot: {repr(use_symbol_glyphs)}')

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
        use_symbol_glyphs=use_symbol_glyphs
    )
