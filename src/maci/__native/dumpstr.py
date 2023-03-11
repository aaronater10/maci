# dumpstr
#########################################################################################################
# Imports
from typing import Union as __Union
from typing import Any as __Any
from typing import NewType as __NewType
from ..error import DumpStr
from ..data import MaciDataObj as __MaciDataObj
from ..data import _Glyphs
from .cleanformat import cleanformat as __cleanformat

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
    class_attrs: bool=False,
    private_attrs: bool=False,
    private_under_attrs: bool=False,
    private_dunder_attrs: bool=False,
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
    __err_msg_general_error = "Error has occurred and cannot proceed"
    __err_msg_no_attrs_found = "Cannot dump string. No attributes found in the object passed"
    __err_msg_type_int_indent_level = "Only int is allowed for 'indent_level'"
    __err_msg_type_bool_indentation_on = "Only bool is allowed for 'indentation_on'"

    if not isinstance(indent_level, int): raise DumpStr(__err_msg_type_int_indent_level, f'\nDATA: {indent_level}')
    if not isinstance(indentation_on, bool): raise DumpStr(__err_msg_type_bool_indentation_on, f'\nDATA: {indentation_on}')

    # Setup
    __build_data_output = ""
    __assignment_glyphs = _Glyphs()
    __skip_object_key = ('_MaciDataObjConstructor', '__maci_obj_format_id')
    __locked_attr_list_key =  '_MaciDataObjConstructor__assignment_locked_attribs'
    __hard_locked_attr_list_key =  '_MaciDataObjConstructor__assignment_hard_locked_attribs'
    __reference_attr_list_key =  '_MaciDataObjConstructor__assigned_src_reference_attr_map'
    __maci_obj_format_id_match = "48448910-fa49-45ca-bd3e-38d7af136af5-7bcece52-e5ee-4272-989d-103f07aa6c0f"

    # Set Glyph Style to Symbols if Requested - Creates New Object with Same Names
    if use_symbol_glyphs:
        __assignment_glyphs = _Glyphs(
            r=__assignment_glyphs.ref,
            h=__assignment_glyphs.hard_lock,
            l=__assignment_glyphs.lock,
            rh=__assignment_glyphs.ref_hard_lock,
            rl=__assignment_glyphs.ref_lock,
        )

    ### MACI DATA: Check if MaciDataObj ###

    # Build Out Data
    if (isinstance(data, __MaciDataObj)) and (data.__maci_obj_format_id__ == __maci_obj_format_id_match):
        for key,value in data.__dict__.items():
            # If Match Prefixes, Skip
            if not key.startswith(__skip_object_key):
                # Check Glyph Type and Build Accordingly

                # Reset Values
                is_set_start_new_line = ''
                is_set_end_new_line = ''

                # Check for Dunder or Unders
                _is_dunder_attr = False
                if key.startswith(f'__'):
                    if (private_attrs or private_dunder_attrs):
                        _is_dunder_attr = True
                    else: continue
                if (key.startswith('_')) and not (_is_dunder_attr):
                    if not (private_attrs or private_under_attrs):
                        continue
                _is_dunder_attr = False # reset dunder check for single under's

                # Reference Name and Locked
                if (key in data.__dict__[__reference_attr_list_key]) and (key in data.__dict__[__locked_attr_list_key]):
                    __build_data_output += f'{key} {__assignment_glyphs.rl} {data.__dict__[__reference_attr_list_key][key]}\n'
                    continue
                # Reference Name and Hard Locked
                if (key in data.__dict__[__reference_attr_list_key]) and (key in data.__dict__[__hard_locked_attr_list_key]):
                    __build_data_output += f'{key} {__assignment_glyphs.rh} {data.__dict__[__reference_attr_list_key][key]}\n'
                    continue
                # Reference Name Only
                if key in data.__dict__[__reference_attr_list_key]:
                    __build_data_output += f'{key} {__assignment_glyphs.r} {data.__dict__[__reference_attr_list_key][key]}\n'
                    continue
                # Locked Only
                if key in data.__dict__[__locked_attr_list_key]:
                    if __multiline_check(value) and indentation_on:
                        value = __cleanformat(value, indent_level)
                        __build_data_output += f'{key} {__assignment_glyphs.l} {value}\n'
                    elif (multi_line_str) and ('\n' in value) and (isinstance(value, str)):
                        is_set_start_new_line = '' if value.startswith('\n') else '\n'
                        is_set_end_new_line = '' if value.endswith('\n') else '\n'
                        __build_data_output += f"{key} {__assignment_glyphs.l} '''{is_set_start_new_line}{value}{is_set_end_new_line}'''\n"
                    else: __build_data_output += f'{key} {__assignment_glyphs.l} {repr(value)}\n'
                    continue
                # Hard Locked Only
                if key in data.__dict__[__hard_locked_attr_list_key]:
                    if __multiline_check(value) and indentation_on:
                        value = __cleanformat(value, indent_level)
                        __build_data_output += f'{key} {__assignment_glyphs.h} {value}\n'
                    elif (multi_line_str) and ('\n' in value) and (isinstance(value, str)):
                        is_set_start_new_line = '' if value.startswith('\n') else '\n'
                        is_set_end_new_line = '' if value.endswith('\n') else '\n'
                        __build_data_output += f"{key} {__assignment_glyphs.h} '''{is_set_start_new_line}{value}{is_set_end_new_line}'''\n"
                    else: __build_data_output += f'{key} {__assignment_glyphs.h} {repr(value)}\n'
                    continue
                # Normal Assignment
                if __multiline_check(value) and indentation_on:
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_glyphs.norm} {value}\n'
                elif (multi_line_str) and ('\n' in value) and (isinstance(value, str)):
                    is_set_start_new_line = '' if value.startswith('\n') else '\n'
                    is_set_end_new_line = '' if value.endswith('\n') else '\n'
                    __build_data_output += f"{key} {__assignment_glyphs.norm} '''{is_set_start_new_line}{value}{is_set_end_new_line}'''\n"
                else: __build_data_output += f'{key} {__assignment_glyphs.norm} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        # Return String Data
        return __build_data_output


    ### DICT: Check if dict ###
    if isinstance(data, dict):
        # Build Data
        for key,value in data.items():
            # Multline Assignment from Indentation
            if indentation_on:
                if __multiline_check(value):
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_glyphs.norm} {value}\n'
                    continue
            # Single Line Assignment
            __build_data_output += f'{key} {__assignment_glyphs.norm} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        # Return String Data
        return __build_data_output


    ### CUSTOM CLASS: Check if any Class Object with Attributes
    _filter_objects = (str, int, float, bool, list, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)
    if not isinstance(data, _filter_objects):
        # Setup
        _init_attr_header = '# attrs: init'
        __build_data_output_init = ''
        _class_attr_header = '# attrs: class'
        __build_data_output_class = ''
        _is_dunder_attr = False
        _is_case1_build = False
        _is_case2_build = False
        _is_case3_build = False

        # Case 1 - Class Attrs Only. Is Instantiated
        if (bool(vars(data)) == False) and class_attrs:
            _is_case1_build = True
            
            for key,value in vars(type(data)).items():
                # Strip Unneeded Attrs/Methods, and Preserve Dunders if Required
                if callable(value): continue
                if (key.startswith('__') and key.endswith('__')): continue
                if key.startswith(f'_{type(data).__name__}'): # dunder detection (name mangle)
                    if (private_attrs) or (private_dunder_attrs) or (private_class_attrs) or (private_class_dunder_attrs):
                        key = key.removeprefix(f'_{type(data).__name__}')
                        _is_dunder_attr = True
                    else: continue
                if (key.startswith('_')) and not (_is_dunder_attr):
                    if not (private_attrs or private_under_attrs or private_class_attrs or private_class_under_attrs):
                        continue
                _is_dunder_attr = False # reset dunder check for single under's

                # Build Data
                if __multiline_check(value) and indentation_on:
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_glyphs.norm} {value}\n'
                else: __build_data_output += f'{key} {__assignment_glyphs.norm} {repr(value)}\n'

        # Case 2 - Class Attrs Only. Not Instantiated
        elif '__mro__' in vars(type(data)) and class_attrs:
            _is_case2_build = True

            for key,value in vars(data).items():
                # Strip Unneeded Attrs/Methods, and Preserve Dunders if Required
                if callable(value): continue
                if (key.startswith('__') and key.endswith('__')): continue
                if key.startswith(f'_{data.__name__}'): # dunder detection (name mangle)
                    if (private_attrs) or (private_dunder_attrs) or (private_class_attrs) or (private_class_dunder_attrs):
                        key = key.removeprefix(f'_{data.__name__}')
                        _is_dunder_attr = True
                    else: continue
                if (key.startswith('_')) and not (_is_dunder_attr):
                    if not (private_attrs or private_under_attrs or private_class_attrs or private_class_under_attrs):
                        continue
                _is_dunder_attr = False # reset dunder check for single under's

                # Build Data
                if __multiline_check(value) and indentation_on:
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_glyphs.norm} {value}\n'
                else: __build_data_output += f'{key} {__assignment_glyphs.norm} {repr(value)}\n'
        
        # Default Case 3 - Init Attrs or Class Attrs, or both
        else:
            _is_case3_build = True

            # First: Init Attrs
            if '__init__' not in vars(data):
                for key,value in vars(data).items():
                    # Strip Unneeded Attrs/Methods, and Preserve Dunders if Required
                    if callable(value): continue
                    if key.startswith(f'_{type(data).__name__}'): # dunder detection (name mangle)
                        if (private_attrs) or (private_dunder_attrs) or (private_init_attrs) or (private_init_dunder_attrs):
                            key = key.removeprefix(f'_{type(data).__name__}')
                            _is_dunder_attr = True
                        else: continue
                    if (key.startswith('_')) and not (_is_dunder_attr):
                        if not (private_attrs or private_under_attrs or private_init_attrs or private_init_under_attrs):
                            continue
                    _is_dunder_attr = False # reset dunder check for single under's
                
                    # Build Data - Init Attrs
                    if __multiline_check(value) and indentation_on:
                        value = __cleanformat(value, indent_level)
                        __build_data_output_init += f'{key} {__assignment_glyphs.norm} {value}\n'
                    else: __build_data_output_init += f'{key} {__assignment_glyphs.norm} {repr(value)}\n'
                
            # Last: Class Attrs
            if class_attrs:
                for key,value in vars(type(data)).items():
                    # Strip Unneeded Attrs/Methods, and Preserve Dunders if Required
                    if callable(value): continue
                    if (key.startswith('__') and key.endswith('__')): continue
                    if key.startswith(f'_{type(data).__name__}'): # dunder detection (name mangle)
                        if (private_attrs) or (private_dunder_attrs) or (private_class_attrs) or (private_class_dunder_attrs):
                            key = key.removeprefix(f'_{type(data).__name__}')
                            _is_dunder_attr = True
                        else: continue
                    if (key.startswith('_')) and not (_is_dunder_attr):
                        if not (private_attrs or private_under_attrs or private_class_attrs or private_class_under_attrs):
                            continue
                    _is_dunder_attr = False # reset dunder check for single under's
                    
                    # Build Data - Class Attrs
                    if __multiline_check(value) and indentation_on:
                        value = __cleanformat(value, indent_level)
                        __build_data_output_class += f'{key} {__assignment_glyphs.norm} {value}\n'
                    else: __build_data_output_class += f'{key} {__assignment_glyphs.norm} {repr(value)}\n'

        # Structure Build
        if _is_case1_build: pass
        elif _is_case2_build: pass
        elif _is_case3_build:
            if not class_attrs:
                __build_data_output = __build_data_output_init 
            else: 
                __build_data_output = '\n'.join([
                                            _class_attr_header,
                                            __build_data_output_class,
                                            _init_attr_header,
                                            __build_data_output_init,
                                        ])
        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        # Return String Data
        return __build_data_output

    # Report if no __dict__ Attribute
    if not hasattr(data, '__dict__'):
        raise DumpStr(__err_msg_no_attrs_found, f'\nDATA: {data}')

    # Report if Error not Definable
    raise DumpStr(__err_msg_general_error, f'\nDATA: {data}')


#########################################################################################################
# Functions

# Multiline Check
def __multiline_check(data: __Union[list, dict, tuple, set]) -> bool:
    """
    Check if Multiline Type to Assist for Indentation
    """
    if isinstance(data, list) \
    or isinstance(data, dict) \
    or isinstance(data, tuple) \
    or isinstance(data, set):
        return True
    return False
