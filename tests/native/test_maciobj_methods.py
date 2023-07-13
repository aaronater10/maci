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
    assert file_data.get_all_maps() == {'parent_maps': {'norm_data': {'map_data': 'norm_data'}, 'lock_data': {'map_lock': 'lock_data'}, 'hard_lock_data': {'map_hard_lock': 'hard_lock_data'}}, 'child_maps': {'map_data': 'norm_data', 'map_lock': 'lock_data', 'map_hard_lock': 'hard_lock_data'}}

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
    assert maci_data.get_all_maps() == {'parent_maps': {'norm_data1': {'map_data1': 'norm_data1', 'map_data2': 'norm_data1', 'map_data3': 'norm_data1'}, 'norm_data2': {'map_data4': 'norm_data2', 'map_data5': 'norm_data2', 'map_data6': 'norm_data2'}}, 'child_maps': {'map_data1': 'norm_data1', 'map_data2': 'norm_data1', 'map_data3': 'norm_data1', 'map_data4': 'norm_data2', 'map_data5': 'norm_data2', 'map_data6': 'norm_data2'}}
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


    ### Test: Breaking a link in chain (from Deletion or Re-Assignment) ###

    # Build Data
    maci_data = maci.build()
    maci_data.norm_data1 = 'data1'
    maci_data.map_data1 = None
    maci_data.map_data2 = None
    maci_data.map_data3 = None
    maci_data.map_data4 = None
    
    # Setup Attrs
    maci_data.map_attr('map_data1', 'norm_data1')
    maci_data.map_attr('map_data2', 'map_data1')
    maci_data.map_attr('map_data3', 'map_data2')
    maci_data.map_attr('map_data4', 'map_data3')

    # Test Data and Parent/Child Map Chain Data and Structure is Correct

    # Normal
    assert maci_data.get_parent_map_chains() == {'norm_data1': ['norm_data1', 'map_data1', 'map_data2', 'map_data3', 'map_data4']}
    
    # RE-ASSIGN Attr: Break in Chain from re-assignment
    maci_data.map_data2 = None
    assert maci_data.get_parent_map_chains() == {'norm_data1': ['norm_data1', 'map_data1'], 'map_data2': ['map_data2', 'map_data3', 'map_data4']}

    # DELETE Attr: Break in Chain from re-assignment
    del maci_data.map_data2
    assert maci_data.get_parent_map_chains() == {'norm_data1': ['norm_data1', 'map_data1'], 'map_data3': ['map_data3', 'map_data4']}


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

    # ON: Check if an Exceptions Raised - Using Maci Base Exception
    with pytest.raises(maci.error.MaciError):
        maci_data.get_parent_map_chains()
    with pytest.raises(maci.error.MaciError):
        maci_data.get_parent_map_chains('norm_data1')
    
    # OFF: Test if Links are Re-Built with it OFF
    assert maci_data.get_parent_map_chains(dup_link_check=False) == {'norm_data1': ['norm_data1', 'map_data2'], 'norm_data2': ['norm_data2', 'map_data4']}
    assert maci_data.get_parent_map_chains('norm_data1', dup_link_check=False) == ['norm_data1', 'map_data2']
    assert maci_data.get_parent_map_chains('norm_data2', dup_link_check=False) == ['norm_data2', 'map_data4']


