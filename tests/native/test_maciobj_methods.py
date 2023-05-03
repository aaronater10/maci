# MaciDataObj Method - Tests
from src import maci
from os import remove
import pytest
import time

test_file_path = './tests/test_files/native/maciobj_method_files/'
file_delay_timer = 0.25

################################################################
# TESTS

# 1. MaciDataObj - Test Integrity of Glyphs from Build -> Dump -> Load
def test1_maciobj_methods_glyph_integrity():
    filename = '1_maciobj_methods_glyph_integrity.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Build Data
    file_data = maci.build()
    file_data.norm_data = 'data'
    file_data.map_data = None
    file_data.lock_data = 'data'
    file_data.hard_lock_data = 'data'
    file_data.map_lock = None
    file_data.map_hard_lock = None

    # Setup Attrs
    file_data.map_attr('map_data', 'norm_data')
    file_data.lock_attr('lock_data')
    file_data.hard_lock_attr('hard_lock_data')

    file_data.map_attr('map_lock', 'lock_data')
    file_data.lock_attr('map_lock')

    file_data.map_attr('map_hard_lock', 'hard_lock_data')
    file_data.hard_lock_attr('map_hard_lock')

    # Test dump with symbols and test data
    maci.dump(filepath, file_data)
    file_import = maci.load(filepath)

    # Test Data
    assert file_import.norm_data == 'data'
    assert file_import.map_data == 'data'
    assert file_import.lock_data == 'data'
    assert file_import.hard_lock_data == 'data'
    assert file_import.map_lock == 'data'
    assert file_import.map_hard_lock == 'data'

    assert 'norm_data' in file_import.get_parent_maps()
    assert 'lock_data' in file_import.get_parent_maps()
    assert 'hard_lock_data' in file_import.get_parent_maps()
    assert 'map_data' in file_import.get_child_maps()
    assert 'lock_data' in file_import.get_locked_list()
    assert 'hard_lock_data' in file_import.get_hard_locked_list()
    assert 'map_lock' in file_import.get_child_maps() and 'map_lock' in file_import.get_locked_list()
    assert 'map_hard_lock' in file_import.get_child_maps() and 'map_hard_lock' in file_import.get_hard_locked_list()
    assert file_data.get_all_maps() == {'parent_link_map': {'norm_data': {'map_data': 'norm_data'}, 'lock_data': {'map_lock': 'lock_data'}, 'hard_lock_data': {'map_hard_lock': 'hard_lock_data'}}, 'child_link_map': {'map_data': 'norm_data', 'map_lock': 'lock_data', 'map_hard_lock': 'hard_lock_data'}}

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. MaciDataObj - MAP: Test Parent/Child map structure and data
def test2_maciobj_methods_parent_child_map_structure():
    # Build Data
    maci_data = maci.build()
    maci_data.norm_data = 'data'
    maci_data.map_data = None

    # Setup Attrs
    maci_data.map_attr('map_data', 'norm_data')

    # Test Data and Parent/Child Map Structure is Correct
    assert maci_data.map_data == 'data'
    assert 'norm_data' in maci_data.get_parent_maps()
    assert 'norm_data' == maci_data.get_parent_maps()['norm_data']['map_data']
    assert 'map_data' in maci_data.get_child_maps()
    assert 'norm_data' == maci_data.get_child_maps()['map_data']


# 3. MaciDataObj - MAP: Test Parent/Child is their respective map types
def test3_maciobj_methods_is_parent_child_map():
    # Build Data
    maci_data = maci.build()
    maci_data.norm_data = 'data'
    maci_data.map_data = None

    # Setup Attrs
    maci_data.map_attr('map_data', 'norm_data')

    # Test Data and Parent/Child Map Type is Correct
    assert maci_data.map_data == 'data'
    assert maci_data.is_parent_map('norm_data')
    assert maci_data.is_child_map('map_data')


