# load
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from os import path as __path
from typing import Any as _Any
from ..error import Load, GeneralError

#########################################################################################################
# Import py Data from File
class MaciFileData:
    def __init__(self, filename: str, attrib_name_dedup: bool, __is_build_request: bool = False):
        # '__assignment_locked_attribs' MUST BE FIRST INIT ASSIGNMENT
        self.__assignment_locked_attribs = []
        self.__assignment_reference_attribs = {}
        self.__attrib_name_dedup = attrib_name_dedup

        # One Time Generated using UUID4 mode from UUID Library.
        # This helps authenticity of MaciFileData Object for Development aid
        self.__maci_file_format_id__ = "48448910-fa49-45ca-bd3e-38d7af136af5-7bcece52-e5ee-4272-989d-103f07aa6c0f"

        # Syntax/Usage Error Messages
        __py_syntax_err_msg = "Must have valid Python data types to import, or file's syntax is not formatted correctly"
        __name_preexists_err_msg = "Name already preexists. Must give unique attribute names in file"
        __name_reference_does_not_exist = "Name reference does not exist! Must reference attribute names in file that have been defined"
        self.__assignment_locked_atrribs_err_msg = "Value Locked! Attribute cannot be reassigned"

        # BUILD REQUEST: If this is a object build request,
        # then end the INIT here with above self.attributes intact
        if __is_build_request: return None

        # Open and Import Config File into Class Object then return the object        
        with open(filename, 'r') as f:
            f = f.read().splitlines()
        
        # Data Build Setup and Switches        
        __is_building_data_sw = False
        __body_build_data_sw = False
        __end_data_build_sw = False
        __build_data = ''

        # Markers
        __start_markers = ('[','{','(')
        __end_markers = (']','}',')')
        __skip_markers = ('',' ','#','\n')
        __assignment_operator_markers = ('=', '$=', '==', '$==')
        __eof_marker = f[-1]

        # Main File Loop
        for __file_data_line in f:

            # Set Skip Marker
            try: __skip_marker = __file_data_line[0]
            except IndexError: __skip_marker = ''

            # Skip Any Comments, Blanks, and New Lines
            if (__is_building_data_sw == False) and (__skip_marker in __skip_markers): continue

            # Set Assignment Operator
            try: 
                __assignment_operator = __file_data_line.split()[1]
            except IndexError: __assignment_operator = ''

            # Basic Syntax Check, or if in a Multiline Build
            if (__assignment_operator in __assignment_operator_markers) or (__is_building_data_sw):

                if not __is_building_data_sw:
                    __current_assignment_operator = __assignment_operator
                    __var_token = __file_data_line.split(__assignment_operator)[0].strip()
                    __value_token = __file_data_line.split(__assignment_operator)[1].strip()
                    __value_token_multi = __file_data_line.split(__assignment_operator)[1].split()[0].strip()
                    __last_token = __file_data_line.split(__assignment_operator)[-1].strip()
                    try: __start_skip_token = __file_data_line.split(__assignment_operator)[1].split()[1][0].strip()
                    except IndexError: __start_skip_token = ''
                    
                if __is_building_data_sw:
                    try: __end_token = __file_data_line[0]
                    except IndexError: __end_token = ''
                
                # Verify Assignment Operator is Not Attr Reference for Multiline Build Check
                is_attr_reference_operator = False
                if (__current_assignment_operator == __assignment_operator_markers[2]) \
                or (__current_assignment_operator == __assignment_operator_markers[3]):
                    is_attr_reference_operator = True
                
                # START BUILD: Check if value in file line is only Start Marker. Check if Multiline or Single Line
                if (__value_token_multi in __start_markers) \
                and ((__last_token in __start_markers) or (__start_skip_token[0] in __skip_markers)) \
                and (__is_building_data_sw == False) \
                and not (is_attr_reference_operator):
                    
                    if (self.__attrib_name_dedup) and (hasattr(self, __var_token)):
                            raise Load(__name_preexists_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')

                    __build_data = __value_token
                    
                    # Turn ON Data Build Switches
                    __is_building_data_sw = True
                    __body_build_data_sw = True
                    __end_data_build_sw = True
                    continue
                
                # END BUILD: Check if line of file is an End Data Build Marker. Import Built Data Type if Valid. Check if EOF in case File Missing End Marker.
                elif (__end_data_build_sw) and ((__end_token in __end_markers) or (f"{__eof_marker}" == f"{__file_data_line}")):
                    __build_data += f"\n{__file_data_line}"
                    
                    try:
                        # Assign Attr
                        setattr(self, __var_token, __literal_eval__(__build_data))

                        # Check if Attr is Locked from Re-Assignment
                        if __current_assignment_operator == __assignment_operator_markers[1]:
                            self.__assignment_locked_attribs.append(__var_token)

                    except SyntaxError: raise Load(__py_syntax_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')

                    # Turn OFF Data Build Switches
                    __is_building_data_sw = False
                    __body_build_data_sw = False
                    __end_data_build_sw = False
                    __build_data = ''
                    continue

                # CONT BUILD: Continue to Build Data
                elif __body_build_data_sw:
                    __build_data += f"\n{__file_data_line}"
                    
                # IMPORT SINGLE LINE VALUES: If not multiline, assume single
                else:
                    try:
                        # Check if Attr Dedup
                        if (self.__attrib_name_dedup) and (hasattr(self, __var_token)):
                            raise Load(__name_preexists_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')
                        
                        # Check if Attr is a Reference to Another Attr's Value for Assignment. Ignore Comments
                        if __current_assignment_operator == __assignment_operator_markers[2]:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assignment_reference_attribs[__var_token] = __value_token
                            continue
                        # Check if Attr is a Reference to Another Attr's Value for Assignment and Locked from Re-Assignment. Ignore Comments
                        if __current_assignment_operator == __assignment_operator_markers[3]:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assignment_reference_attribs[__var_token] = __value_token
                            self.__assignment_locked_attribs.append(__var_token)
                            continue

                        # Assign Attr
                        setattr(self, __var_token, __literal_eval__(__value_token))

                        # Check if Attr is Locked from Re-Assignment
                        if __current_assignment_operator == __assignment_operator_markers[1]:
                            self.__assignment_locked_attribs.append(__var_token)
                        
                    except ValueError: raise Load(__py_syntax_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')
                    except AttributeError:
                        # REF_NAME: Ignores Comments to Display Attr Reference Name
                        raise Load(
                            __name_reference_does_not_exist,
                            f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token} \nREF_NAME: {f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()}'
                        )
                    except SyntaxError: raise Load(__py_syntax_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')

            else: raise Load(__py_syntax_err_msg, f'\nFILE: "{filename}"')
    

    def __setattr__(self, _name: str, _new_value: _Any) -> None:
        # Check if Attr Already Exists, if so, Collect Original Value
        if _name in self.__dict__:
            _orig_value = self.__dict__.get(_name)
            
        # Release Attribute Reference if Name is Re-Assigned
        if _name in self.__dict__:
            self.__reference_deletion_check(_name)

        # Always Assign Value 
        self.__dict__[_name] = _new_value

        # If attr was added to lock list after first assignment, assign orig value back, and raise exception
        # Exception can be caught/bypassed, setting original value is vital to protect value
        if _name in self.__assignment_locked_attribs:
            # PROTECT ORIGINAL VALUE
            self.__dict__[_name] = _orig_value
            # RAISE EXCEPTION
            raise Load(self.__assignment_locked_atrribs_err_msg, f'\nATTRIB_NAME: "{_name}"')


    def lock_attr(self, attr_name: str) -> None:
        """
        Lock's a class attribute name from re-assignment
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_attr_name_exist = "Locked attribute name does not exist! Must be created first to lock"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nATTR_NAME: "{attr_name}"')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nATTR_NAME: "{attr_name}"')

        # Assign Attr to Locked List
        self.__assignment_locked_attribs.append(attr_name)


    def unlock_attr(self, attr_name: str) -> None:
        """
        Unlocks a class attribute name from locked re-assignment
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_attr_name_exist = "Unlock attribute name does not exist"
        __err_msg_attr_name_exist_unlock = "Unlock attribute name does not exist in lock! Could not find name to unlock"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nATTR_NAME: "{attr_name}"')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nATTR_NAME: "{attr_name}"')

        # Remove Attr from Locked List
        try: self.__assignment_locked_attribs.remove(attr_name)
        except ValueError: raise GeneralError(__err_msg_attr_name_exist_unlock, f'\nATTR_NAME: "{attr_name}"')


    def reference_attr(self, attr_name: str, reference_name: str) -> None:
        """
        Create reference of class attribute name to another attribute name value from this object

        This will also assign the value of the reference name to the attribute

        Useful to maintain name references stored to a file
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_reference_name_str = "Only str is allowed for reference_name"
        __err_msg_attr_name_exist = "Source attribute name does not exist! Must be created first to assign reference"
        __err_msg_reference_name_exist = "Reference attribute name does not exist! Cannot assign value reference"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nATTR_NAME: "{attr_name}"')
        if not isinstance(reference_name, str): raise GeneralError(__err_msg_reference_name_str, f'\nATTR_NAME: "{reference_name}"')

        # Look up if Attr or Reference Name Exists
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nATTR_NAME: "{attr_name}"')
        if not reference_name in self.__dict__: raise GeneralError(__err_msg_reference_name_exist, f'\nATTR_NAME: "{reference_name}"')

        # Set Value to Reference Value
        setattr(self, attr_name, getattr(self, reference_name))
    
        # Assign Attr Name to Reference Name in Reference Dict
        self.__assignment_reference_attribs[attr_name] = reference_name


    def __reference_deletion_check(self, _name: str):
        """
        Internal method: check if reference requires deletion from reference list
        if attribute is attempted to be re-assigned
        """
        if _name in self.__assignment_reference_attribs.keys():
            self.__assignment_reference_attribs.pop(_name, None)


def load(filename: str, attrib_name_dedup: bool=True) -> 'MaciFileData':
    """
    Imports saved python data from any text file.

    Returns a class of attributes. Assign the output to var

    Enter file location as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes

    Returns None if file empty

    [Example Use]
    load('filename.data' or 'path/to/filename.data')
    """
    __err_msg_file = 'Invalid data type or nothing specified for filename:'
    __err_msg_attrib = 'Invalid data type or nothing specified for attrib_name_dedup:'
    
    # Error Checks
    if not isinstance(filename, str): raise Load(__err_msg_file, f'\nFILE: "{filename}"')
    if not isinstance(attrib_name_dedup, bool): raise Load(__err_msg_attrib, f'\nDATA: {attrib_name_dedup}')

    # Check if file empty. Returns None if empty
    try:
        if __path.getsize(filename) == 0:
            return None
    except FileNotFoundError as __err_msg: raise Load(__err_msg, f'\nFILE: "{filename}"')

    # Return Final Import
    return MaciFileData(filename, attrib_name_dedup)
