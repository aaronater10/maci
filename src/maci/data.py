# data
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from typing import Any as _Any
from .error import Load, GeneralError, Hint

#########################################################################################################
# MaciDataObj Constructor
class _MaciDataObjConstructor:
    def __init__(
        self,
        filename: str,
        *,
        attrib_name_dedup: bool,
        _py_syntax_err_msg: str='',
        _name_preexists_err_msg: str='',
        _name_reference_does_not_exist_msg: str='',
        _assignment_locked_atrribs_err_msg: str='',
        _is_str_parse_request: bool=False,
        _str_data: str='',
        _is_build_request: bool=False,
        _is_hint_request: bool=False,
    ) -> None:
        # '__assignment_locked_attribs' MUST BE FIRST INIT ASSIGNMENT
        self.__assignment_locked_attribs = []
        self.__assignment_reference_attribs = {}
        self.__attrib_name_dedup = attrib_name_dedup
        self.__is_hint_request = _is_hint_request

        # One Time Generated using UUID4 mode from UUID Library.
        # This helps authenticity of MaciDataObj Object for Development aid
        self.__maci_file_format_id__ = "48448910-fa49-45ca-bd3e-38d7af136af5-7bcece52-e5ee-4272-989d-103f07aa6c0f"

        # Syntax/Usage Error Messages
        py_syntax_err_msg = _py_syntax_err_msg
        name_preexists_err_msg = _name_preexists_err_msg
        name_reference_does_not_exist = _name_reference_does_not_exist_msg
        self.__assignment_locked_atrribs_err_msg = _assignment_locked_atrribs_err_msg

        # HINT REQUEST: If this is an object hinting request,
        # then end the INIT here with above self.attributes intact
        if _is_hint_request: return None

        # BUILD REQUEST: If this is an object build request,
        # then end the INIT here with above self.attributes intact
        if _is_build_request: return None

        # STR PARSE REQUEST: If this is a str parse request,
        # then set 'file_data' to process the string same as a file would
        if _is_str_parse_request:
            file_data = _str_data.splitlines()
        
        # PARSE FILE: Assume this is a normal file parse if not string parse
        else:
            # Open and Import Config File Data into Object
            with open(filename, 'r') as file_data:
                file_data = file_data.read().splitlines()

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
        __eof_marker = file_data[-1]

        # Main File Loop
        for __file_data_line in file_data:

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
                            raise Load(name_preexists_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')

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

                    except SyntaxError: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')

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
                            raise Load(name_preexists_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')
                        
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
                        
                    except ValueError: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')
                    except AttributeError:
                        # REF_NAME: Ignores Comments to Display Attr Reference Name
                        raise Load(
                            name_reference_does_not_exist,
                            f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token} \nREF_NAME: {f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()}'
                        )
                    except SyntaxError: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}" \nATTRIB_NAME: {__var_token}')

            else: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}"')
    

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


#########################################################################################################
# Main MaciDataObj Reference

# Meta for structure references
class __MaciDataObj(type):
    def __repr__(self):
        return f"<class '{self.__module__}.{self.__name__}'>"

# Main Object Name Reference
class MaciDataObj(_MaciDataObjConstructor, metaclass=__MaciDataObj):
    def __init__(
        self,
        filename: str,
        *,
        attrib_name_dedup: bool,
        _py_syntax_err_msg: str='',
        _name_preexists_err_msg: str='',
        _name_reference_does_not_exist_msg: str='',
        _assignment_locked_atrribs_err_msg: str='',
        _is_str_parse_request: bool=False,
        _str_data: str='',
        _is_load_request: bool=False,
        _is_build_request: bool=False,
        _is_hint_request: bool=False,
    )-> None:
        __constructor_locked = True
        __constructor_locked = False if (
                                        _is_load_request            
                                        or _is_build_request
                                        or _is_hint_request
                                    ) else True

        # Error Messages
        _init_request_err_msg = "Unusable 'MaciDataObj' object. Only meant for hinting and not to be instantiated"
        _init_request_err_msg_help = "Use 'maci.hint.MaciDataObj' to hint type correctly"

        # Hint Error Report
        if __constructor_locked:
            raise Hint(_init_request_err_msg, f'\nFor hinting: {_init_request_err_msg_help}')

        # NORMAL REQUEST
        if not __constructor_locked:
            super().__init__(
                filename,
                attrib_name_dedup=attrib_name_dedup,
                _py_syntax_err_msg=_py_syntax_err_msg,
                _name_preexists_err_msg=_name_preexists_err_msg,
                _name_reference_does_not_exist_msg=_name_reference_does_not_exist_msg,
                _assignment_locked_atrribs_err_msg=_assignment_locked_atrribs_err_msg,
                _is_str_parse_request=_is_str_parse_request,
                _str_data=_str_data,
                _is_build_request=_is_build_request,
                _is_hint_request=_is_hint_request
            )