# 4. MaciDataObj - MAP: Test Parent/Child large map structure, data, and sources
def test4_maciobj_methods_parent_child_large_map_and_sources():
    # Build Data
    maci_data = maci.build()
    maci_data.norm_data1 = 'data1'
    maci_data.map_data1 = None
    maci_data.map_data2 = None
    maci_data.map_data3 = None
    maci_data.norm_data2 = 'data2'
    maci_data.map_data4 = None
    maci_data.map_data5 = None
    maci_data.map_data6 = None

    # Setup Attrs
    maci_data.map_attr('map_data1', 'norm_data1')
    maci_data.map_attr('map_data2', 'norm_data1')
    maci_data.map_attr('map_data3', 'norm_data1')

    maci_data.map_attr('map_data4', 'norm_data2')
    maci_data.map_attr('map_data5', 'norm_data2')
    maci_data.map_attr('map_data6', 'norm_data2')

    # Test Data and Parent/Child Map Structure is Correct

    # Data
    assert maci_data.map_data1 == 'data1'
    assert maci_data.map_data2 == 'data1'
    assert maci_data.map_data3 == 'data1'

    assert maci_data.map_data4 == 'data2'
    assert maci_data.map_data5 == 'data2'
    assert maci_data.map_data6 == 'data2'

    # Map Sources Match
    assert maci_data._MaciDataObjConstructor__assigned_dst_reference_attr_map == maci_data.get_parent_maps()
    assert maci_data._MaciDataObjConstructor__assigned_src_reference_attr_map == maci_data.get_child_maps()

    # Map Methods Match Data Structure
    assert maci_data.get_all_maps() == {'parent_link_map': {'norm_data1': {'map_data1': 'norm_data1', 'map_data2': 'norm_data1', 'map_data3': 'norm_data1'}, 'norm_data2': {'map_data4': 'norm_data2', 'map_data5': 'norm_data2', 'map_data6': 'norm_data2'}}, 'child_link_map': {'map_data1': 'norm_data1', 'map_data2': 'norm_data1', 'map_data3': 'norm_data1', 'map_data4': 'norm_data2', 'map_data5': 'norm_data2', 'map_data6': 'norm_data2'}}
    assert maci_data.get_parent_maps() == {'norm_data1': {'map_data1': 'norm_data1', 'map_data2': 'norm_data1', 'map_data3': 'norm_data1'}, 'norm_data2': {'map_data4': 'norm_data2', 'map_data5': 'norm_data2', 'map_data6': 'norm_data2'}}
    assert maci_data.get_child_maps() == {'map_data1': 'norm_data1', 'map_data2': 'norm_data1', 'map_data3': 'norm_data1', 'map_data4': 'norm_data2', 'map_data5': 'norm_data2', 'map_data6': 'norm_data2'}


# 5. MaciDataObj - MAP: Test Parent Chain Data and Structure
def test5_maciobj_methods_map_parent_chains():
    # Build Data
    maci_data = maci.build()
    maci_data.norm_data1 = 'data1'
    maci_data.map_data1 = None
    maci_data.map_data2 = None
    maci_data.norm_data2 = 'data2'
    maci_data.map_data3 = None
    maci_data.map_data4 = None

    # Setup Attrs
    maci_data.map_attr('map_data1', 'norm_data1')
    maci_data.map_attr('map_data2', 'map_data1')

    maci_data.map_attr('map_data3', 'norm_data2')
    maci_data.map_attr('map_data4', 'map_data3')

    # Test Data and Parent/Child Map Chain Data and Structure is Correct
    assert maci_data.map_data1 == 'data1'
    assert maci_data.map_data2 == 'data1'

    assert maci_data.map_data3 == 'data2'
    assert maci_data.map_data4 == 'data2'

    assert maci_data.get_parent_map_chains() ==  {'norm_data1': ['norm_data1', 'map_data1', 'map_data2'], 'norm_data2': ['norm_data2', 'map_data3', 'map_data4']}
    assert maci_data.get_parent_map_chains('norm_data1') ==  ['norm_data1', 'map_data1', 'map_data2']
    assert maci_data.get_parent_map_chains('norm_data2') ==  ['norm_data2', 'map_data3', 'map_data4']

    ### Test: Dup Link Check (ON by Default) ###
    
    # Build Data
    maci_data = maci.build()
    maci_data.norm_data1 = 'data1'
    maci_data.map_data1 = None
    maci_data.map_data2 = None
    maci_data.norm_data2 = 'data2'
    maci_data.map_data3 = None
    maci_data.map_data4 = None

    # Setup Attrs
    maci_data.map_attr('map_data1', 'norm_data1')
    maci_data.map_attr('map_data2', 'norm_data1')

    maci_data.map_attr('map_data3', 'norm_data2')
    maci_data.map_attr('map_data4', 'norm_data2')

    # ON: Check if an Exception Raised - Using Maci Base Exception
    with pytest.raises(maci.error.MaciError):
        maci_data.get_parent_map_chains()
    
    # OFF: Test if Links are Re-Built with it OFF
    assert maci_data.get_parent_map_chains(dup_link_check=False) == {'norm_data1': ['norm_data1', 'map_data2'], 'norm_data2': ['norm_data2', 'map_data4']}
    assert maci_data.get_parent_map_chains('norm_data1', dup_link_check=False) == ['norm_data1', 'map_data2']
    assert maci_data.get_parent_map_chains('norm_data2', dup_link_check=False) == ['norm_data2', 'map_data4']


