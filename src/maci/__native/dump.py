# dump
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from typing import Union as __Union
from typing import Any as __Any
from ..error import Dump, DumpRaw
from .load import MaciFileData as __MaciFileData
from .dumpraw import dumpraw as __dumpraw
from .cleanformat import cleanformat as __cleanformat

#########################################################################################################
# Save Data to File
class __MaciDummy:
    class Class: """dummy class for hinting"""

def dump(
    filename: str, 
    data: __Union['__MaciFileData', dict, '__MaciDummy.Class'], 
    write_mode: str = 'w',
    indent_level: int = 1,
    indentation_on: bool = True,
    verify_if_class_instantiated = True
    ) -> None:
    """
    Saves your Attr or Key/Value pair data to a file with the new data.

    Enter filename as str, Pass MaciFileData, dict, or custom class data type for output to file.

    [Importing Data Back] Functions:

    load: Import data back returning a class of attributes with Maci features

    loadattrs: Import attributes back into a custom class. This is done in-place

    [Options]

    write_mode:

    'w' = write new file with new data (Default)

    'a' = append new data to existing file

    indent_level: set indent level for types list, dict, tuple, set (Default 1)

    indentation_on: set to False to turn OFF indentation on types list, dict, tuple, set (Default ON)

    [Example Use]
    Normal: dump('path/of/filename', 'data')

    Append to File: dump('path/of/filename', 'data', write_mode='a')

    Indent OFF: dump('path/of/filename', 'data', indentation_on=False)
    """
    # Error Checks
    __err_msg_general_error = "Error has occurred and cannot proceed"
    __err_msg_no_attrs_found = "Cannot save file. No attributes found in the object passed"
    __err_msg_type_str_filename = "Only str is allowed for filename"
    __err_msg_type_str_write_mode = "Only str is allowed for write_mode"
    __err_msg_type_int_indent_level = "Only int is allowed for indent_level"
    __err_msg_type_bool_indentation_on = "Only bool is allowed for indentation_on"
    __err_msg_class_instance_error = "Seeing internal built-in names to save. Normally due to a class not being instantiated. If intentional, turn off check with 'verify_if_class_instantiated = False'"

    if not isinstance(filename, str): raise Dump(__err_msg_type_str_filename, f'\nFILE: "{filename}"')
    if not isinstance(write_mode, str): raise Dump(__err_msg_type_str_write_mode, f'\nFILE: "{filename}" \nDATA: {write_mode}')
    if not isinstance(indent_level, int): raise Dump(__err_msg_type_int_indent_level, f'\nFILE: "{filename}" \nDATA: {indent_level}')
    if not isinstance(indentation_on, bool): raise Dump(__err_msg_type_bool_indentation_on, f'\nFILE: "{filename}" \nDATA: {indentation_on}')


    # Save Data to File
    __build_data_output = ""
    __assignment_operators = ('=', '$=', '==', '$==')
    __skip_object_key = ('_MaciFileData', '__maci_file_format_id')
    __non_instance_names = ['__module__', '__init__']
    __locked_attr_list_key =  '_MaciFileData__assignment_locked_attribs'
    __reference_attr_list_key =  '_MaciFileData__assignment_reference_attribs'
    __maci_file_format_id_match = "48448910-fa49-45ca-bd3e-38d7af136af5-7bcece52-e5ee-4272-989d-103f07aa6c0f"


    ### MACI FILE DATA: Check if MaciFileData ###

    # Build Out Data
    if (isinstance(data, __MaciFileData)) and (data.__maci_file_format_id__ == __maci_file_format_id_match):
        for key,value in data.__dict__.items():
            # If Match Prefixes, Skip
            if not key.startswith(__skip_object_key):
                # Check Operator Type and Build Accordingly

                # Reference Name and Locked
                if (key in data.__dict__[__reference_attr_list_key]) and (key in data.__dict__[__locked_attr_list_key]):
                    __build_data_output += f'{key} {__assignment_operators[3]} {data.__dict__[__reference_attr_list_key][key]}\n'
                    continue
                # Reference Name Only
                if key in data.__dict__[__reference_attr_list_key]:
                    __build_data_output += f'{key} {__assignment_operators[2]} {data.__dict__[__reference_attr_list_key][key]}\n'
                    continue
                # Locked Only
                if key in data.__dict__[__locked_attr_list_key]:
                    if __multiline_check(value) and indentation_on:
                        value = __cleanformat(value, indent_level)
                        __build_data_output += f'{key} {__assignment_operators[1]} {value}\n'
                    else: __build_data_output += f'{key} {__assignment_operators[1]} {repr(value)}\n'
                    continue
                # Normal Assignment
                if __multiline_check(value) and indentation_on:
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_operators[0]} {value}\n'
                else: __build_data_output += f'{key} {__assignment_operators[0]} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        # Write File Data
        __write_file_data(filename, __build_data_output, write_mode)

        return None


    ### DICT: Check if dict ###
    if isinstance(data, dict):
        # Build Data
        for key,value in data.items():
            # Multline Assignment from Indentation
            if indentation_on:
                if __multiline_check(value):
                    value = __cleanformat(value, indent_level)
                    __build_data_output += f'{key} {__assignment_operators[0]} {value}\n'
                    continue
            # Single Line Assignment
            __build_data_output += f'{key} {__assignment_operators[0]} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        # Write File Data
        __write_file_data(filename, __build_data_output, write_mode)

        return None


    ### CLASS: Check if any Class Object with Attributes
    _filter_objects = (str, int, float, bool, list, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)
    if not isinstance(data, _filter_objects):
        # Build Data
        for key,value in data.__dict__.items():
            # Verify Class is Instantiated
            if verify_if_class_instantiated:
                if key in __non_instance_names:
                    raise Dump(__err_msg_class_instance_error, f'\nFILE: "{filename}" \nCLASS: {data} \nATTR_NAME: {key}')
            # Normal Assignment
            if __multiline_check(value) and indentation_on:
                value = __cleanformat(value, indent_level)
                __build_data_output += f'{key} {__assignment_operators[0]} {value}\n'
            else: __build_data_output += f'{key} {__assignment_operators[0]} {repr(value)}\n'

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        # Write File Data
        __write_file_data(filename, __build_data_output, write_mode)

        return None

    # Report if no __dict__ Attribute
    if not hasattr(data, '__dict__'):
        raise Dump(__err_msg_no_attrs_found, f'\nFILE: "{filename}" \nDATA: {data}')

    # Report if Error not Definable
    raise Dump(__err_msg_general_error, f'\nDATA: {data}')


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


# Write File Data
def __write_file_data(filename: str, data: __Any, write_mode: str) -> None:
    """
    Write New or Append Data to File
    """
    __err_msg_write_mode = 'Bad write mode'
    __write_mode_allowed_list = ['w', 'a']
    try:
        # Write New File Mode
        if write_mode == 'w':
            __dumpraw(filename, data)
        # Append Append File Mode
        if write_mode == 'a':
            __dumpraw(filename, data, mode='a')        
        # Raise Exception if No Match
        if not write_mode in __write_mode_allowed_list:
            raise Dump(__err_msg_write_mode, f'\nFILE: "{filename}" \nDATA: {write_mode}')
    except DumpRaw as __err_msg: raise Dump(__err_msg, '')
