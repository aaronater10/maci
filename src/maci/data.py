# data
#########################################################################################################
# Imports

# MaciDataObj
from ast import literal_eval as _literal_eval
from datetime import datetime as _datetime
from datetime import date as _datetime_date
from datetime import time as _datetime_time
from copy import deepcopy as _deepcopy
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List
from typing import Union as _Union
from typing import Optional as _Optional
from typing import NamedTuple as _NamedTuple
from typing import Set as _Set
from typing import Callable as _Callable
from .error import Load, GeneralError, Hint
# Dump Function
from io import StringIO as _StringIO
from typing import TypeVar as _TypeVar
from ._native.dumpraw import dumpraw as _dumpraw
from ._native.cleanformat import cleanformat as _cleanformat
from .error import Dump, DumpRaw, DumpStr

#########################################################################################################
# Assignment Glyphs
class _Glyphs(_NamedTuple):
    """
    Core assignment glyphs -> NamedTuple

    Glyph processing order is critical for performance and stability and must be maintained

    Any glyph closer to the top of the list will have the greatest
    performance gain in the current design implementation

    Order is as follows with reasons:

    Normal -> Letter -> Symbol ('==' is the exception reasons below)

    1. == -> must be above '=' assignment glyph to not get incorrectly parsed

    2. = -> must be below '==' to not incorrectly parse assignment glyph

    3..9. +<letter(s)>= purely preference as they do not step over each other, but letter
    syntax is preferred to be evaluated first over symbols

    10. $$== -> must be above '$$=' assignment glyph to not get incorrectly parsed

    11. $$= -> must be below '$$==' to not incorrectly parse assignment glyph

    12. $== -> must be above '$=' assignment glyph to not get incorrectly parsed

    13. $= -> must be below '$==' to not incorrectly parse assignment glyph
    """
    ### Core Glyphs ###
    ref: str = '=='
    norm: str = '='
    m: str = '+m='
    h: str = '+h='
    l: str = '+l='
    mh: str = '+mh='
    ml: str = '+ml='
    hm: str = '+hm='
    lm: str = '+lm='
    ref_hard_lock: str = '$$=='
    hard_lock: str = '$$='
    ref_lock: str = '$=='
    lock: str = '$='

    # Mixed Case Scenarios for Glyph Checks
    @staticmethod
    def get_mixed_case_set() -> _Set[str]:
        return {'+mL=', '+Ml=', '+mH=', '+Mh=', '+lM=', '+Lm=', '+hM=', '+Hm='}


#########################################################################################################
# Method Wrapper for '_MaciDataObjConstructor' -> 'MaciDataObj' Name
def _rename_exc_name_to_user_object_name(method: _Callable[..., _Any]) -> _Callable[..., _Any]:
    def wrapper(*args: _Any, **kwargs: _Any) -> _Callable[..., _Any]:
        # Setup
        build_err_msg = ''
        search_name = '_MaciDataObjConstructor'
        replace_name = 'MaciDataObj'
        # Exception Names - Add to it as needed
        exception_names_to_catch = (TypeError,)

        # Report with replaced name in output if found and caught
        try:
            return_data = method(*args, **kwargs)
        except exception_names_to_catch as exception:
            for exc_msg in exception.args:
                if '_MaciDataObjConstructor' in exc_msg: # pragma: no cover  # py37-39 does not show obj name in msg
                    build_err_msg += exc_msg.replace(search_name, replace_name)
                    continue
                build_err_msg += exc_msg # pragma: no cover  # hits as a catch-all for py37-39
            # Raise with final message and original Exception Type. Remove Double-Trace as it is a Duplicate
            raise type(exception)(build_err_msg) from None
        return return_data
    return wrapper


#########################################################################################################
# MaciDataObj Functions
def _date_time_parse_check(value: str) -> _Union[_datetime, _datetime_date, _datetime_time, None]:
    """
    Check if supported custom datetime format, or ISO8601 format

    Returns datetime obj if found. Otherwise None
    """
    custom_date_time_formats = {
        'date_time': '%Y-%m-%d %H:%M:%S',
        'date_timem': '%Y-%m-%d %H:%M:%S.%f',
        'date': '%Y-%m-%d',
        'time': '%H:%M:%S',
        'timem': '%H:%M:%S.%f',
        'time_date': '%H:%M:%S %Y-%m-%d',
        'timem_date': '%H:%M:%S.%f %Y-%m-%d',
    }

    for format_type, format_str in custom_date_time_formats.items():
        try:
            datetime_object = _datetime.strptime(value, format_str)
            if format_type == 'date_time': return datetime_object
            if format_type == 'date_timem': return datetime_object
            if format_type == 'date': return datetime_object.date()
            if format_type == 'time': return datetime_object.time()
            if format_type == 'timem': return datetime_object.time()
            if format_type == 'time_date': return datetime_object
            if format_type == 'timem_date': return datetime_object # pragma: no branch
        except ValueError: continue
    else:
        try: return _datetime.fromisoformat(value)
        except ValueError: return None


