"""
stub file to document public api class and methods types, and doc string comments
"""
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List
from typing import Union as _Union
from typing import Optional as _Optional

#########################################################################################################
# Stub data

### Classes ###
class MaciDataObj:
    
    def hard_lock_attr(self, attr_name: str) -> None:
        """
        Hard lock's an attribute name from re-assignment, deletion, and cannot be unlocked
        """
        
    def lock_attr(self, attr_name: str) -> None:
        """
        Lock's an attribute name from re-assignment
        """
        
    def unlock_attr(self, attr_name: str) -> None:
        """
        Unlocks a attribute name from locked re-assignment
        """
        
    def map_attr(self, child_attr: str, parent_attr: str) -> None:
        """
        Create a link of an attribute name to another attribute name

        This will auto assign/track the value of the parent attr to the child attr

        Useful to maintain references and follow values of other attributes. Similar
        to the concept of a pointer.
        """
        
    def unmap_attr(self, attr_name: str) -> None:
        """
        Unlink an attribute name from another attribute name

        This will detach the link between the child attr and parent attr

        If it is a parent attr, all child links will be detached from that parent
        """
        
    def is_parent_map(self, attr_name: str) -> bool:
        """
        Check if attr is a parent link

        Returns: True if Parent, and False if not
        """
        
    def is_child_map(self, attr_name: str) -> bool:
        """
        Check if attr is a child link

        Returns: True if Child, and False if not
        """

    def get_locked_list(self) -> _List[str]:
        """
        General locked list

        Returns a copy of the current list of locked attributes
        """
        
    def get_hard_locked_list(self) -> _List[str]:
        """
        Hard locked list

        Returns a new list of the current hard locked attributes
        """
        
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
        
    def get_parent_maps(self) -> _Dict[str, _Dict[str, str]]:
        """
        Get all Parent Links

        Returns a new dict of the current parent link reference map

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Parent map will be -> {'attr_parent': {'attr_child': 'attr_parent'}}
        """
        
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
        
    def get_child_maps(self) -> _Dict[str, str]:
        """
        Get all Child Links

        Returns a new dict of the current child link reference map

        [Example Map Structure]

        attr_parent = 'some value'

        attr_child == attr_parent

        Child map will be -> {'attr_child': 'attr_parent'}
        """