# 6. MaciDataObj - UNMAP: Test Map being Unmapped Directly and Indirectly
def test6_maciobj_methods_map_data_followed():
    # Build Data
    maci_data = maci.build()
    maci_data.norm_data1 = 'ring_data'
    maci_data.map_data1 = None
    maci_data.map_data2 = None
    maci_data.map_data3 = None

    maci_data.norm_data2 = 'chain_data'
    maci_data.map_data4 = None
    maci_data.map_data5 = None
    maci_data.map_data6 = None

    # Setup Attrs: Ring Style, then Chain Style

    # RING
    maci_data.map_attr('map_data1', 'norm_data1')
    maci_data.map_attr('map_data2', 'norm_data1')
    maci_data.map_attr('map_data3', 'norm_data1')

    # CHAIN
    maci_data.map_attr('map_data4', 'norm_data2')
    maci_data.map_attr('map_data5', 'map_data4')
    maci_data.map_attr('map_data6', 'map_data5')

    # Test Map Data, and Ring Data & Chain Data is Followed by Parent Re-Assignment
    assert maci_data.map_data1 == 'ring_data'
    assert maci_data.map_data2 == 'ring_data'
    assert maci_data.map_data3 == 'ring_data'
    assert maci_data.map_data4 == 'chain_data'
    assert maci_data.map_data5 == 'chain_data'
    assert maci_data.map_data6 == 'chain_data'

    # RING: Parent Data Changed "norm_data1"
    maci_data.norm_data1 = 'ring_data_changed'
    assert maci_data.map_data1 == 'ring_data_changed'
    assert maci_data.map_data2 == 'ring_data_changed'
    assert maci_data.map_data3 == 'ring_data_changed'

    # CHAIN: Parent Data Changed "norm_data2"
    maci_data.norm_data2 = 'chain_data_changed'
    assert maci_data.map_data4 == 'chain_data_changed'
    assert maci_data.map_data5 == 'chain_data_changed'
    assert maci_data.map_data6 == 'chain_data_changed'


# 7. MaciDataObj - UNMAP: Test Map being Unmapped Directly and Indirectly
def test7_maciobj_methods_unmap_direct_indirect():
    # Build Data
    maci_data = maci.build()
    maci_data.norm_data1 = 'data1'
    maci_data.map_data1 = None
    maci_data.map_data2 = None

    maci_data.norm_data2 = 'data2'
    maci_data.map_data3 = None
    maci_data.map_data4 = None

    # Setup Attrs
    maci_data.map_attr('map_data1', 'norm_data1')
    maci_data.map_attr('map_data2', 'norm_data1')

    maci_data.map_attr('map_data3', 'norm_data2')
    maci_data.map_attr('map_data4', 'norm_data2')

    # Test Map Data and Unmap
    assert maci_data.map_data1 == 'data1'
    assert maci_data.map_data2 == 'data1'
    assert maci_data.map_data3 == 'data2'
    assert maci_data.map_data4 == 'data2'
    assert 'map_data1' in maci_data.get_child_maps()
    assert 'map_data2' in maci_data.get_child_maps()
    assert 'map_data3' in maci_data.get_child_maps()
    assert 'map_data4' in maci_data.get_child_maps()

    # UNMAP Child: Direct "map_data1" - Parent Map Still Intact
    maci_data.unmap_attr('map_data1')
    assert 'map_data1' not in maci_data.get_child_maps()
    assert 'norm_data1' in maci_data.get_parent_maps()

    # UNMAP Child: InDirect "map_data2" (From Value Re-Assignment)
    maci_data.map_data2 = None
    assert 'map_data2' not in maci_data.get_child_maps()

    # UNMAP Parent: Direct "norm_data2" - Parent Map Still Intact
    maci_data.unmap_attr('norm_data2')
    assert 'map_data3' not in maci_data.get_child_maps()
    assert 'map_data4' not in maci_data.get_child_maps()

    # Test Maps Empty
    assert maci_data.get_parent_maps() ==  {}
    assert maci_data.get_parent_map_chains() ==  {}
    assert maci_data.get_child_maps() ==  {}
