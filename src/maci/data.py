# data
#########################################################################################################
# Imports
from ast import literal_eval as __literal_eval__
from copy import deepcopy
from typing import Any as _Any
from typing import NoReturn as _NoReturn
from typing import Dict as _Dict
from typing import List as _List
from typing import Union as _Union
from typing import Optional as _Optional
from .error import Load, GeneralError, Hint

#########################################################################################################
# MaciDataObj Constructor
class _MaciDataObjConstructor:
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
        _is_hint_request: bool=False,
    ) -> None:
        # Setup: Reference lists and maps should be first assignment
        self.__assignment_locked_attribs = []
        self.__assignment_hard_locked_attribs = ()
        self.__assigned_src_reference_attr_map = {}
        self.__assigned_dst_reference_attr_map: _Dict[str, _Dict[str, str]] = {}
        self.__attrib_name_dedup = attr_name_dedup

        # One Time Generated using UUID4 mode from UUID Library.
        # This helps authenticity of MaciDataObj Object for Development aid
        self.__maci_file_format_id__ = "48448910-fa49-45ca-bd3e-38d7af136af5-7bcece52-e5ee-4272-989d-103f07aa6c0f"

        # Syntax/Usage Error Messages
        py_syntax_err_msg = _py_syntax_err_msg
        name_preexists_err_msg = _name_preexists_err_msg
        name_reference_does_not_exist = _name_reference_does_not_exist_msg
        self.__assignment_locked_atrribs_err_msg = _assignment_locked_atrribs_err_msg
        self.__assignment_hard_locked_atrribs_err_msg = _assignment_hard_locked_atrribs_err_msg

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
            with open(filename, 'r', encoding=encoding) as file_data:
                file_data = file_data.read().splitlines()

        # Data Build Setup and Switches        
        __is_building_data_sw = False
        __body_build_data_sw = False
        __end_data_build_sw = False
        __build_data = ''

        # Markers
        __start_markers = ('[', '{', '(', "'''", '"""')
        __end_markers = (']', '}', ')', "'''", '"""')
        __skip_markers = ('',' ','#','\n')
        __assignment_glyphs = ('=', '$=', '==', '$==', '$$=', '$$==')
        __eof_marker = file_data[-1]

        # Main File/Str Loop
        # To display correct line number, ensure to add +1 when ready to raise. Keeping
        # constant +1 track will add latency to loop, so only provide as needed
        for line_num,__file_data_line in enumerate(file_data):

            # Set Skip Marker
            try: __skip_marker = __file_data_line[0]
            except IndexError: __skip_marker = ''

            # Skip Any Comments, Blanks, and New Lines. Do not skip during a muli-line build
            if (__is_building_data_sw == False) and (__skip_marker in __skip_markers): continue

            # Set Assignment Glyph
            try: 
                __assignment_glyph = __file_data_line.split()[1]
            except IndexError: __assignment_glyph = ''

            # Basic Syntax Check, or if in a Multiline Build
            if (__assignment_glyph in __assignment_glyphs) or (__is_building_data_sw):

                if not __is_building_data_sw:

                    # Check if Value Empty
                    if __file_data_line.partition(__assignment_glyph)[2].strip() == '':
                        raise Load(
                            py_syntax_err_msg,
                            f'\nFILE: "{filename}" \nLINE: {line_num+1} \nATTR_NAME: {__file_data_line.partition(__assignment_glyph)[0].strip()} \nGOT: {__file_data_line}'
                        )
                    
                    __current_assignment_glyph = __assignment_glyph
                    __var_token = __file_data_line.partition(__assignment_glyph)[0].strip()
                    __value_token = __file_data_line.partition(__assignment_glyph)[2].strip()
                    __value_token_multi = __file_data_line.partition(__assignment_glyph)[2].split()[0].strip()
                    __last_token = __file_data_line.partition(__assignment_glyph)[2].strip()
                    try: __start_skip_token = __file_data_line.split(__assignment_glyph)[1].split()[1][0].strip()
                    except IndexError: __start_skip_token = ''
                    
                if __is_building_data_sw:
                    try: __end_token = __file_data_line[0]
                    except IndexError: __end_token = ''
                
                # Verify Assignment Glyph is Not Attr Reference for Multiline Build Check
                is_attr_reference_glyph = False
                if (__current_assignment_glyph == __assignment_glyphs[2]) \
                or (__current_assignment_glyph == __assignment_glyphs[3]) \
                or (__current_assignment_glyph == __assignment_glyphs[5]):
                    is_attr_reference_glyph = True
                
                # START BUILD: Check if value in file line is only Start Marker. Check if Multiline or Single Line
                if (__value_token_multi in __start_markers) \
                and ((__last_token in __start_markers) or (__start_skip_token[0] in __skip_markers)) \
                and (__is_building_data_sw == False) \
                and not (is_attr_reference_glyph):
                    
                    # Check if var_token is a Pythonic valid name
                    if not __var_token.isidentifier():
                        raise Load(
                            'Must use valid Python name syntax to load attr name',
                            f'\nFILE: "{filename}" \nLINE: {line_num+1} \nATTR_NAME: {__file_data_line.partition(__assignment_glyph)[0].strip()} \nGOT: {__file_data_line}'
                        )
                    
                    if (self.__attrib_name_dedup) and (hasattr(self, __var_token)):
                            raise Load(name_preexists_err_msg, f'\nFILE: "{filename}" \nATTR_NAME: {__var_token}')

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
                        if __current_assignment_glyph == __assignment_glyphs[1]:
                            self.__assignment_locked_attribs.append(__var_token)

                        # Check if Attr is Hard Locked from Re-Assignment
                        if __current_assignment_glyph == __assignment_glyphs[4]:
                            self.__dict__['_MaciDataObjConstructor__assignment_hard_locked_attribs'] = (*self.__assignment_hard_locked_attribs, __var_token)

                    except SyntaxError: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}" \nATTR_NAME: {__var_token}')

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
                        # Check if var_token is a Pythonic valid name
                        if not __var_token.isidentifier():
                            raise Load(
                                'Must use valid Python name syntax to load attr name',
                                f'\nFILE: "{filename}" \nLINE: {line_num+1} \nATTR_NAME: {__file_data_line.partition(__assignment_glyph)[0].strip()} \nGOT: {__file_data_line}'
                            )
                        # Check if Attr Dedup
                        if (self.__attrib_name_dedup) and (hasattr(self, __var_token)):
                            raise Load(name_preexists_err_msg, f'\nFILE: "{filename}" \nATTR_NAME: {__var_token}')
                        
                        # Check if Attr is a Reference to Another Attr's Value for Assignment. Ignore Comments
                        if __current_assignment_glyph == __assignment_glyphs[2]:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assigned_src_reference_attr_map[__var_token] = __value_token
                            self.__assigned_dst_reference_attr_map.setdefault(__value_token, {}).setdefault(__var_token, __value_token)
                            continue
                        
                        # Check if Attr is a Reference to Another Attr's Value for Assignment and Locked from Re-Assignment. Ignore Comments
                        if __current_assignment_glyph == __assignment_glyphs[3]:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assigned_src_reference_attr_map[__var_token] = __value_token
                            self.__assigned_dst_reference_attr_map.setdefault(__value_token, {}).setdefault(__var_token, __value_token)
                            self.__assignment_locked_attribs.append(__var_token)
                            continue
                        
                        # Check if Attr is a Reference to Another Attr's Value for Assignment and Hard Locked from Re-Assignment. Ignore Comments
                        if __current_assignment_glyph == __assignment_glyphs[5]:
                            __value_token = f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()
                            setattr(self, __var_token, getattr(self, __value_token))
                            self.__assigned_src_reference_attr_map[__var_token] = __value_token
                            self.__assigned_dst_reference_attr_map.setdefault(__value_token, {}).setdefault(__var_token, __value_token)
                            self.__dict__['_MaciDataObjConstructor__assignment_hard_locked_attribs'] = (*self.__assignment_hard_locked_attribs, __var_token)
                            continue

                        # Assign Attr
                        setattr(self, __var_token, __literal_eval__(__value_token))

                        # Check if Attr is Locked from Re-Assignment
                        if __current_assignment_glyph == __assignment_glyphs[1]:
                            self.__assignment_locked_attribs.append(__var_token)

                        # Check if Attr is Hard Locked from Re-Assignment
                        if __current_assignment_glyph == __assignment_glyphs[4]:
                            self.__dict__['_MaciDataObjConstructor__assignment_hard_locked_attribs'] = (*self.__assignment_hard_locked_attribs, __var_token)
                        
                    except ValueError: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}" \nATTR_NAME: {__var_token}')
                    except AttributeError:
                        # REF_NAME: Ignores Comments to Display Attr Reference Name
                        raise Load(
                            name_reference_does_not_exist,
                            f'\nFILE: "{filename}" \nATTR_NAME: {__var_token} \nREF_NAME: {f"{__value_token} "[:__value_token.find(__skip_markers[2])].rstrip()}'
                        )
                    except SyntaxError: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}" \nATTR_NAME: {__var_token}')

            else: raise Load(py_syntax_err_msg, f'\nFILE: "{filename}"')
    

    def __setattr__(self, _name: str, _new_value: _Any) -> None:
        # Check if Attr Already Exists, if so, Collect Original Value
        if hasattr(self, _name):
            _orig_value = self.__dict__.get(_name)
            
        # Release Attribute Reference if Name is Re-Assigned
        if hasattr(self, _name):
            self.__reference_deletion_check(_name, _src_ref_list=True)

        # Protect Internal List/Reference Attrs and Methods from Re-Assignment
        _internal_check_lists = (
            '_MaciDataObjConstructor__assignment_hard_locked_attribs',
            '_MaciDataObjConstructor__assignment_locked_attribs',
            '_MaciDataObjConstructor__assigned_src_reference_attr_map',
            '_MaciDataObjConstructor__assigned_dst_reference_attr_map',
            '_MaciDataObjConstructor__reference_deletion_check',
            'hard_lock_attr',
            'lock_attr',
            'unlock_attr',
            'reference_attr'
        )
        if hasattr(self, _name) and (_name in _internal_check_lists):
            raise GeneralError('Cannot re-assign internal MaciDataObj attribute or method name!', f'\nATTR_NAME: "{_name}"')


        # Always Assign Value 
        self.__dict__[_name] = _new_value


        # If attr was added to lock/hard_lock list after first assignment, assign orig value back, and raise exception
        # Exception can be caught/bypassed, setting original value is vital to protect value

        # General Lock Protection
        if hasattr(self, '_MaciDataObjConstructor__assignment_locked_attribs'):
            if _name in self.__assignment_locked_attribs:
                # PROTECT ORIGINAL VALUE
                self.__dict__[_name] = _orig_value
                # RAISE EXCEPTION
                raise GeneralError(self.__assignment_locked_atrribs_err_msg, f'\nATTR_NAME: "{_name}"')

        # Hard Lock Protection
        if hasattr(self, '_MaciDataObjConstructor__assignment_hard_locked_attribs'):
            if _name in self.__assignment_hard_locked_attribs:
                # PROTECT ORIGINAL VALUE
                self.__dict__[_name] = _orig_value
                # RAISE EXCEPTION
                raise GeneralError(self.__assignment_hard_locked_atrribs_err_msg, f'\nATTR_NAME: "{_name}"')
        
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
                        
                        if any(other_child_ref_name_track):
                            other_ref_name = other_child_ref_name_track.pop()
                        else: break

                    # Assign New Value to All Child or Chained References and Verify None are Locked
                    for ref_name in collected_references:
                        # If Source is Locked, Block Update
                        _is_locked = ref_name in self.__assignment_locked_attribs
                        _is_hard_locked = ref_name in self.__assignment_hard_locked_attribs
                        if _is_locked: raise GeneralError(self.__assignment_locked_atrribs_err_msg, f'\nATTR_NAME: "{ref_name}"')
                        if _is_hard_locked: raise GeneralError(self.__assignment_hard_locked_atrribs_err_msg, f'\nATTR_NAME: "{ref_name}"')

                        # Update Reference(s) to New Value
                        self.__dict__[ref_name] = _new_value
    
    
    def __delattr__(self, _name: str) -> None:
        # Protect Internal List/Reference Attrs from Deletion
        _internal_check_lists = (
            '_MaciDataObjConstructor__assignment_hard_locked_attribs',
            '_MaciDataObjConstructor__assignment_locked_attribs',
            '_MaciDataObjConstructor__assigned_src_reference_attr_map',
            '_MaciDataObjConstructor__assigned_dst_reference_attr_map'
        )
        if _name in _internal_check_lists:
            raise GeneralError('Cannot delete internal MaciDataObj attribute name!', f'\nATTR_NAME: "{_name}"')

        # Protect Hard Locked Attr from Deletion
        if _name in self.__assignment_hard_locked_attribs:
            # RAISE EXCEPTION
            raise GeneralError(self.__assignment_hard_locked_atrribs_err_msg, f'\nATTR_NAME: "{_name}"')

        # Release Attribute from Lock & Reference List if Name is Deleted
        if hasattr(self, _name):
            self.__reference_deletion_check(_name, _src_ref_list=True, _dst_ref_list=True, _lock_list=True)

        # Allow Normal Deletion
        super().__delattr__(_name)


    def hard_lock_attr(self, attr_name: str) -> None:
        """
        Hard lock's an attribute name from re-assignment, deletion, and cannot be unlocked
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_attr_name_exist = "Hard locked attribute name does not exist! Must be created first to lock"
        __err_msg_attr_name_locked = "Attribute name already hard locked! Cannot be re-locked once locked"
        __err_msg_attr_name_other_lock = "Attribute name exists with other lock (lock_attr) already! Cannot be locked with multiple locks"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nATTR_NAME: "{attr_name}"')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nATTR_NAME: "{attr_name}"')

        # Assign Attr to Locked Tuple if Does Not Preexist
        if attr_name in self.__assignment_hard_locked_attribs:
            raise GeneralError(__err_msg_attr_name_locked, f'\nATTR_NAME: "{attr_name}"')
        if attr_name in self.__assignment_locked_attribs:
            raise GeneralError(__err_msg_attr_name_other_lock, f'\nATTR_NAME: "{attr_name}"')

        self.__dict__['_MaciDataObjConstructor__assignment_hard_locked_attribs'] = (*self.__assignment_hard_locked_attribs, attr_name)


    def lock_attr(self, attr_name: str) -> None:
        """
        Lock's an attribute name from re-assignment
        """
        # Error Checks
        __err_msg_attr_name_str = "Only str is allowed for attr_name"
        __err_msg_attr_name_exist = "Locked attribute name does not exist! Must be created first to lock"
        __err_msg_attr_name_locked = "Attribute name already locked! Cannot be re-locked once locked"
        __err_msg_attr_name_other_lock = "Attribute name exists with other lock (hard_lock_attr) already! Cannot be locked with multiple locks"

        if not isinstance(attr_name, str): raise GeneralError(__err_msg_attr_name_str, f'\nATTR_NAME: "{attr_name}"')
        if not attr_name in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nATTR_NAME: "{attr_name}"')

        # Assign Attr to Locked List if Does Not Preexist
        if attr_name in self.__assignment_locked_attribs:
            raise GeneralError(__err_msg_attr_name_locked, f'\nATTR_NAME: "{attr_name}"')
        if attr_name in self.__assignment_hard_locked_attribs:
            raise GeneralError(__err_msg_attr_name_other_lock, f'\nATTR_NAME: "{attr_name}"')

        self.__assignment_locked_attribs.append(attr_name)


    def unlock_attr(self, attr_name: str) -> None:
        """
        Unlocks a attribute name from locked re-assignment
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


    def link_attr(self, child_attr: str, parent_attr: str) -> None:
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

        if not isinstance(child_attr, str): raise GeneralError(__err_msg_attr_name_str, f'\nATTR_NAME: "{child_attr}"')
        if not isinstance(parent_attr, str): raise GeneralError(__err_msg_reference_name_str, f'\nATTR_NAME: "{parent_attr}"')

        # Look up if Attr or Reference Name Exists
        if not child_attr in self.__dict__: raise GeneralError(__err_msg_attr_name_exist, f'\nATTR_NAME: "{child_attr}"')
        if not parent_attr in self.__dict__: raise GeneralError(__err_msg_reference_name_exist, f'\nATTR_NAME: "{parent_attr}"')

        # Set Value to Reference Value
        setattr(self, child_attr, getattr(self, parent_attr))
    
        # Assign Attr Name to Reference Name in Reference Maps
        self.__assigned_src_reference_attr_map[child_attr] = parent_attr
        self.__assigned_dst_reference_attr_map.setdefault(parent_attr, {}).setdefault(child_attr, parent_attr)


    def __reference_deletion_check(self, _name: str, *, _src_ref_list: bool=False, _dst_ref_list: bool=False, _lock_list: bool=False) -> _NoReturn:
        """
        Internal method: check if reference requires deletion from reference list
        if attribute is attempted to be re-assigned
        """
        # General Lock Attrs
        if _lock_list:
            if _name in self.__assignment_locked_attribs:
                self.__assignment_locked_attribs.remove(_name)

        # Reference Attrs - Must maintain reference map if attr in any locks
        
        # Source Reference List
        if _src_ref_list:
            if _name in self.__assigned_src_reference_attr_map:
                _is_locked = _name in self.__assignment_locked_attribs
                _is_hard_locked = _name in self.__assignment_hard_locked_attribs
                
                if not (_is_locked or _is_hard_locked):
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
                
                if not (_is_locked or _is_hard_locked):
                    # Release Source References
                    for key in self.__assigned_dst_reference_attr_map[_name]:
                        self.__assigned_src_reference_attr_map.pop(key)
                    # Release Destination Reference
                    self.__assigned_dst_reference_attr_map.pop(_name)


    def get_locked_list(self) -> _List[str]:
        """
        General locked list

        Returns a copy of the current list of locked attributes
        """
        return self.__assignment_locked_attribs.copy()
    

    def get_hard_locked_list(self) -> _List[str]:
        """
        Hard locked list

        Returns a new list of the current hard locked attributes
        """
        return list(self.__assignment_hard_locked_attribs)
    

    def get_all_links(self) -> _Dict[str, _Dict[str, _Union[str, _Dict[str, str]]]]:
        """
        Get all Parent and Child Links

        Returns a new dict of the current parent and child link reference maps

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Parent map will be -> 'parent_link_map': {'attr_parent': {'attr_child': 'attr_parent'}}

        Child map will be -> 'child_link_map': {'attr_child': 'attr_parent'}
        """
        return {'parent_link_map': deepcopy(self.__assigned_dst_reference_attr_map), 'child_link_map': deepcopy(self.__assigned_src_reference_attr_map)}


    def get_parent_links(self) -> _Dict[str, _Dict[str, str]]:
        """
        Get all Parent Links

        Returns a new dict of the current parent link reference map

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Parent map will be -> {'attr_parent': {'attr_child': 'attr_parent'}}
        """
        return deepcopy(self.__assigned_dst_reference_attr_map)


    def get_parent_chains(self, parent_attr: _Optional[str]=None, *, dup_link_check: bool=True) -> _Union[_Dict[str, _List[str]], _List[str]]:
        """
        Get Parent Chains

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
        The true linking is controlled by other mechs.

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

        if not isinstance(parent_attr, (str, type(None))): raise GeneralError(err_msg_parent_name_type, f'\nGOT: {parent_attr}')
        if not isinstance(dup_link_check, bool): raise GeneralError(err_msg_dup_link_chk_type, f'\nGOT: {dup_link_check}')

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
                f"\nGOT: {parent_attr}"
            )

        # Return single parent chain if specified, otherwise continue build
        if parent_attr in all_parent_chains:
            return all_parent_chains[parent_attr]

        # Return all chains if no parent specified
        return all_parent_chains


    def get_child_links(self) -> _Dict[str, str]:
        """
        Get all Child Links

        Returns a new dict of the current child link reference map

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Child map will be -> {'attr_child': 'attr_parent'}
        """
        return deepcopy(self.__assigned_src_reference_attr_map)


    # Name compatibility aliases/deprecation from ported library
    def __getattr__(self, attr_name: str) -> object:
        if attr_name == 'reference_attr': return self.link_attr

        # Raise normal error if anything else
        raise_msg = f"'{type(self).__name__}' object has no attribute '{attr_name}'"
        raise AttributeError(raise_msg)


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
        _is_hint_request: bool=False,
    )-> None:
        __constructor_locked = True
        __constructor_locked = False if (_is_load_request
                                        or _is_build_request
                                        or _is_hint_request
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
        if not __constructor_locked:
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
                _is_hint_request=_is_hint_request
            )

    def __repr__(self) -> str:
        skip_name_keys = ('_MaciDataObjConstructor', '__maci_file_format_id')
        build_repr = ', '.join([f"{name}={value!r}" for name,value in vars(self).items() if not name.startswith(skip_name_keys)])
        return f"{type(self).__name__}({build_repr})"
