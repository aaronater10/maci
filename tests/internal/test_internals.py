# Internals - Tests
from src import maci
import pytest

################################################################
# Tests

# 1. Internal Name Protection
def test1_internal_name_protection():
    # Build Data
    maci_data = maci.build()

    internal_maci_attr_names = [
        '_MaciDataObjConstructor__assignment_hard_locked_attribs',
        '_MaciDataObjConstructor__assignment_locked_attribs',
        '_MaciDataObjConstructor__assigned_src_reference_attr_map',
        '_MaciDataObjConstructor__assigned_dst_reference_attr_map'
    ]
    internal_maci_methods = [
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
        '_MaciDataObjConstructor__reference_deletion_check'
    ]


    # Tests

    ### ATTRS ###
    # Protect from Re-Assignment by Raise
    for attr_name in internal_maci_attr_names:
        with pytest.raises(maci.error.GeneralError):
            setattr(maci_data, attr_name, None)

    # Protect from Deletion by Raise
    for attr_name in internal_maci_attr_names:
        with pytest.raises(maci.error.GeneralError):
            delattr(maci_data, attr_name)
    

    ### METHODS ###
    # Protect from Re-Assignment by Raise
    for method_name in internal_maci_methods:
        with pytest.raises(maci.error.GeneralError):
            setattr(maci_data, method_name, None)
    # Object methods cannot be deleted and throws normal attr error
