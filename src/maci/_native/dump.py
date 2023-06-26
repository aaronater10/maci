# dump
#########################################################################################################
# Imports
from typing import Union as __Union
from typing import NewType as __NewType
from typing import Any as _Any
from ..error import Dump
from ..data import __dump_data
from ..data import MaciDataObj as __MaciDataObj

#########################################################################################################
# Dump Data to File

# Hinting reference name for "CustomClass" to denote a CustomClass can be used to dump data
CustomClass = __NewType('CustomClass', object)

def dump(
    filename: str, 
    data: __Union['__MaciDataObj', dict, CustomClass], 
    *,
    append: bool=False,
    indent_level: int=1,
    indentation_on: bool=True,
    multi_line_str: bool=False,
    encoding: __Union[str, None]=None,
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
    ) -> None:
    """
    Dumps your attributes or key/value pair data to a file

    Enter filename as str, Pass MaciDataObj, dict, or Custom Class data type for output to file

    [Importing Data Back] Functions:

    load: Import data back returning a class of attributes with Maci features

    loadattrs: Import attributes back into a custom class. This is done in-place

    [Options]

    append: set to True to append data to a file (Default=False, which writes a new file each time)

    indent_level: set indent level for types list, dict, tuple, set (Default 1)

    indentation_on: set to False to turn OFF indentation on types list, dict, tuple, set (Default ON)

    [Example Use]
    Normal: dump('path/of/filename', 'data')

    Append to File: dump('path/of/filename', 'data', append=True)

    Indent OFF: dump('path/of/filename', 'data', indentation_on=False)
    """
    # Error Checks & Messages
    _err_messages: _Any = {  # ignore type checker
        '__err_msg_no_attrs_found': "Cannot save file. No attributes found in the object passed",
    }
    __err_msg_type_filename = "Only str is allowed for 'filename'"
    __err_msg_type_data = "Only MaciDataObj|dict|CustomClass is allowed for 'data'"
    __err_msg_type_append = "Only bool is allowed for 'append'"
    __err_msg_type_indent_level = "Only int is allowed for 'indent_level'"
    __err_msg_type_indentation_on = "Only bool is allowed for 'indentation_on'"
    __err_msg_type_multi_line_str = "Only bool is allowed for 'multi_line_str'"
    __err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"
    __err_msg_type_private_attrs = "Only bool is allowed for 'private_attrs'"
    __err_msg_type_private_under_attrs = "Only bool is allowed for 'private_under_attrs'"
    __err_msg_type_private_dunder_attrs = "Only bool is allowed for 'private_dunder_attrs'"
    __err_msg_type_class_attrs = "Only bool is allowed for 'class_attrs'"
    __err_msg_type_private_init_attrs = "Only bool is allowed for 'private_init_attrs'"
    __err_msg_type_private_init_under_attrs = "Only bool is allowed for 'private_init_under_attrs'"
    __err_msg_type_private_init_dunder_attrs = "Only bool is allowed for 'private_init_dunder_attrs'"
    __err_msg_type_private_class_attrs = "Only bool is allowed for 'private_class_attrs'"
    __err_msg_type_private_class_under_attrs = "Only bool is allowed for 'private_class_under_attrs'"
    __err_msg_type_private_class_dunder_attrs = "Only bool is allowed for 'private_class_dunder_attrs'"
    __err_msg_type_use_symbol_glyphs = "Only bool is allowed for 'use_symbol_glyphs'"


    filter_data_object_types = (str, int, float, bool, list, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)

    if not isinstance(filename, str): raise Dump(__err_msg_type_filename, f'\nGot: "{filename}"')
    if isinstance(data, filter_data_object_types): raise Dump(__err_msg_type_data, f'\nGot: {repr(data)}')
    if not isinstance(append, bool): raise Dump(__err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(indent_level, int): raise Dump(__err_msg_type_indent_level, f'\nGot: {repr(indent_level)}')
    if not isinstance(indentation_on, bool): raise Dump(__err_msg_type_indentation_on, f'\nGot: {repr(indentation_on)}')
    if not isinstance(multi_line_str, bool): raise Dump(__err_msg_type_multi_line_str, f'\nGot: {repr(multi_line_str)}')
    if not isinstance(encoding, (str, type(None))): raise Dump(__err_msg_type_encoding, f'\nGot: {repr(encoding)}')
    if not isinstance(private_attrs, bool): raise Dump(__err_msg_type_private_attrs, f'\nGot: {repr(private_attrs)}')
    if not isinstance(private_under_attrs, bool): raise Dump(__err_msg_type_private_under_attrs, f'\nGot: {repr(private_under_attrs)}')
    if not isinstance(private_dunder_attrs, bool): raise Dump(__err_msg_type_private_dunder_attrs, f'\nGot: {repr(private_dunder_attrs)}')
    if not isinstance(class_attrs, bool): raise Dump(__err_msg_type_class_attrs, f'\nGot: {repr(class_attrs)}')
    if not isinstance(private_init_attrs, bool): raise Dump(__err_msg_type_private_init_attrs, f'\nGot: {repr(private_init_attrs)}')
    if not isinstance(private_init_under_attrs, bool): raise Dump(__err_msg_type_private_init_under_attrs, f'\nGot: {repr(private_init_under_attrs)}')
    if not isinstance(private_init_dunder_attrs, bool): raise Dump(__err_msg_type_private_init_dunder_attrs, f'\nGot: {repr(private_init_dunder_attrs)}')
    if not isinstance(private_class_attrs, bool): raise Dump(__err_msg_type_private_class_attrs, f'\nGot: {repr(private_class_attrs)}')
    if not isinstance(private_class_under_attrs, bool): raise Dump(__err_msg_type_private_class_under_attrs, f'\nGot: {repr(private_class_under_attrs)}')
    if not isinstance(private_class_dunder_attrs, bool): raise Dump(__err_msg_type_private_class_dunder_attrs, f'\nGot: {repr(private_class_dunder_attrs)}')
    if not isinstance(use_symbol_glyphs, bool): raise Dump(__err_msg_type_use_symbol_glyphs, f'\nGot: {repr(use_symbol_glyphs)}')

    # Write built data to file, return None
    __dump_data(
        filename=filename,
        data=data,
        append=append,
        indent_level=indent_level,
        indentation_on=indentation_on,
        multi_line_str=multi_line_str,
        encoding=encoding,
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

    return None