# 6. MaciDataObj - MAP: Test children is following parent data properly
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

    maci_data.norm_data3 = 'data3'
    maci_data.map_data5 = None
    maci_data.map_data6 = None

    maci_data.unmapped_attr = 1.0

    # Setup Attrs
    maci_data.map_attr('map_data1', 'norm_data1')
    maci_data.map_attr('map_data2', 'norm_data1')

    maci_data.map_attr('map_data3', 'norm_data2')
    maci_data.map_attr('map_data4', 'norm_data2')

    maci_data.map_attr('map_data5', 'norm_data3')
    maci_data.map_attr('map_data6', 'norm_data3')

    # Test Map Data and Unmap
    assert maci_data.map_data1 == 'data1'
    assert maci_data.map_data2 == 'data1'
    assert maci_data.map_data3 == 'data2'
    assert maci_data.map_data4 == 'data2'
    assert maci_data.map_data5 == 'data3'
    assert maci_data.map_data6 == 'data3'
    assert 'map_data1' in maci_data.get_child_maps()
    assert 'map_data2' in maci_data.get_child_maps()
    assert 'map_data3' in maci_data.get_child_maps()
    assert 'map_data4' in maci_data.get_child_maps()
    assert 'map_data5' in maci_data.get_child_maps()
    assert 'map_data6' in maci_data.get_child_maps()

    # Test: Parent: norm_data1 - Children: map_data1, map_data2

    # UNMAP Child: Direct "map_data1" - Parent Map Still Intact
    maci_data.unmap_attr('map_data1')
    assert 'map_data1' not in maci_data.get_child_maps()
    assert 'norm_data1' in maci_data.get_parent_maps()

    # UNMAP Child: InDirect "map_data2" (From Value Re-Assignment)
    maci_data.map_data2 = None
    assert 'map_data2' not in maci_data.get_child_maps()

    # Test: Parent: norm_data2 - Children: map_data3, map_data4

    # UNMAP Parent: Direct "norm_data2" - Parent Map Still Intact
    maci_data.unmap_attr('norm_data2')
    assert 'map_data3' not in maci_data.get_child_maps()
    assert 'map_data4' not in maci_data.get_child_maps()

    # Test: Parent: norm_data3 - Children: map_data5, map_data6

    # UNMAP Child: InDirect "map_data5" (From Attribute Deletion)
    del maci_data.map_data5
    assert 'map_data5' not in maci_data.get_child_maps()

    # UNMAP Parent: InDirect "norm_data3" and "map_data6" (From Attribute Deletion)
    del maci_data.norm_data3
    assert 'norm_data3' not in maci_data.get_parent_maps()
    assert 'map_data6' not in maci_data.get_child_maps()

    # Test Maps Empty
    assert maci_data.get_parent_maps() ==  {}
    assert maci_data.get_parent_map_chains() ==  {}
    assert maci_data.get_child_maps() ==  {}

    # Test UnMapping an Attr that Exists, but is not Mapped
    with pytest.raises(maci.error.GeneralError):
        maci_data.unmap_attr('unmapped_attr')


# 8. MaciDataObj - LOCK: Test general locking protection and indirect unlock
def test8_maciobj_methods_lock():
    # Build Data
    maci_data = maci.build()
    maci_data.lock_data = 'data'

    # Check if not in List, Setup Attr
    assert 'lock_data' not in maci_data.get_locked_list()
    maci_data.lock_attr('lock_data')

    # Test Attr is Locked and Matched Source List
    assert list(maci_data._MaciDataObjConstructor__assignment_locked_attribs) == maci_data.get_locked_list() == ['lock_data']
    assert 'lock_data' in maci_data.get_locked_list()

    # Test - Re-Assign: Lock block from exception, test data still same
    with pytest.raises(maci.error.MaciError):
        maci_data.lock_data = None
    assert maci_data.lock_data == 'data'

    # Test: You cannot lock attr twice or use a different lock

    # Re-lock
    with pytest.raises(maci.error.MaciError):
        maci_data.lock_attr('lock_data')

    # Use other lock
    with pytest.raises(maci.error.MaciError):
        maci_data.hard_lock_attr('lock_data')

    # Test: Removed from Lock list via Deletion
    del maci_data.lock_data
    assert 'lock_data' not in maci_data.get_locked_list()


# 9. MaciDataObj - UNLOCK: Test general unlocking functionality and protection
def test9_maciobj_methods_unlock():
    # Build Data
    maci_data = maci.build()
    maci_data.lock_data = 'data'

    # Setup Attr
    maci_data.lock_attr('lock_data')
    assert 'lock_data' in maci_data.get_locked_list()
    
    # Unlock it
    maci_data.unlock_attr('lock_data')

    # Test Attr is Unlocked and Matched Source List
    assert 'lock_data' not in maci_data.get_locked_list()
    assert list(maci_data._MaciDataObjConstructor__assignment_locked_attribs) == maci_data.get_locked_list() == []

    # Test: Unlock again block from exception, test that you cannot unlock attr twice
    with pytest.raises(maci.error.MaciError):
        maci_data.unlock_attr('lock_data')


# 10. MaciDataObj - HARD LOCK: Test general hard locking functionality and protection
def test10_maciobj_methods_hard_lock():
    # Build Data
    maci_data = maci.build()
    maci_data.hard_lock_data = 'data'

    # Check if not in List, Setup Attr
    assert 'hard_lock_data' not in maci_data.get_hard_locked_list()
    maci_data.hard_lock_attr('hard_lock_data')

    # Test Attr is Hard Locked and Matched Source List
    assert 'hard_lock_data' in maci_data.get_hard_locked_list()
    assert list(maci_data._MaciDataObjConstructor__assignment_hard_locked_attribs) == maci_data.get_hard_locked_list() == ['hard_lock_data']

    # Test - Re-Assign, Delete: Hard Lock block from exception, test data still same
    
    # Re-Assign Attr
    with pytest.raises(maci.error.MaciError):
        maci_data.hard_lock_data = None
    assert maci_data.hard_lock_data == 'data'
    # Delete Attr
    with pytest.raises(maci.error.MaciError):
        del maci_data.hard_lock_data
    assert maci_data.hard_lock_data == 'data'

    # Test: You cannot lock attr twice or use a different lock

    # Re-lock
    with pytest.raises(maci.error.MaciError):
        maci_data.hard_lock_attr('hard_lock_data')

    # Use other lock
    with pytest.raises(maci.error.MaciError):
        maci_data.lock_attr('hard_lock_data')