#########################################################################################################
# MaciDataObj Constructor
class _MaciDataObjConstructor:
    # Protect Internal Attrs and Methods from Re-Assignment Listed Names
    __internal_check_lists_setattr_maci_names = {
        '_MaciDataObjConstructor__assignment_hard_locked_attribs',
        '_MaciDataObjConstructor__assignment_locked_attribs',
        '_MaciDataObjConstructor__assigned_src_reference_attr_map',
        '_MaciDataObjConstructor__assigned_dst_reference_attr_map',
        '_MaciDataObjConstructor__reference_deletion_check',
    }
    # Protect Internal Method Names from Re-Assignment Listed Names
    __internal_check_lists_setattr_maci_methods = {
        'hard_lock_attr',
        'lock_attr',
        'unlock_attr',
        'map_attr',
        'unmap_attr',
        'get_all_maps',
        'get_parent_maps',
        'get_child_maps',
        'get_parent_map_chains',
        'get_locked_list',
        'get_hard_locked_list',
        'is_parent_map',
        'is_child_map',
    }
    # Protect Internal List/Reference Attrs from Deletion Listed Names
    __internal_check_lists_delattr = {
            '_MaciDataObjConstructor__assignment_hard_locked_attribs',
            '_MaciDataObjConstructor__assignment_locked_attribs',
            '_MaciDataObjConstructor__assigned_src_reference_attr_map',
            '_MaciDataObjConstructor__assigned_dst_reference_attr_map'
    }

    # Main Constructor
    def __init__(
        self,
        filename: str,
        *,
        attr_name_dedup: bool,
        encoding: _Union[str, None],
        _py_syntax_err_msg: str='',
        _name_preexists_err_msg: str='',
        _name_reference_does_not_exist_msg: str='',
        _assignment_locked_atrribs_err_msg: str='',
        _assignment_hard_locked_atrribs_err_msg: str='',
        _is_str_parse_request: bool=False,
        _str_data: str='',
        _is_build_request: bool=False,
        _ignore_internal_maci_attr_check: bool=False
    ) -> None:
        # Setup: Reference lists and maps should be first assignment
        self.__assignment_locked_attribs: _Set[str] = set()
        self.__assignment_hard_locked_attribs: _Set[str] = set()
        self.__assigned_src_reference_attr_map: _Dict[str, str] = {}
        self.__assigned_dst_reference_attr_map: _Dict[str, _Dict[str, str]] = {}
        self.__attrib_name_dedup = attr_name_dedup
        self.__ignore_internal_maci_attr_check = _ignore_internal_maci_attr_check

        # One Time Generated using UUID4 mode from UUID Library.
        # This helps authenticity of MaciDataObj Object for Development aid
        self.__maci_obj_format_id__ = "48448910-fa49-45ca-bd3e-38d7af136af5-7bcece52-e5ee-4272-989d-103f07aa6c0f"

        # Syntax/Usage Error Messages
        py_syntax_err_msg = _py_syntax_err_msg
        name_preexists_err_msg = _name_preexists_err_msg
        name_reference_does_not_exist = _name_reference_does_not_exist_msg
        self.__assignment_locked_atrribs_err_msg = _assignment_locked_atrribs_err_msg
        self.__assignment_hard_locked_atrribs_err_msg = _assignment_hard_locked_atrribs_err_msg

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
            with open(filename, 'r', encoding=encoding) as loaded_file_data:
                file_data = loaded_file_data.read().splitlines()

        # Data Build Setup and Switches        
        __is_building_data_sw = False
        __body_build_data_sw = False
        __end_data_build_sw = False
        __build_data = ''

        # Markers
        __start_markers = {'[', '{', '(', "'''", '"""'}
        __end_markers = {']', '}', ')', "'''", '"""'}
        __end_multistr_markers = {"'''", '"""'}
        __end_markers_build = __end_markers
        __skip_markers = ('', ' ', '#', '\n')
        __eof_marker = file_data[-1]
        __ignore_multistr_markers = ("'''", '"""')
        __ignore_multistr_marker = ''

        # Assignment Glyphs - Set by Another Class and is a NamedTuple
        __assignment_glyphs = _Glyphs()

        # Glyph Checks for Internal Mechs
        _assignment_glyphs_for_any_checks = set(__assignment_glyphs)
        _assignment_glyphs_for_all_ref_checks = {
            __assignment_glyphs.ref,
            __assignment_glyphs.ref_lock,
            __assignment_glyphs.ref_hard_lock,
            __assignment_glyphs.m,
            __assignment_glyphs.ml,
            __assignment_glyphs.lm,
            __assignment_glyphs.mh,
            __assignment_glyphs.hm
        }
        _assignment_glyphs_for_ref_checks = {__assignment_glyphs.ref, __assignment_glyphs.m}
        _assignment_glyphs_for_ref_lock_checks = {__assignment_glyphs.ref_lock, __assignment_glyphs.ml, __assignment_glyphs.lm}
        _assignment_glyphs_for_ref_hard_lock_checks = {__assignment_glyphs.ref_hard_lock, __assignment_glyphs.mh, __assignment_glyphs.hm}
        _assignment_glyphs_for_lock_checks = {__assignment_glyphs.lock, __assignment_glyphs.l}
        _assignment_glyphs_for_hard_lock_checks = {__assignment_glyphs.hard_lock, __assignment_glyphs.h}
        _assignment_glyphs_for_mixed_cases = __assignment_glyphs.get_mixed_case_set()


        # Main File/Str Loop
        # To display correct line number start=1
        for line_num,__file_data_line in enumerate(file_data, start=1):

            # Set Skip Marker
            try:
                __skip_marker = __file_data_line[0]
                potential_name_char = __file_data_line.lstrip()[0]
            except IndexError: __skip_marker = ''
            else:
                # Check if there is a leading blank with data on same line
                if (__skip_marker in __skip_markers) and (potential_name_char not in __skip_markers) and (__is_building_data_sw == False):
                    raise Load(
                            py_syntax_err_msg,
                            f'\nFile: {repr(filename)} \nLine: {line_num} \nGot: {repr(__file_data_line)}'
                        )

            # Skip Any Comments, Blanks, and New Lines. Do not skip during a muli-line build
            if (__is_building_data_sw == False) and (__skip_marker in __skip_markers): continue

            # Set Assignment Glyph: Checks valid syntax, and checks if glyph is uppercase
            if (__is_building_data_sw == False):
                for _glyph in __assignment_glyphs:
                    if __file_data_line.lower().partition(_glyph)[0].strip().isidentifier():
                        # Pull Indices of Raw Glyph
                        idx_start = __file_data_line.lower().find(_glyph)
                        idx_end = __file_data_line.lower().find(_glyph) + len(_glyph)
                        glyph_from_data = __file_data_line[idx_start:idx_end]

                        # Ensure Raw Glyph meets glyph criteria, else empty it
                        if __assignment_glyphs.norm not in glyph_from_data: glyph_from_data = ''

                        # Assume Mixed if if both Upper and lower
                        if glyph_from_data in _assignment_glyphs_for_mixed_cases:
                            __assignment_glyph = glyph_from_data
                            break

                        # Assume Upper if empty
                        if glyph_from_data.isupper():
                            __assignment_glyph = _glyph.upper()
                            break
                        
                        # Assume is lower, or if Symbol
                        __assignment_glyph = _glyph
                        break
                # Not found, then empty
                else: __assignment_glyph = ''

            # Basic Syntax Check, or if in a Multiline Build
            if (__assignment_glyph.lower() in _assignment_glyphs_for_any_checks) or (__is_building_data_sw):

                if not __is_building_data_sw:

                    # Check if Value Empty
                    if __file_data_line.partition(__assignment_glyph)[2].strip() == '':
                        raise Load(
                            py_syntax_err_msg,
                            f'\nFile: {repr(filename)} \nLine: {line_num} \nAttr: {__file_data_line.partition(__assignment_glyph)[0].strip()} \nGot: {repr(__file_data_line)}'
                        )
                    
                    __current_assignment_glyph = __assignment_glyph.lower()
                    __var_token = __file_data_line.partition(__assignment_glyph)[0].strip()
                    __value_token = __file_data_line.partition(__assignment_glyph)[2].strip()
                    __value_token_multi = __file_data_line.partition(__assignment_glyph)[2].partition(__skip_markers[2])[0].strip()

                    # Set Last Token with Accommodation to Multi-Line String
                    if __file_data_line.partition(__assignment_glyph)[2].strip()[-3:] in __start_markers:
                        __last_token = __file_data_line.partition(__assignment_glyph)[2].strip()[-3:]
                    else:
                        __last_token = __file_data_line.partition(__assignment_glyph)[2].strip().rpartition(__skip_markers[2])[0].strip()
                    
                    try: __start_skip_token = __file_data_line.split(__assignment_glyph)[1].split()[1][0].strip()
                    except IndexError: __start_skip_token = ''  # nosec: B105  # not password
                
                # Collect End Token if in Build
                if __is_building_data_sw:
                    try:
                        if __file_data_line[0] in __end_markers:
                            __end_token = __file_data_line[0]
                        elif __file_data_line[0:3] in __end_markers:
                            __end_token = __file_data_line[0:3]
                        else: __end_token = ''  # nosec: B105  # not password
                    except IndexError: __end_token = ''  # nosec: B105  # not password
                
                # Verify Assignment Glyph is Not Attr Reference for Multiline Build Check
                is_attr_reference_glyph = False
                if __current_assignment_glyph in _assignment_glyphs_for_all_ref_checks:
                    is_attr_reference_glyph = True

                
                ### START BUILD: Check if value in file line is only Start Marker. Check if Multiline or Single Line
                if (__value_token_multi in __start_markers) \
                and ((__last_token in __start_markers) or (__start_skip_token[0] in __skip_markers)) \
                and (__is_building_data_sw == False) \
                and not (is_attr_reference_glyph):
                    
                    # Check if Attr Dedup
                    if (self.__attrib_name_dedup) and (hasattr(self, __var_token)):
                            raise Load(name_preexists_err_msg, f'\nFile: {repr(filename)} \nLine: {line_num} \nAttr: {__var_token}')

                    # Check for Comment
                    if __skip_markers[2] in __value_token:
                        __value_token = __value_token.partition(__skip_markers[2])[0].strip()
                    
                    # Check if starting a build with no remaining lines to read
                    if (len(file_data) == line_num):
                        raise Load(py_syntax_err_msg, f'\nFile: {repr(filename)} \nLine: {line_num} \nAttr: {__var_token}')
                    
                    # Set First Value
                    __build_data = __value_token

                    # Swap ignore type if multi-str. If triple-singles, then ignore triple-doubles and vice-versa
                    if __ignore_multistr_markers[0] == __value_token: __ignore_multistr_marker = __ignore_multistr_markers[1]
                    if __ignore_multistr_markers[1] == __value_token: __ignore_multistr_marker = __ignore_multistr_markers[0]

                    # Turn ON/UPDATE Data Build Switches
                    __is_building_data_sw = True
                    __body_build_data_sw = True
                    __end_data_build_sw = True
                    if __value_token in __end_multistr_markers: # pragma: no branch
                        __end_markers_build = __end_multistr_markers
                    continue

                ### END BUILD: Check if line of file is an End Data Build Marker. Import Built Data Type if Valid. Check if EOF in case File Missing End Marker.
                elif (__end_data_build_sw) and (((__end_token in __end_markers_build) and (not __end_token == __ignore_multistr_marker)) or (f"{__eof_marker}" == f"{__file_data_line}")):
                    __build_data += f"\n{__file_data_line}"

                    try:
                        # Assign Attr
                        setattr(self, __var_token, _literal_eval(__build_data))

                        # Check if Attr is Locked from Re-Assignment
                        if __current_assignment_glyph in _assignment_glyphs_for_lock_checks:
                            self.__assignment_locked_attribs.add(__var_token)

                        # Check if Attr is Hard Locked from Re-Assignment
                        if __current_assignment_glyph in _assignment_glyphs_for_hard_lock_checks:
                            self.__assignment_hard_locked_attribs.add(__var_token)

                    except SyntaxError: raise Load(py_syntax_err_msg, f'\nFile: {repr(filename)} \nLine: {line_num} \nAttr: {__var_token}')

                    # Turn OFF/UPDATE Data Build Switches
                    __is_building_data_sw = False
                    __body_build_data_sw = False
                    __end_data_build_sw = False
                    __build_data = ''
                    __end_markers_build = __end_markers
                    continue

                ### CONT BUILD: Continue to Build Data
                elif __body_build_data_sw:
                    __build_data += f"\n{__file_data_line}"
                    
                
                ### IMPORT SINGLE LINE VALUES: If not multiline, assume single
                else:
                    try:
                        # Check if Attr Dedup
                        if (self.__attrib_name_dedup) and (hasattr(self, __var_token)):
                            raise Load(name_preexists_err_msg, f'\nFile: {repr(filename)} \nLine: {line_num} \nAttr: {__var_token}')
                        
                        # Check if Attr is a Reference to Another Attr's Value for Assignment. Ignore Comments
                        if __current_assignment_glyph in _assignment_glyphs_for_ref_checks:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assigned_src_reference_attr_map[__var_token] = __value_token
                            self.__assigned_dst_reference_attr_map.setdefault(__value_token, {}).setdefault(__var_token, __value_token)
                            continue
                        
                        # Check if Attr is a Reference to Another Attr's Value for Assignment and Locked from Re-Assignment. Ignore Comments
                        if __current_assignment_glyph in _assignment_glyphs_for_ref_lock_checks:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assigned_src_reference_attr_map[__var_token] = __value_token
                            self.__assigned_dst_reference_attr_map.setdefault(__value_token, {}).setdefault(__var_token, __value_token)
                            self.__assignment_locked_attribs.add(__var_token)
                            continue
                        
                        # Check if Attr is a Reference to Another Attr's Value for Assignment and Hard Locked from Re-Assignment. Ignore Comments
                        if __current_assignment_glyph in _assignment_glyphs_for_ref_hard_lock_checks:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assigned_src_reference_attr_map[__var_token] = __value_token
                            self.__assigned_dst_reference_attr_map.setdefault(__value_token, {}).setdefault(__var_token, __value_token)
                            self.__assignment_hard_locked_attribs.add(__var_token)
                            continue

                        # Assign Attr
                        setattr(self, __var_token, _literal_eval(__value_token))

                        # Check if Attr is Locked from Re-Assignment
                        if __current_assignment_glyph in _assignment_glyphs_for_lock_checks:
                            self.__assignment_locked_attribs.add(__var_token)

                        # Check if Attr is Hard Locked from Re-Assignment
                        if __current_assignment_glyph in _assignment_glyphs_for_hard_lock_checks:
                            self.__assignment_hard_locked_attribs.add(__var_token)
                        
                    except AttributeError:
                        # Reference Name: Ignores Comments to Display Attr Reference Name
                        raise Load(
                            name_reference_does_not_exist,
                            f'\nFile: {repr(filename)} \nLine: {line_num} \nAttr: {__var_token} \nMap_Name: {f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()}'
                        )
                    except (ValueError, SyntaxError):
                        # Check if datetime format and set attr, else raise exception
                        datetime_format =_date_time_parse_check(__value_token)
                        if datetime_format is not None:
                            # Assign Attr to datetime object
                            setattr(self, __var_token, datetime_format)
                        else:
                            raise Load(py_syntax_err_msg, f'\nFile: {repr(filename)} \nLine: {line_num} \nAttr: {__var_token}')

            else: raise Load(py_syntax_err_msg, f'\nFile: {repr(filename)} \nLine: {line_num}')
    


    def __getattr__(self, _name: str) -> _Any:
        if _name in self.__dict__:  # pragma: no cover  # not evaluating but is used/operating
            return self.__dict__[_name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{_name}'")


    def __setattr__(self, _name: str, _new_value: _Any) -> None:
        # Check if Attr Already Exists, if so, Collect Original Value
        if hasattr(self, _name):
            _orig_value = self.__dict__.get(_name)
            
        # Release Attribute Reference if Name is Re-Assigned
        if hasattr(self, _name):
            self.__reference_deletion_check(_name, _src_ref_list=True)

        # Protect Internal List/Reference Attrs and Methods from Re-Assignment
        if hasattr(self, _name) and (_name in _MaciDataObjConstructor.__internal_check_lists_setattr_maci_names):
            raise GeneralError('Cannot re-assign internal MaciDataObj attribute name!', f'\nAttr: {repr(_name)}')
        
        # Protect Internal Method Names from Re-Assignment. Can be switched OFF by User
        if hasattr(self, _name) and (_name in _MaciDataObjConstructor.__internal_check_lists_setattr_maci_methods) and (not self.__ignore_internal_maci_attr_check):
            raise GeneralError('Cannot re-assign internal MaciDataObj method name!', f'\nMethod_Name: {repr(_name)}')


        # Always Assign Value 
        self.__dict__[_name] = _new_value


        # If attr was added to lock/hard_lock list after first assignment, assign orig value back, and raise exception
        # Exception can be caught/bypassed, setting original value is vital to protect value

        # General Lock Protection
        if hasattr(self, '_MaciDataObjConstructor__assignment_locked_attribs'): # pragma: no branch
            if _name in self.__assignment_locked_attribs:
                # PROTECT ORIGINAL VALUE
                self.__dict__[_name] = _orig_value
                # RAISE EXCEPTION
                raise GeneralError(self.__assignment_locked_atrribs_err_msg, f'\nAttr: {repr(_name)}')

        # Hard Lock Protection
        if hasattr(self, '_MaciDataObjConstructor__assignment_hard_locked_attribs'):
            if _name in self.__assignment_hard_locked_attribs:
                # PROTECT ORIGINAL VALUE
                self.__dict__[_name] = _orig_value
                # RAISE EXCEPTION
                raise GeneralError(self.__assignment_hard_locked_atrribs_err_msg, f'\nAttr: {repr(_name)}')
        
        # Always Re-Reference Attr New Value if Source not Locked
        if hasattr(self, '_MaciDataObjConstructor__assigned_dst_reference_attr_map'):
            if _name in self.__assigned_dst_reference_attr_map:
                for key in self.__assigned_dst_reference_attr_map[_name]:
                    collected_references = []
                    collected_references.append(key)

                    # Check if the Child Reference is Parent of Other Child References
                    other_ref_name = key
                    other_child_ref_name_track = []
                    while other_ref_name in self.__assigned_dst_reference_attr_map:
                        for other_child_ref_name in self.__assigned_dst_reference_attr_map[other_ref_name]:
                            collected_references.append(other_child_ref_name)
                            other_child_ref_name_track.append(other_child_ref_name)
                        
                        other_ref_name = other_child_ref_name_track.pop()


                    # Assign New Value to All Child or Chained References and Verify None are Locked
                    for ref_name in collected_references:
                        # If Source is Locked, Block Update
                        _is_locked = ref_name in self.__assignment_locked_attribs
                        _is_hard_locked = ref_name in self.__assignment_hard_locked_attribs
                        if _is_locked: raise GeneralError(self.__assignment_locked_atrribs_err_msg, f'\nAttr: {repr(ref_name)}')
                        if _is_hard_locked: raise GeneralError(self.__assignment_hard_locked_atrribs_err_msg, f'\nAttr: {repr(ref_name)}')

                        # Update Reference(s) to New Value
                        self.__dict__[ref_name] = _new_value
    
    
    def __delattr__(self, _name: str) -> None:
        # Protect Internal List/Reference Attrs from Deletion
        if _name in _MaciDataObjConstructor.__internal_check_lists_delattr:
            raise GeneralError('Cannot delete internal MaciDataObj attribute name!', f'\nAttr: {repr(_name)}')

        # Protect Hard Locked Attr from Deletion
        if _name in self.__assignment_hard_locked_attribs:
            # RAISE EXCEPTION
            raise GeneralError(self.__assignment_hard_locked_atrribs_err_msg, f'\nAttr: {repr(_name)}')

        # Release Attribute from Lock & Reference List if Name is Deleted
        if hasattr(self, _name): # pragma: no branch
            self.__reference_deletion_check(_name, _src_ref_list=True, _dst_ref_list=True, _lock_list=True)

        # Allow Normal Deletion
        super().__delattr__(_name)


    @_rename_exc_name_to_user_object_name
    def hard_lock_attr(self, attr_name: str) -> None:
        """
        Hard lock's an attribute name from re-assignment, deletion, and cannot be unlocked
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_attr_name_exist = "Hard locked attribute name does not exist! Must be created first to lock"
        __err_msg_attr_name_locked = "Attribute name already hard locked! Cannot be re-locked once locked"
        __err_msg_attr_name_other_lock = "Attribute name exists with other lock (lock_attr) already! Cannot be locked with multiple locks"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nAttr: {repr(attr_name)}')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nAttr: {repr(attr_name)}')

        # Assign Attr to Locked Tuple if Does Not Preexist
        if attr_name in self.__assignment_hard_locked_attribs:
            raise GeneralError(__err_msg_attr_name_locked, f'\nAttr: {repr(attr_name)}')
        if attr_name in self.__assignment_locked_attribs:
            raise GeneralError(__err_msg_attr_name_other_lock, f'\nAttr: {repr(attr_name)}')

        self.__assignment_hard_locked_attribs.add(attr_name)


    @_rename_exc_name_to_user_object_name
    def lock_attr(self, attr_name: str) -> None:
        """
        Lock's an attribute name from re-assignment
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_attr_name_exist = "Locked attribute name does not exist! Must be created first to lock"
        __err_msg_attr_name_locked = "Attribute name already locked! Cannot be re-locked once locked"
        __err_msg_attr_name_other_lock = "Attribute name exists with other lock (hard_lock_attr) already! Cannot be locked with multiple locks"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nAttr: {repr(attr_name)}')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nAttr: {repr(attr_name)}')

        # Assign Attr to Locked List if Does Not Preexist
        if attr_name in self.__assignment_locked_attribs:
            raise GeneralError(__err_msg_attr_name_locked, f'\nAttr: {repr(attr_name)}')
        if attr_name in self.__assignment_hard_locked_attribs:
            raise GeneralError(__err_msg_attr_name_other_lock, f'\nAttr: {repr(attr_name)}')

        self.__assignment_locked_attribs.add(attr_name)


    @_rename_exc_name_to_user_object_name
    def unlock_attr(self, attr_name: str) -> None:
        """
        Unlocks a attribute name from locked re-assignment
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_attr_name_exist = "Unlock attribute name does not exist"
        __err_msg_attr_name_exist_unlock = "Unlock attribute name does not exist in lock! Could not find name to unlock"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nAttr: {repr(attr_name)}')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nAttr: {repr(attr_name)}')

        # Remove Attr from Locked List
        try: self.__assignment_locked_attribs.remove(attr_name)
        except KeyError: raise GeneralError(__err_msg_attr_name_exist_unlock, f'\nAttr: {repr(attr_name)}')


    @_rename_exc_name_to_user_object_name
    def map_attr(self, child_attr: str, parent_attr: str) -> None:
        """
        Create a link of an attribute name to another attribute name

        This will auto assign/track the value of the parent attr to the child attr

        Useful to maintain references and follow values of other attributes. Similar
        to the concept of a pointer.
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for 'child_attr'"
        __err_msg_reference_name_str = "Only str is allowed for 'parent_attr'"
        __err_msg_attr_name_exist = f"Attribute name '{child_attr}' does not exist! Must be created first to assign to parent attribute"
        __err_msg_reference_name_exist = f"Attribute name '{parent_attr}' does not exist! Cannot assign value to child attribute"

        if not isinstance(child_attr, str): raise GeneralError(__err_msg_attr_name_str, f'\nAttr: {repr(child_attr)}')
        if not isinstance(parent_attr, str): raise GeneralError(__err_msg_reference_name_str, f'\nAttr: {repr(parent_attr)}')

        # Look up if Attr or Reference Name Exists
        if not child_attr in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nAttr: {repr(child_attr)}')
        if not parent_attr in self.__dict__: raise GeneralError(__err_msg_reference_name_exist, f'\nAttr: {repr(parent_attr)}')

        # Set Value to Reference Value
        setattr(self, child_attr, getattr(self, parent_attr))
    
        # Assign Attr Name to Reference Name in Reference Maps
        self.__assigned_src_reference_attr_map[child_attr] = parent_attr
        self.__assigned_dst_reference_attr_map.setdefault(parent_attr, {}).setdefault(child_attr, parent_attr)


    @_rename_exc_name_to_user_object_name
    def unmap_attr(self, attr_name: str) -> None:
        """
        Unlink an attribute name from another attribute name

        This will detach the link between the child attr and parent attr

        If it is a parent attr, all child links will be detached from that parent
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for 'attr_name'"
        __err_msg_attr_name_exist = f"Attribute name does not exist! Must be created first and linked to an attribute to unlink"
        __err_msg_reference_name_exist = f"Attribute name is not mapped to anything! Cannot unmap attribute"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nGot: {repr(attr_name)}')

        # Look up if Attr or Reference Name Exists at all or in Reference Maps
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nGot: {repr(attr_name)}')

        if (attr_name not in self.__assigned_src_reference_attr_map) \
        and (attr_name not in self.__assigned_dst_reference_attr_map):
            raise GeneralError(__err_msg_reference_name_exist, f'\nAttr: {attr_name}')
        
        self.__reference_deletion_check(attr_name, _src_ref_list=True, _dst_ref_list=True, _ref_removal_request=True)


    @_rename_exc_name_to_user_object_name
    def is_parent_map(self, attr_name: str) -> bool:
        """
        Check if attr is a parent link

        Returns: True if Parent, and False if not
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for 'attr_name'"
        __err_msg_attr_name_exist = f"Attribute name does not exist! Must be created first to check link type"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nGot: {repr(attr_name)}')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nGot: {repr(attr_name)}')

        # Check Link Type
        return (attr_name in self.__assigned_dst_reference_attr_map)
    

    @_rename_exc_name_to_user_object_name
    def is_child_map(self, attr_name: str) -> bool:
        """
        Check if attr is a child link

        Returns: True if Child, and False if not
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for 'attr_name'"
        __err_msg_attr_name_exist = f"Attribute name does not exist! Must be created first to check link type"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nGot: {repr(attr_name)}')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nGot: {repr(attr_name)}')

        # Check Link Type
        return (attr_name in self.__assigned_src_reference_attr_map)


    def __reference_deletion_check(
        self,
        _name: str,
        *,
        _src_ref_list: bool=False,
        _dst_ref_list: bool=False,
        _lock_list: bool=False,
        _ref_removal_request: bool=False,
    ) -> None:
        """
        Internal method: check if reference requires deletion from reference list
        if attribute is attempted to be re-assigned or deleted
        """
        # General Lock Attrs
        if _lock_list:
            if _name in self.__assignment_locked_attribs:
                self.__assignment_locked_attribs.remove(_name)

        # Reference Attrs - Must maintain reference map if attr in any locks
        
        # Source Reference List
        if _src_ref_list: # pragma: no branch
            if _name in self.__assigned_src_reference_attr_map:
                _is_locked = _name in self.__assignment_locked_attribs
                _is_hard_locked = _name in self.__assignment_hard_locked_attribs
                
                if (not (_is_locked or _is_hard_locked)) or (_ref_removal_request):
                    # Release Source & Destination Reference
                    _dst_ref_name: str = self.__assigned_src_reference_attr_map.pop(_name)
                    self.__assigned_dst_reference_attr_map[_dst_ref_name].pop(_name)
                    _verify_mapping_empty = self.__assigned_dst_reference_attr_map[_dst_ref_name]
                    # Release Destination Reference if Empty
                    if bool(_verify_mapping_empty) == False:
                        self.__assigned_dst_reference_attr_map.pop(_dst_ref_name)

        # Destination Reference List
        if _dst_ref_list:
            if _name in self.__assigned_dst_reference_attr_map:
                _is_locked = _name in self.__assignment_locked_attribs
                _is_hard_locked = _name in self.__assignment_hard_locked_attribs
                
                if (not (_is_locked or _is_hard_locked)) or (_ref_removal_request): # pragma: no branch
                    # Release Source References
                    for key in self.__assigned_dst_reference_attr_map[_name]:
                        self.__assigned_src_reference_attr_map.pop(key)
                    # Release Destination Reference
                    self.__assigned_dst_reference_attr_map.pop(_name)


    @_rename_exc_name_to_user_object_name
    def get_locked_list(self) -> _List[str]:
        """
        General locked list

        Returns a copy of the current list of locked attributes
        """
        return list(self.__assignment_locked_attribs)


    @_rename_exc_name_to_user_object_name
    def get_hard_locked_list(self) -> _List[str]:
        """
        Hard locked list

        Returns a new list of the current hard locked attributes
        """
        return list(self.__assignment_hard_locked_attribs)


    @_rename_exc_name_to_user_object_name
    def get_all_maps(self) -> _Dict[str, _Dict[str, _Any]]:
        """
        Get all Parent and Child Links

        Returns a new dict of the current parent and child link reference maps

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Parent map will be -> 'parent_map': {'attr_parent': {'attr_child': 'attr_parent'}}

        Child map will be -> 'child_map': {'attr_child': 'attr_parent'}
        """
        return {'parent_maps': _deepcopy(self.__assigned_dst_reference_attr_map), 'child_maps': _deepcopy(self.__assigned_src_reference_attr_map)}


    @_rename_exc_name_to_user_object_name
    def get_parent_maps(self) -> _Dict[str, _Dict[str, str]]:
        """
        Get all Parent Links

        Returns a new dict of the current parent link reference map

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Parent map will be -> {'attr_parent': {'attr_child': 'attr_parent'}}
        """
        return _deepcopy(self.__assigned_dst_reference_attr_map)


    @_rename_exc_name_to_user_object_name
    def get_parent_map_chains(self, parent_attr: _Optional[str]=None, *, dup_link_check: bool=True) -> _Union[_Dict[str, _List[str]], _List[str]]:
        """
        Get Parent Map Chains

        Builds and returns a new dict or list of attr name chains that are currently linked together by interconnected children with
        the very top chain link being their parent

        Chains are represented as a list with the parent being first and the children to follow
        
        Represented chains are built from scratch each time this method is called

        [Options]

        parent_attr: Optional - if specified, gets the chain of the parent name that currently has a chain. returns a list

        dup_link_check: Default=True - Protects against duplicate links to the parent. If disabled and a duplicate is found, it 
        will still return chain(s), but will cut the chain's previous links to the parent and only continue the chain from the
        last reference to the parent and retain any chain links following the last reference (see note below to clear any concerns).
        
        Note: It is worth stating, this method does not break/affect the actual behavior of the attributes being linked together, as this method only fresh builds a representation
        of the attributes linked together in the form of a chain for your reference to help understand what attribute names are connected to each other.
        The true linking is controlled by other mechs, and any real duplicate links are not affected as that is acceptable behavior.

        [Example Chain Structure]

        attr_parent = 'some value'

        attr_child1 == attr_parent

        attr_child2 == attr_child1

        Parent chain will be -> {'attr_parent': ['attr_parent', 'attr_child1', 'attr_child2']}
        """
        # Error Checks
        err_msg_parent_name_type = "Only str|None is allowed for 'parent_attr'"
        err_msg_dup_link_chk_type = "Only bool is allowed for 'dup_link_check'"
        err_msg_chain_conflict = f"Cannot build chain due to duplicate child name(s) already linked to parent! Disable this check with 'dup_link_check'"
        err_msg_parent_not_found = f"Name '{parent_attr}' does not have a chain that exists!"

        if not isinstance(parent_attr, (str, type(None))): raise GeneralError(err_msg_parent_name_type, f'\nGot: {parent_attr}')
        if not isinstance(dup_link_check, bool): raise GeneralError(err_msg_dup_link_chk_type, f'\nGot: {dup_link_check}')

        # Always use new objects
        all_parent_chains = {}
        chain_link_tracker = []

        # Seek and Build the chains that exist
        for child in self.__assigned_src_reference_attr_map:

            # If not parent assume it is a child link
            if child not in self.__assigned_dst_reference_attr_map:
                # Start new chain link build and add first child
                chain_link_build = []
                chain_link_build.append(child)
                parent_check = ''
                child_check = child

                # Walk up the chain to discover other links to reach parent
                while True:
                    parent_check = self.__assigned_src_reference_attr_map[child_check]

                    # Parent NOT Specified: If enabled, verify no other child link is also linked to the same parent
                    if ((parent_check in chain_link_tracker) and (dup_link_check)) \
                    and (parent_attr is None):
                        found_offenders = list(filter(lambda attr:not (attr == child_check), self.__assigned_dst_reference_attr_map[parent_check]))
                        raise GeneralError(
                            err_msg_chain_conflict,
                            f"\nPARENT: {parent_check} \nLINK_ATTEMPTED: {child_check} \nALREADY_LINKED_TO_PARENT: {found_offenders}"
                        )
                    
                    # Parent IS Specified: If enabled, verify no other child link is also linked to the same parent
                    if ((parent_check in chain_link_tracker) and (dup_link_check)) \
                    and ((parent_attr is not None) and (parent_attr == parent_check)):
                        found_offenders = list(filter(lambda attr:not (attr == child_check), self.__assigned_dst_reference_attr_map[parent_check]))
                        raise GeneralError(
                            err_msg_chain_conflict,
                            f"\nPARENT: {parent_check} \nLINK_ATTEMPTED: {child_check} \nALREADY_LINKED_TO_PARENT: {found_offenders}"
                        )
                    
                    # Check if the parent is also a child
                    if parent_check in self.__assigned_src_reference_attr_map:
                        chain_link_build.append(parent_check)
                        child_check = parent_check
                    
                    # Add parent to chain and invert order for top->down order. update tracker
                    else:
                        chain_link_build.append(parent_check)
                        chain_link_tracker.extend(chain_link_build)
                        chain_link_build.reverse()
                        all_parent_chains[parent_check] = chain_link_build
                        break

        # Check if parent_name was specified but not found
        if (parent_attr is not None) and (parent_attr not in all_parent_chains):
            raise GeneralError(
                err_msg_parent_not_found,
                f"\nGot: {parent_attr}"
            )

        # Return single parent chain if specified, otherwise continue build
        if parent_attr in all_parent_chains:
            return all_parent_chains[parent_attr]

        # Return all chains if no parent specified
        return all_parent_chains


    @_rename_exc_name_to_user_object_name
    def get_child_maps(self) -> _Dict[str, str]:
        """
        Get all Child Links

        Returns a new dict of the current child link reference map

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Child map will be -> {'attr_child': 'attr_parent'}
        """
        return _deepcopy(self.__assigned_src_reference_attr_map)
    

    @_rename_exc_name_to_user_object_name
    def get_attrs(self) -> _Dict[str, _Any]:
        """
        Returns a dict copy of the MaciDataObj's current attribute names and values
        """
        skip_name_keys = ('_MaciDataObjConstructor', '__maci_obj_format_id')
        return {name:value for name,value in self.__dict__.items() if not name.startswith(skip_name_keys)}
    

    @_rename_exc_name_to_user_object_name
    def load_attrs(self, data: _Dict[str, _Any]) -> None:
        """
        Loads data from a dict into the MaciDataObj in-place
        
        Creates new attribute names with their values retained based on the top level key names of the dict

        Note: If the key name is not a valid pythonic name convention, it will be skipped
        """
        err_msg_type_data = "Only dict is allowed for 'data'"
        if not isinstance(data, dict): raise GeneralError(err_msg_type_data, f'\nGot: {repr(data)}')

        for attr,value in data.items():
            # Validate is String and Identifier for valid Attr Names, otherwise skip
            if not isinstance(attr, str): continue
            if not attr.isidentifier(): continue            
            setattr(self, attr, value)


#########################################################################################################
# Main MaciDataObj Reference

# Meta for structure references
class __MaciDataObj(type):
    def __repr__(self: type) -> str:
        return f"<class '{self.__module__}.{self.__name__}'>"

# Main Object Usage
class MaciDataObj(_MaciDataObjConstructor, metaclass=__MaciDataObj):
    def __init__(
        self,
        filename: str,
        *,
        attr_name_dedup: bool,
        encoding: _Union[str, None],
        _py_syntax_err_msg: str='',
        _name_preexists_err_msg: str='',
        _name_reference_does_not_exist_msg: str='',
        _assignment_locked_atrribs_err_msg: str='',
        _assignment_hard_locked_atrribs_err_msg: str='',
        _is_str_parse_request: bool=False,
        _str_data: str='',
        _is_load_request: bool=False,
        _is_build_request: bool=False,
        _ignore_internal_maci_attr_check: bool=False,
    )-> None:
        __constructor_locked = True
        __constructor_locked = False if (_is_load_request
                                        or _is_build_request
                                    ) else True

        # Error Messages
        _init_request_err_msg = "Unusable 'MaciDataObj' object. Only meant for hinting and not to be instantiated"
        _init_request_err_msg_obj = "For object: Use 'maci.build()' to create empty 'MaciDataObj' to build out"
        _init_request_err_msg_hinting = "For hinting: Use 'maci.hint.MaciDataObj' to hint type correctly"
        _init_request_err_msg_help = f"{_init_request_err_msg_obj}\n{_init_request_err_msg_hinting}"

        # Hint Error Report
        if __constructor_locked:
            raise Hint(_init_request_err_msg, f'\n{_init_request_err_msg_help}')

        # NORMAL REQUEST
        if not __constructor_locked: # pragma: no branch
            super().__init__(
                filename,
                attr_name_dedup=attr_name_dedup,
                encoding=encoding,
                _py_syntax_err_msg=_py_syntax_err_msg,
                _name_preexists_err_msg=_name_preexists_err_msg,
                _name_reference_does_not_exist_msg=_name_reference_does_not_exist_msg,
                _assignment_locked_atrribs_err_msg=_assignment_locked_atrribs_err_msg,
                _assignment_hard_locked_atrribs_err_msg=_assignment_hard_locked_atrribs_err_msg,
                _is_str_parse_request=_is_str_parse_request,
                _str_data=_str_data,
                _is_build_request=_is_build_request,
                _ignore_internal_maci_attr_check=_ignore_internal_maci_attr_check,
            )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, MaciDataObj):
            return NotImplemented
        else:
            # Compare str repr of maci objects, which contain actual attrs & values in strings
            return str(self) == str(other)

    def __bool__(self) -> bool:
        skip_name_keys = ('_MaciDataObjConstructor', '__maci_obj_format_id')
        if [attr for attr in self.__dict__ if not attr.startswith(skip_name_keys)]:
            return True
        return False

    def __repr__(self) -> str:
        skip_name_keys = ('_MaciDataObjConstructor', '__maci_obj_format_id')
        build_repr = ', '.join(f"{name}={value!r}" for name,value in self.__dict__.items() if not name.startswith(skip_name_keys))
        return f"{type(self).__name__}({build_repr})"
    
    def __dir__(self) -> _List[str]:
        skip_name_keys = ('_MaciDataObjConstructor', '__maci_obj_format_id')
        default_attrs = list(name for name in dir(MaciDataObj) if not name.startswith(skip_name_keys))
        user_attrs = list(name for name in self.__dict__ if not name.startswith(skip_name_keys))
        return default_attrs + user_attrs


#########################################################################################################
# Main Dump Function

# Hinting reference name for "ClassObject" to denote a ClassObject can be used to dump data
ClassObject = _TypeVar('ClassObject')

def __dump_data(
    *,
    _is_string_request: bool=False,
    filename: str,
    data: _Any, # objects allowed: MaciDataObj, dict, ClassObject - ignoring type checker
    append: bool=False,
    indent_level: int=1,
    indentation_on: bool=True,
    multi_line_str: bool=False,
    encoding: _Union[str, None]=None,
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
    __err_msg_no_attrs_found: str=''
) -> _Optional[str]:
    """
    Main dump function for file/string dump
    """
    # DUMP STR REQUEST: If this is a str dump request,
    # then set values accordingly
    
    # Error Checks & Collect Error Messages
    __err_msg_general_error = "Error has occurred and cannot proceed"
    __err_msg_invalid_maciobj = "Invalid maci object passed in. Please use a valid 'MaciDataObj'"
    __err_msg_no_attrs_found = __err_msg_no_attrs_found

    if _is_string_request:
        # Set Error Type
        DumpStrError = DumpStr
        # Set Values
        filename = ''
        __err_msg_invalid_maciobj_item = f'\nGot: {repr(data)}'
    else:
        DumpError = Dump
        __err_msg_invalid_maciobj_item = f'\nFile: {repr(filename)} \nGot: {repr(data)}'

    if isinstance(data, type(MaciDataObj)):
        if _is_string_request: raise DumpStrError(__err_msg_invalid_maciobj, __err_msg_invalid_maciobj_item)
        raise DumpError(__err_msg_invalid_maciobj, __err_msg_invalid_maciobj_item)


    # Setup
    __build_data_output: _Any = _StringIO()
    __assignment_glyphs = _Glyphs()
    __skip_object_key = ('_MaciDataObjConstructor', '__maci_obj_format_id')
    __locked_attr_list_key =  '_MaciDataObjConstructor__assignment_locked_attribs'
    __hard_locked_attr_list_key =  '_MaciDataObjConstructor__assignment_hard_locked_attribs'
    __reference_attr_list_key =  '_MaciDataObjConstructor__assigned_src_reference_attr_map'
    __maci_obj_format_id_match = "48448910-fa49-45ca-bd3e-38d7af136af5-7bcece52-e5ee-4272-989d-103f07aa6c0f"

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    # Set Glyph Style to Symbols if Requested - Creates New Object with Same Names
    if use_symbol_glyphs:
        __assignment_glyphs = _Glyphs(
            m=__assignment_glyphs.ref,
            h=__assignment_glyphs.hard_lock,
            l=__assignment_glyphs.lock,
            mh=__assignment_glyphs.ref_hard_lock,
            ml=__assignment_glyphs.ref_lock,
        )

    
    ### MACI Got: Check if MaciDataObj ###

    # Build Out Data
    if (isinstance(data, MaciDataObj)) and (data.__maci_obj_format_id__ == __maci_obj_format_id_match):
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
                    else: continue  # pragma: no cover  # code does work, but py10+ is only passing cov oddly
                if (key.startswith('_')) and not (_is_dunder_attr):
                    if not (private_attrs or private_under_attrs):
                        continue
                _is_dunder_attr = False # reset dunder check for single under's

                # Reference Name and Locked
                if (key in data.__dict__[__reference_attr_list_key]) and (key in data.__dict__[__locked_attr_list_key]):
                    __build_data_output.write(f'{key} {__assignment_glyphs.ml} {data.__dict__[__reference_attr_list_key][key]}\n')
                    continue
                # Reference Name and Hard Locked
                if (key in data.__dict__[__reference_attr_list_key]) and (key in data.__dict__[__hard_locked_attr_list_key]):
                    __build_data_output.write(f'{key} {__assignment_glyphs.mh} {data.__dict__[__reference_attr_list_key][key]}\n')
                    continue
                # Reference Name Only
                if key in data.__dict__[__reference_attr_list_key]:
                    __build_data_output.write(f'{key} {__assignment_glyphs.m} {data.__dict__[__reference_attr_list_key][key]}\n')
                    continue

                # REPR SIGNAL: If certain object type matches, disable repr use
                repr_signal = __repr_signal(value)

                # Locked Only
                if key in data.__dict__[__locked_attr_list_key]:
                    if __multiline_check(value) and indentation_on:
                        value = _cleanformat(value, indent_level)
                        __build_data_output.write(f'{key} {__assignment_glyphs.l} {value}\n')
                    elif (multi_line_str) and (isinstance(value, str)) and ('\n' in value):
                        __build_data_output.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.l, value=value))
                    else:
                        if not repr_signal:
                            __build_data_output.write(f'{key} {__assignment_glyphs.l} {value}\n')
                            continue
                        __build_data_output.write(f'{key} {__assignment_glyphs.l} {repr(value)}\n')
                    continue
                # Hard Locked Only
                if key in data.__dict__[__hard_locked_attr_list_key]:
                    if __multiline_check(value) and indentation_on:
                        value = _cleanformat(value, indent_level)
                        __build_data_output.write(f'{key} {__assignment_glyphs.h} {value}\n')
                    elif (multi_line_str) and (isinstance(value, str)) and ('\n' in value):
                        __build_data_output.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.h, value=value))
                    else:
                        if not repr_signal:
                            __build_data_output.write(f'{key} {__assignment_glyphs.h} {value}\n')
                            continue
                        __build_data_output.write(f'{key} {__assignment_glyphs.h} {repr(value)}\n')
                    continue
                # Normal Assignment
                if __multiline_check(value) and indentation_on:
                    value = _cleanformat(value, indent_level)
                    __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                elif (multi_line_str) and (isinstance(value, str)) and ('\n' in value):
                    __build_data_output.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.norm, value=value))
                else:
                    if not repr_signal:
                        __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                        continue
                    __build_data_output.write(f'{key} {__assignment_glyphs.norm} {repr(value)}\n')

        # Get Final Build Value
        __build_data_output = __build_data_output.getvalue()

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()


        # Check if DUMP STR REQUEST: Return built string
        if _is_string_request:
            return __build_data_output

        # Write File Data and Return None
        __write_file_data(filename, __build_data_output, write_mode, encoding=encoding)
        return None


    ### DICT: Check if dict ###
    if isinstance(data, dict):
        # Build Data
        for key,value in data.items():
            # Multline Assignment from Indentation
            if indentation_on:
                if __multiline_check(value):
                    value = _cleanformat(value, indent_level)
                    __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                    continue
            if (multi_line_str) and (isinstance(value, str)) and ('\n' in value):                
                __build_data_output.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.norm, value=value))
                continue

            # REPR SIGNAL: If certain object type matches, disable repr use
            repr_signal = __repr_signal(value)

            # Single Line Assignment
            if not repr_signal:
                __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                continue
            __build_data_output.write(f'{key} {__assignment_glyphs.norm} {repr(value)}\n')

        # Get Final Build Value
        __build_data_output = __build_data_output.getvalue()

        # Strip Last \n Char
        __build_data_output = __build_data_output.rstrip()

        
        # Check if DUMP STR REQUEST: Return built string
        if _is_string_request:
            return __build_data_output

        # Write File Data and Return None
        __write_file_data(filename, __build_data_output, write_mode, encoding=encoding)
        return None


    ### CUSTOM CLASS: Check if any Class Object with Attributes
    _filter_objects = (str, int, float, bool, list, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)
    if not isinstance(data, _filter_objects): # pragma: no branch
        # Setup
        _init_attr_header = '# attrs: init'
        __build_data_output_init = _StringIO()
        _class_attr_header = '# attrs: class'
        __build_data_output_class = _StringIO()
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
                        key = key[len(f'_{type(data).__name__}'):]
                        _is_dunder_attr = True
                    else: continue  # pragma: no cover  # code does work, but py10+ is only passing cov oddly
                if (key.startswith('_')) and not (_is_dunder_attr):
                    if not (private_attrs or private_under_attrs or private_class_attrs or private_class_under_attrs):
                        continue
                _is_dunder_attr = False # reset dunder check for single under's

                # REPR SIGNAL: If certain object type matches, disable repr use
                repr_signal = __repr_signal(value)

                # Build Data
                if __multiline_check(value) and indentation_on:
                    value = _cleanformat(value, indent_level)
                    __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                elif (multi_line_str) and (isinstance(value, str)) and ('\n' in value):                
                    __build_data_output.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.norm, value=value))
                else:
                    if not repr_signal:
                        __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                        continue
                    __build_data_output.write(f'{key} {__assignment_glyphs.norm} {repr(value)}\n')

        # Case 2 - Class Attrs Only. Not Instantiated
        elif '__mro__' in vars(type(data)) and class_attrs:
            _is_case2_build = True

            for key,value in vars(data).items():
                # Strip Unneeded Attrs/Methods, and Preserve Dunders if Required
                if callable(value): continue
                if (key.startswith('__') and key.endswith('__')): continue
                if key.startswith(f'_{data.__name__}'): # dunder detection (name mangle)
                    if (private_attrs) or (private_dunder_attrs) or (private_class_attrs) or (private_class_dunder_attrs):
                        key = key[len(f'_{data.__name__}'):]
                        _is_dunder_attr = True
                    else: continue  # pragma: no cover  # code does work, but py10+ is only passing cov oddly
                if (key.startswith('_')) and not (_is_dunder_attr):
                    if not (private_attrs or private_under_attrs or private_class_attrs or private_class_under_attrs):
                        continue
                _is_dunder_attr = False # reset dunder check for single under's

                # REPR SIGNAL: If certain object type matches, disable repr use
                repr_signal = __repr_signal(value)

                # Build Data
                if __multiline_check(value) and indentation_on:
                    value = _cleanformat(value, indent_level)
                    __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                elif (multi_line_str) and (isinstance(value, str)) and ('\n' in value):                
                    __build_data_output.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.norm, value=value))
                else:
                    if not repr_signal:
                        __build_data_output.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                        continue
                    __build_data_output.write(f'{key} {__assignment_glyphs.norm} {repr(value)}\n')
        
        # Default Case 3 - Init Attrs or Class Attrs, or both
        else:
            _is_case3_build = True

            # First: Init Attrs
            if '__init__' not in vars(data): # pragma: no branch
                for key,value in vars(data).items():
                    # Strip Unneeded Attrs/Methods, and Preserve Dunders if Required
                    if callable(value): continue
                    if key.startswith(f'_{type(data).__name__}'): # dunder detection (name mangle)
                        if (private_attrs) or (private_dunder_attrs) or (private_init_attrs) or (private_init_dunder_attrs):
                            key = key[len(f'_{type(data).__name__}'):]
                            _is_dunder_attr = True
                        else: continue  # pragma: no cover  # code does work, but py10+ is only passing cov oddly
                    if (key.startswith('_')) and not (_is_dunder_attr):
                        if not (private_attrs or private_under_attrs or private_init_attrs or private_init_under_attrs):
                            continue
                    _is_dunder_attr = False # reset dunder check for single under's

                    # REPR SIGNAL: If certain object type matches, disable repr use
                    repr_signal = __repr_signal(value)
                
                    # Build Data - Init Attrs
                    if __multiline_check(value) and indentation_on:
                        value = _cleanformat(value, indent_level)
                        __build_data_output_init.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                    elif (multi_line_str) and (isinstance(value, str)) and ('\n' in value):                
                        __build_data_output_init.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.norm, value=value))
                    else:
                        if not repr_signal:
                            __build_data_output_init.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                            continue
                        __build_data_output_init.write(f'{key} {__assignment_glyphs.norm} {repr(value)}\n')
                
            # Last: Class Attrs
            if class_attrs:
                for key,value in vars(type(data)).items():
                    # Strip Unneeded Attrs/Methods, and Preserve Dunders if Required
                    if callable(value): continue
                    if (key.startswith('__') and key.endswith('__')): continue
                    if key.startswith(f'_{type(data).__name__}'): # dunder detection (name mangle)
                        if (private_attrs) or (private_dunder_attrs) or (private_class_attrs) or (private_class_dunder_attrs): 
                            key = key[len(f'_{type(data).__name__}'):]
                            _is_dunder_attr = True
                        else: continue  # pragma: no cover  # code does work, but py10+ is only passing cov oddly
                    if (key.startswith('_')) and not (_is_dunder_attr):
                        if not (private_attrs or private_under_attrs or private_class_attrs or private_class_under_attrs):
                            continue
                    _is_dunder_attr = False # reset dunder check for single under's

                    # REPR SIGNAL: If certain object type matches, disable repr use
                    repr_signal = __repr_signal(value)
                    
                    # Build Data - Class Attrs
                    if __multiline_check(value) and indentation_on:
                        value = _cleanformat(value, indent_level)
                        __build_data_output_class.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                    elif (multi_line_str) and (isinstance(value, str)) and ('\n' in value):                
                        __build_data_output_class.write(__setup_multi_string(key=key, assignment_glyph=__assignment_glyphs.norm, value=value))
                    else:
                        if not repr_signal:
                            __build_data_output_class.write(f'{key} {__assignment_glyphs.norm} {value}\n')
                            continue
                        __build_data_output_class.write(f'{key} {__assignment_glyphs.norm} {repr(value)}\n')

        # Get Final Build Values
        __build_data_output = __build_data_output.getvalue()
        __build_data_output_class = __build_data_output_class.getvalue()
        __build_data_output_init = __build_data_output_init.getvalue()

        # Structure Build
        if _is_case1_build: pass
        elif _is_case2_build: pass
        elif _is_case3_build: # pragma: no branch
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


        # Check if DUMP STR REQUEST: Return built string
        if _is_string_request:
            return __build_data_output

        # Write File Data and Return None
        __write_file_data(filename, __build_data_output, write_mode, encoding=encoding)
        return None
    
    
    # Return None for type checker
    return None  # pragma: no cover  # ignore. only for type checker


#########################################################################################################
# Dump: Functions

# Multiline Check
def __multiline_check(data: _Union[list, dict, tuple, set]) -> bool:
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
def __write_file_data(filename: str, data: _Any, write_mode: str, *, encoding: _Union[str, None]) -> None:
    """
    Write New or Append Data to File
    """
    __err_msg_write_mode = 'Bad write mode'
    __write_mode_allowed_list = ['w', 'a']
    try:
        # Write New File Mode
        if write_mode == 'w':
            _dumpraw(filename, data, encoding=encoding)
        # Append Append File Mode
        if write_mode == 'a':
            _dumpraw(filename, data, append=True, encoding=encoding)
        # Raise Exception if No Match - Dev Check
        if not write_mode in __write_mode_allowed_list: # pragma: no cover
            raise Dump(__err_msg_write_mode, f'\nGot: {repr(write_mode)}')
    except DumpRaw as __err_msg: raise Dump(__err_msg, '')


# Setup Multi-String
def __setup_multi_string(key: str, assignment_glyph: str, value: str,) -> str:
    is_set_start_new_line = '' if value.startswith('\n') else '\n'
    is_set_end_new_line = '' if value.endswith('\n') else '\n'
    surrounding_quote_type = "'''" if '"""' in value else '"""'
    return f'{key} {assignment_glyph} {surrounding_quote_type}{is_set_start_new_line}{value}{is_set_end_new_line}{surrounding_quote_type}\n'


# Set DateTime Object to String
def __repr_signal(value: _Any) -> bool:
    """
    Returns a bool to signal whether to use repr for certain object types
    """
    types_to_signal_disable_repr = (_datetime, _datetime_date, _datetime_time)
    if isinstance(value, types_to_signal_disable_repr):
        return False
    return True
