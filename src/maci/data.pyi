# stub file to document public api class and methods types, and doc string comments
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List
from typing import Union as _Union
from typing import Optional as _Optional
from typing import TypeVar as _TypeVar

#########################################################################################################
# Stub data: Classes

class MaciDataObj:
    """
    maci data object
    """
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
    )-> None: pass

    def hard_lock_attr(self, attr_name: str) -> None:
        """
        Hard lock's an attribute name from re-assignment, deletion, and cannot be unlocked
        """
        
    def lock_attr(self, attr_name: str) -> None:
        """
        Lock's an attribute name from re-assignment. Can be unlocked

        [Partner Functions]

        unlock_attr: unlocks an attribute from being locked
        """
        
    def unlock_attr(self, attr_name: str) -> None:
        """
        Unlocks an attribute name that is locked from re-assignment
        """
        
    def map_attr(self, child_attr: str, parent_attr: str) -> None:
        """
        Map an attribute name to another attribute name to follow its value

        This works similar to the concept of a pointer, and references
        the parent attr value it is mapped to. It also maintains reference to the same object in memory naturally
        from python's inherent optimization design

        [Partner Functions]

        unmap_attr: unmaps a child attr from being mapped to a parent attr. If parent, unmaps all children

        [Note]

        Re-assignment: If a child attr is re-assigned to another value or attr, it will release its map to the current parent attr

        Locked: If a child attr is locked, and the parent attr changes its value, the parent attr value will change,
        but the child attr value will not change and throw an exception

        """
        
    def unmap_attr(self, attr_name: str) -> None:
        """
        Unmap a child attribute name from a parent attribute name

        This will release the map between the child attr and parent attr

        If a parent attr is specified, all child maps will be detached from that parent
        """

    def is_parent_map(self, attr_name: str) -> bool:
        """
        Check if attr is a parent mapped with children

        Returns: True if Parent, and False if not
        """
        
    def is_child_map(self, attr_name: str) -> bool:
        """
        Check if attr is a child mapped to a parent

        Returns: True if Child, and False if not
        """

    def get_locked_list(self) -> _List[str]:
        """
        Returns a copy of the current list of locked attributes
        """
        
    def get_hard_locked_list(self) -> _List[str]:
        """
        Returns a copy of the current list of hard locked attributes
        """
        
    def get_all_maps(self) -> _Dict[str, _Dict[str, _Any]]:
        """
        Returns a new dict of the current parent and child reference maps

        [Example: Map Structure]

        {
        
        'parent_maps': {'attr_parent1': {'attr_child1': 'attr_parent1'}},

        'child_maps': {'attr_child1': 'attr_parent1'}
        
        }
        """
        
    def get_parent_maps(self) -> _Dict[str, _Dict[str, str]]:
        """
        Returns a new dict of the current parent reference maps

        [Example: Map Structure]

        {'attr_parent1': {'attr_child1': 'attr_parent1'}, 'attr_parent2': {'attr_child2': 'attr_parent2'}}
        """
        
    def get_parent_map_chains(self, parent_attr: _Optional[str]=None, *, dup_link_check: bool=True) -> _Union[_Dict[str, _List[str]], _List[str]]:
        """
        Builds a unique chain like structure of attr names that are currently linked or chained together by interconnected children with
        the very top chain link being their parent

        Actual chains are represented as a list with the parent being first and the children to follow

        Chains are built from scratch each time this is called

        [Example: Chain Structure]

        Parent not specified: {'attr_parent': ['attr_parent', 'attr_child1', 'attr_child2', 'attr_child3']}

        Parent specified: ['attr_parent', 'attr_child1', 'attr_child2', 'attr_child3']

        [Options]

        dup_link_check: Default=True - Protects against duplicate links being built to the parent. If disabled and a duplicate is found, it 
        will still return chain(s), but will cut the chain's previous links to the parent and only continue the chain from the
        last reference to the parent and retain any chain links following the last reference (see note below to clear any concerns).
        
        Note: It is worth stating, this method does not break/affect the actual behavior of the attributes being linked together, as this method only fresh builds a representation
        of the attributes linked together in the form of a chain for your reference to help understand what attribute names are connected to each other.
        The true linking is controlled by other mechs, and any real duplicate links are not affected as that is acceptable behavior.

        """
        
    def get_child_maps(self) -> _Dict[str, str]:
        """
        Returns a new dict of the current child reference maps

        [Example: Map Structure]

        {'attr_child1': 'attr_parent1', 'attr_child2': 'attr_parent1'}
        """
    
    def get_attrs(self) -> _Dict[str, _Any]:
        """
        Returns a dict copy of the MaciDataObj's current attribute names and values
        """

    def load_attrs(self, data: _Dict[str, _Any]) -> None:
        """
        Loads data from a dict into the MaciDataObj in-place
        
        Creates new attribute names with their values retained based on the top level key names of the dict

        Note: If the key name is not a valid pythonic name convention, it will be skipped
        """
    
    def __getattr__(self, _name: str) -> _Any:
        ...

    def __setattr__(self, _name: str, _new_value: _Any) -> None:
        ...
    
    def __dir__(self) -> _List[str]:
        ...


#########################################################################################################
# Stub data: Functions

# Hinting reference name for "ClassObject" to denote a ClassObject can be used to dump data
ClassObject = _TypeVar('ClassObject')

def __dump_data(
    *,
    _is_string_request: bool=False,
    filename: str,
    data: _Union[MaciDataObj, dict, ClassObject],
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