# 11. MaciDataObj - Mixed Concepts: Test general locking, hard locking, and mapping in different scenarios
def test11_maciobj_methods_mixed_concepts():
    # Build Data
    maci_data = maci.build()
    maci_data.data_a0 = 'data_a'
    maci_data.data_a1 = None
    maci_data.data_b0 = 'data_b'
    maci_data.data_b1 = None

    ### Map & Lock ###

    # Setup Data and Test
    maci_data.map_attr('data_a1', 'data_a0')
    maci_data.lock_attr('data_a1')

    # Test: Check if in Both Child and Lock Lists
    assert 'data_a1' in maci_data.get_child_maps() and 'data_a1' in maci_data.get_locked_list()
    
    # Test: Check if re-assign parent data works, but child is blocked because locked
    with pytest.raises(maci.error.MaciError):
        maci_data.data_a0 = None
    assert maci_data.data_a0 == None
    assert maci_data.data_a1 == 'data_a'


    ### Map & Hard Lock ###
    
    # Setup Data and Test
    maci_data.map_attr('data_b1', 'data_b0')
    maci_data.hard_lock_attr('data_b1')

    # Test: Check if in Both Child and Lock Lists
    assert 'data_b1' in maci_data.get_child_maps() and 'data_b1' in maci_data.get_hard_locked_list()
    
    # Test: Check if re-assign parent data works, but child is blocked because locked
    with pytest.raises(maci.error.MaciError):
        maci_data.data_b0 = None
    assert maci_data.data_b0 == None
    assert maci_data.data_b1 == 'data_b'

    
    ### LOCK & MAP: Remove Map, Re-Map, Remove Lock, Re-Lock - Check all List Statuses ###

    maci_data.unmap_attr('data_a1')
    assert 'data_a1' not in maci_data.get_child_maps() and 'data_a1' in maci_data.get_locked_list()

    # Re-Map raises exception cause still locked
    with pytest.raises(maci.error.MaciError):
        maci_data.map_attr('data_a1', 'data_a0')
    
    # Unlock and test
    maci_data.unlock_attr('data_a1')
    assert 'data_a1' not in maci_data.get_child_maps() and 'data_a1' not in maci_data.get_locked_list()

    # Re-map and Re-Lock then Unlock and check if still mapped and value changes
    # And, lock, change parent, check value change, unlock, re-assign parent and check if child updates
    maci_data.map_attr('data_a1', 'data_a0')
    maci_data.lock_attr('data_a1')

    maci_data.unlock_attr('data_a1')
    assert 'data_a1' in maci_data.get_child_maps() and 'data_a1' not in maci_data.get_locked_list()

    assert maci_data.data_a0 == None
    assert maci_data.data_a1 == None

    maci_data.lock_attr('data_a1')
    try: maci_data.data_a0 = 'change1'
    except: pass
    
    assert maci_data.data_a0 == 'change1'
    assert maci_data.data_a1 == None

    maci_data.unlock_attr('data_a1')

    maci_data.data_a0 = 'change2'
    assert maci_data.data_a0 == 'change2'
    assert maci_data.data_a1 == 'change2'


    ### HARD LOCK & MAP: Remove Map, Attempt Re-Map - Check all List Statuses ###
    
    maci_data.unmap_attr('data_b1')
    assert 'data_b1' not in maci_data.get_child_maps() and 'data_b1' in maci_data.get_hard_locked_list()

    # Re-Map raises exception cause still hard locked
    with pytest.raises(maci.error.MaciError):
        maci_data.map_attr('data_b1', 'data_b0')


# 12. MaciDataObj - Load Attrs: Test loading attrs into maci object from dict
def test12_maciobj_methods_load_attrs():
    # Build Data
    dict_data = {'k1': 1, 'k2': 2}
    maci_data = maci.build()
    
    # Tests
    maci_data.load_attrs(dict_data)
    assert maci_data.k1 == 1
    assert maci_data.k2 == 2


# 13. MaciDataObj - Get Attrs: Test getting dict representation of attrs from maci object
def test13_maciobj_methods_get_attrs():
    # Build Data
    maci_data = maci.build()
    maci_data.data_str = "data"
    maci_data.data_int = 1

    # Tests
    data_dict = maci_data.get_attrs()
    assert data_dict == {'data_str': 'data', 'data_int': 1}
