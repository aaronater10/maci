# exceptions: MaciDataObj Method - Tests
from src import maci
import pytest


################################################################
# TESTS

# 1. General: Object Rename Wrapper - TypeError with MaciDataObj.* name
def test1_exc_maciobj_method_general_object_rename_wrapper():
    # Build Data
    maci_data = maci.build() 

    # Tests
    with pytest.raises(TypeError):
        maci_data.is_parent_map()
    with pytest.raises(TypeError):
        maci_data.is_child_map()
    with pytest.raises(TypeError):
        maci_data.get_all_maps('')
    with pytest.raises(TypeError):
        maci_data.get_child_maps('')
    with pytest.raises(TypeError):
        maci_data.get_parent_maps('')
    with pytest.raises(TypeError):
        maci_data.get_parent_map_chains('', '')
    with pytest.raises(TypeError):
        maci_data.get_hard_locked_list('')
    with pytest.raises(TypeError):
        maci_data.get_locked_list('')
    with pytest.raises(TypeError):
        maci_data.hard_lock_attr()
    with pytest.raises(TypeError):
        maci_data.lock_attr()
    with pytest.raises(TypeError):
        maci_data.unlock_attr()
    with pytest.raises(TypeError):
        maci_data.map_attr()
    with pytest.raises(TypeError):
        maci_data.unmap_attr()


# 1. get_parent_map_chains - Type Checks
def test1_exc_maciobj_method_get_parent_map_chains_types():
    # Build Data
    maci_data = maci.build()    

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.get_parent_map_chains(parent_attr=1.0)
    with pytest.raises(maci.error.GeneralError):
        maci_data.get_parent_map_chains(parent_attr="", dup_link_check=1.0)    


# 2. get_parent_map_chains - Unsupported Options or Data
def test2_exc_maciobj_method_get_parent_map_chains_opts_data():
    # Build Data
    maci_data = maci.build() 

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.get_parent_map_chains(parent_attr="") 



# 1. hard_lock_attr - Type Checks
def test1_exc_maciobj_method_hard_lock_attr_types():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.hard_lock_attr(attr_name=1.0)  


# 2. hard_lock_attr - Unsupported Options or Data
def test2_exc_maciobj_method_hard_lock_attr_opts_data():
    # Build Data
    maci_data = maci.build() 

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.hard_lock_attr(attr_name="")



# 1. lock_attr - Type Checks
def test1_exc_maciobj_method_lock_attr_types():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.lock_attr(attr_name=1.0)  


# 2. lock_attr - Unsupported Options or Data
def test2_exc_maciobj_method_lock_attr_opts_data():
    # Build Data
    maci_data = maci.build() 

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.lock_attr(attr_name="")



# 1. is_child_map - Type Checks
def test1_exc_maciobj_method_is_child_map_types():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.is_child_map(attr_name=1.0)  


# 2. is_child_map - Unsupported Options or Data
def test2_exc_maciobj_method_is_child_map_opts_data():
    # Build Data
    maci_data = maci.build() 

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.is_child_map(attr_name="")



# 1. is_parent_map - Type Checks
def test1_exc_maciobj_method_is_parent_map_types():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.is_parent_map(attr_name=1.0)  


# 2. is_parent_map - Unsupported Options or Data
def test2_exc_maciobj_method_is_parent_map_opts_data():
    # Build Data
    maci_data = maci.build() 

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.is_parent_map(attr_name="")



# 1. map_attr - Type Checks
def test1_exc_maciobj_method_map_attr_types():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.map_attr(child_attr=1.0, parent_attr="")
    with pytest.raises(maci.error.GeneralError):
        maci_data.map_attr(child_attr="", parent_attr=1.0)  


# 2. map_attr - Unsupported Options or Data
def test2_exc_maciobj_method_map_attr_opts_data():
    # Build Data
    maci_data = maci.build()
    maci_data.child = 1
    maci_data.parent = 1

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.map_attr(child_attr="", parent_attr="parent")
    with pytest.raises(maci.error.GeneralError):
        maci_data.map_attr(child_attr="child", parent_attr="")



# 1. unlock_attr - Type Checks
def test1_exc_maciobj_method_unlock_attr_types():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.unlock_attr(attr_name=1.0)  


# 2. unlock_attr - Unsupported Options or Data
def test2_exc_maciobj_method_unlock_attr_opts_data():
    # Build Data
    maci_data = maci.build() 

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.unlock_attr(attr_name="")



# 1. unmap_attr - Type Checks
def test1_exc_maciobj_method_unmap_attr_types():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.unmap_attr(attr_name=1.0)


# 2. unmap_attr - Unsupported Options or Data
def test2_exc_maciobj_method_unmap_attr_opts_data():
    # Build Data
    maci_data = maci.build()
    maci_data.child = 1
    maci_data.parent = 1

    # Tests
    with pytest.raises(maci.error.GeneralError):
        maci_data.unmap_attr(attr_name="")
