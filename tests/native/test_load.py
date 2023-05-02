# load - Tests
from src import maci
from os import path
import unittest
import pytest

test_file_path = './tests/test_files/native/load_files/'

################################################################
'''
NOTICE:
- Any new tests must not use the unittest class and instead use the pytest framework if needed.
- Add new tests below the "TestLoad" class
- Old tests are still being used/kept to reference consistent functionality
- Ensure to still continue to number tests in order
'''
################################################################


################################################################
# Tests

class TestLoad(unittest.TestCase):

    # 1. Basic File Import - Importing an Empty File
    def test1_basic_file_import(self):
        filename = '1_empty.data'
        filepath = test_file_path + filename
        assert path.getsize(filepath) == 0, f"File Not Empty: {filename}"
        assert (maci.load(filepath)) == None, f"Not None {filename}"

    # 2. Single Line Import - Importing Singles Lines of All Accepted Data Types
    def test2_single_line_import(self):
        filename = '2_single_line.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
        assert (file_import.data_int == 1) and (isinstance(file_import.data_int, int))
        assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
        assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
        assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
        assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
        assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
        assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
        assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
        assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))

    # 3. Multi Line Import - Importing Multi Line of All Accepted Data Types
    def test3_multi_line_import(self):
        filename = '3_multi_line.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
        assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
        assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
        assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))

    # 4. Multi-Single Line Import - Importing Multi and Single Lines Together
    def test4_multi_single_line_import(self):
        filename = '4_multi-single_line.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
        assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
        assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
        assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
        assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
        assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))
        assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))

    # 5. Multi-Single Comments Import - Importing Multi and Single Lines with Comments
    def test5_multi_single_comments_import(self):
        filename = '5_multi-single_comments.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
        assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
        assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
        assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
        assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
        assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))
        assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))

    # 6. Nested Data Import - Importing Nested Data
    def test6_nested_data_import(self):
        filename = '6_nested.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert isinstance(file_import.data_list, list)
        assert (file_import.data_list[0] == [1,2,3]) and (isinstance(file_import.data_list[0], list))
        assert (file_import.data_list[1] == [1, 2, 3, 4, 5]) and (isinstance(file_import.data_list[1], list))
        assert (file_import.data_list[2] == {'k1': 1, 'k2': 2, 'k3': 3}) and (isinstance(file_import.data_list[2], dict))
        assert (file_import.data_list[3] == (1, 2, 3)) and (isinstance(file_import.data_list[3], tuple))
        assert (file_import.data_list[4] == {1, 2, 3}) and (isinstance(file_import.data_list[4], set))
        assert (file_import.data_list[5] == [1, 2, 3]) and (isinstance(file_import.data_list[5], list))

    # 7. White Space Import - Importing Data with White Space in Between
    def test7_white_space_import(self):
        filename = '7_white_space.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
        assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
        assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
        assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
        assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))
        assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
        assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
        assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))

    # 8. All Multi-Single Line Types Import - Importing All Multi-Single Line Types Together
    def test8_all_multi_single_types_import(self):
        filename = '8_all_multi-single_types.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types

        # Multi
        assert (file_import.data_list_m == [1,2,3]) and (isinstance(file_import.data_list_m, list))
        assert (file_import.data_dict_m == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict_m, dict))
        assert (file_import.data_tuple_m == (1,2,3)) and (isinstance(file_import.data_tuple_m, tuple))
        assert (file_import.data_set_m == {1,2,3}) and (isinstance(file_import.data_set_m, set))
        # Single
        assert (file_import.data_str == "data") and (isinstance(file_import.data_str, str))
        assert (file_import.data_int == 1) and (isinstance(file_import.data_int, int))
        assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
        assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
        assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
        assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
        assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
        assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
        assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
        assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))

    # 9. Big Data Import - Importing 100K+ Values of Data with Single Lines
    def test9_big_data_import(self):
        filename = '9_big_data_with_singles.data'
        filepath = test_file_path + filename
        big_data_len = 100_000

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (len(file_import.data_single) == big_data_len) and (isinstance(file_import.data_single, list))
        assert (file_import.data_float == 1.0) and (isinstance(file_import.data_float, float))
        assert (file_import.data_bool == True) and (isinstance(file_import.data_bool, bool))
        assert (len(file_import.data_multi) == big_data_len) and (isinstance(file_import.data_multi, dict))
        assert (file_import.data_none == None) and (isinstance(file_import.data_none, type(None)))
        assert (file_import.data_bytes == b'data') and (isinstance(file_import.data_bytes, bytes))

    # 10. Misc Behavior Import - Importing Misc, Odd, or Unique Data Inputs
    def test10_misc_data_import(self):
        filename = '10_misc.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (file_import.data_single_tuple_1 == (1,)) and (isinstance(file_import.data_single_tuple_1, tuple))
        assert (file_import.data_single_tuple_2 == (1,)) and (isinstance(file_import.data_single_tuple_2, tuple))
        assert (file_import.data_tuple_int_1 == 1) and (isinstance(file_import.data_tuple_int_1, int))
        assert (file_import.data_tuple_int_2 == 1) and (isinstance(file_import.data_tuple_int_2, int))
        assert (file_import.data_str_1 == "data with internal spaces") and (isinstance(file_import.data_str_1, str))
        assert (file_import.data_str_2 == " data with internal and end spaces ") and (isinstance(file_import.data_str_2, str))
        assert (file_import.data_list == [1,2,3]) and (isinstance(file_import.data_list, list))
        assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_dict, dict))
        assert (file_import.data_tuple == (1,2,3)) and (isinstance(file_import.data_tuple, tuple))
        assert (file_import.data_set == {1,2,3}) and (isinstance(file_import.data_set, set))
        assert (file_import.data_token1 == ['normal value', "var = 'value'", 'normal value']) and (isinstance(file_import.data_token1, list))
        assert (file_import.data_end_token1 == ['normal value', "var = 'value'", 'normal value']) and (isinstance(file_import.data_end_token1, list))

    # 11. Single-Line Attr Dedup OFF - Turning OFF Attribute Dedup Feature Test
    def test11_single_attr_dedup_off(self):
        filename = '11_attr_dedup_off_single.data'
        filepath = test_file_path + filename

        # Test Turn OFF Attr Dedup Protection
        file_import = maci.load(filepath, attr_name_dedup=False)

        # Test Attributes and Types - Confirm data and it's type was in fact changed inside file
        assert (file_import.data_dict == "changed data") and (isinstance(file_import.data_dict, str))

    # 12. Multi-Line Attr Dedup OFF - Turning OFF Attribute Dedup Feature Test
    def test12_multi_attr_dedup_off(self):
        filename = '12_attr_dedup_off_multi.data'
        filepath = test_file_path + filename

        # Test Turn OFF Attr Dedup Protection
        file_import = maci.load(filepath, attr_name_dedup=False)

        # Test Attributes and Types - Confirm data and it's type was in fact changed inside file
        assert (file_import.data_list == "changed data") and (isinstance(file_import.data_list, str))

    # 13. Single-Line Attr Lock - Attribute Locked and Cannot Re-Assign
    def test13_single_attr_lock(self):
        filename = '13_attr_lock_single.data'
        filepath = test_file_path + filename

        # Test File Import
        file_import = maci.load(filepath)

        # Test Attributes and Types - Confirm attr values not changed and match expected
        change_value = 'changed_value'

        with self.assertRaises(maci.error.MaciError): file_import.data_str = change_value
        self.assertEqual(file_import.data_str, "data")

        with self.assertRaises(maci.error.MaciError): file_import.data_int = change_value
        self.assertEqual(file_import.data_int, 1)

        with self.assertRaises(maci.error.MaciError): file_import.data_float = change_value
        self.assertEqual(file_import.data_float, 1.0)

        with self.assertRaises(maci.error.MaciError): file_import.data_bool = change_value
        self.assertEqual(file_import.data_bool, True)

        with self.assertRaises(maci.error.MaciError): file_import.data_list = change_value
        self.assertEqual(file_import.data_list, [1,2,3])

        with self.assertRaises(maci.error.MaciError): file_import.data_dict = change_value
        self.assertEqual(file_import.data_dict, {'k1':1, 'k2':2, 'k3':3})

        with self.assertRaises(maci.error.MaciError): file_import.data_tuple = change_value
        self.assertEqual(file_import.data_tuple, (1,2,3))

        with self.assertRaises(maci.error.MaciError): file_import.data_set = change_value
        self.assertEqual(file_import.data_set, {1,2,3})

        with self.assertRaises(maci.error.MaciError): file_import.data_none = change_value
        self.assertEqual(file_import.data_none, None)

        with self.assertRaises(maci.error.MaciError): file_import.data_bytes = change_value
        self.assertEqual(file_import.data_bytes, b'data')

    # 14. Single-Line Attr Lock - Attribute Locked and Cannot Re-Assign
    def test14_multi_attr_lock(self):
        filename = '14_attr_lock_multi.data'
        filepath = test_file_path + filename

        # Test File Import
        file_import = maci.load(filepath)

        # Test Attributes and Types - Confirm attr values not changed and match expected
        change_value = 'changed_value'

        with self.assertRaises(maci.error.MaciError): file_import.data_list = change_value
        self.assertEqual(file_import.data_list, [1,2,3])

        with self.assertRaises(maci.error.MaciError): file_import.data_dict = change_value
        self.assertEqual(file_import.data_dict, {'k1':1, 'k2':2, 'k3':3})

        with self.assertRaises(maci.error.MaciError): file_import.data_tuple = change_value
        self.assertEqual(file_import.data_tuple, (1,2,3))

        with self.assertRaises(maci.error.MaciError): file_import.data_set = change_value
        self.assertEqual(file_import.data_set, {1,2,3})
    
    # 15. Mixed Attr/Regular Imports - Confirm Importing Attribute Locked and Regular Values in One File
    def test15_attr_lock_mixed_imports(self):
        filename = '15_attr_lock_mixed_imports.data'
        filepath = test_file_path + filename

        # Test File Import
        maci.load(filepath)    

    # 16. Attr Referencing - Reference Pre-Defined Attr's Value and Confirm Assigned
    def test16_attr_ref_single_multi(self):
        filename = '16_attr_ref_single-multi.data'
        filepath = test_file_path + filename

        # Test File Import
        file_import = maci.load(filepath)

        # Test Attributes and Types
        self.assertEqual(file_import.data_list_multi, 1)
        self.assertEqual(file_import.data_float, {'k1':1, 'k2':2, 'k3':3})
        self.assertEqual(file_import.data_bool, {'k1':1, 'k2':2, 'k3':3})
        self.assertEqual(file_import.data_set, (1,2,3))
    
    # 17. Attr Referencing Lock - Reference Pre-Defined Attr's Value, Confirm Assigned, and Locked
    def test17_attr_ref_lock_single_multi(self):
        filename = '17_attr_ref_lock_single-multi.data'
        filepath = test_file_path + filename

        # Test File Import
        file_import = maci.load(filepath)

        # Test Attributes and Types - Locked Values Check, then Test Re-Assignment
        change_value = 'changed_value'
        
        self.assertEqual(file_import.data_list_multi, 1)
        with self.assertRaises(maci.error.MaciError): file_import.data_list_multi = change_value

        self.assertEqual(file_import.data_float, {'k1':1, 'k2':2, 'k3':3})
        with self.assertRaises(maci.error.MaciError): file_import.data_float = change_value

        self.assertEqual(file_import.data_bool, {'k1':1, 'k2':2, 'k3':3})
        with self.assertRaises(maci.error.MaciError): file_import.data_bool = change_value

        self.assertEqual(file_import.data_set, (1,2,3))
        with self.assertRaises(maci.error.MaciError): file_import.data_set = change_value

### END OF OLD TESTS ###
################################################################
# SEE AT TOP ABOVE FOR THIS
################################################################
### NEW TESTS BELOW ###

# 18. Ignore Glyph in Value Str Check - Import Single Line Value String Containing a Glyph
def test18_ignore_glyph_in_value_str():
    filename = '18_glyph_in_value.data'
    filepath = test_file_path + filename

    # File Import
    file_import = maci.load(filepath)

    # Test Attributes: Symbols
    assert (file_import.data_str1 == "data with = glyph")
    assert (file_import.data_str2 == "data with == glyph")
    assert (file_import.data_str3 == "data with $= glyph")
    assert (file_import.data_str4 == "data with $$= glyph")
    assert (file_import.data_str5 == "data with $== glyph")
    assert (file_import.data_str6 == "data with $$== glyph")

    # Test Attributes: Letters
    assert (file_import.data_let1 == "data with +m= glyph")
    assert (file_import.data_let2 == "data with +l= glyph")
    assert (file_import.data_let3 == "data with +h= glyph")
    assert (file_import.data_let4 == "data with +ml= glyph")
    assert (file_import.data_let5 == "data with +mh= glyph")
    assert (file_import.data_let6 == "data with +lm= glyph")
    assert (file_import.data_let7 == "data with +hm= glyph")


# 19. Check if Error Raised on Value Empty - Import Single Line Value with Empty Value
def test19_raise_on_value_empty():
    filename_no_spaces = '19_raise_on_value_empty_no_spaces.data'
    filename_spaces = '19_raise_on_value_empty_spaces.data'

    # File Import: No Spaces
    filepath = test_file_path + filename_no_spaces
    with pytest.raises(maci.error.Load):
        maci.load(filepath)
    
    # File Import: Value Empty with Spaces
    filepath = test_file_path + filename_spaces
    with pytest.raises(maci.error.Load):
        maci.load(filepath)


# 20. Check Pythonic Assignment Syntax - Import Values and Glyphs with varying spaced or connected assignments
def test20_python_assignment_syntax():
    filename = '20_python_assignment_syntax.data'

    # File Import
    filepath = test_file_path + filename
    file_import = maci.load(filepath)

    # Test Attributes and Types

    # Single
    assert file_import.data_str == "data"
    assert file_import.data_int == 1
    assert file_import.data_float == 1.0
    assert file_import.data_bool == True
    assert file_import.data_list == [1,2,3]
    assert file_import.data_dict == {'k1':1, 'k2':2, 'k3':3}
    assert file_import.data_tuple == (1,2,3)
    assert file_import.data_set == {1,2,3}
    assert file_import.data_none == None
    assert file_import.data_bytes == b'data'
    # Multi
    assert file_import.data_list_multi == [1,2,3]
    assert file_import.data_dict_multi == {'k1':1, 'k2':2, 'k3':3}
    assert file_import.data_tuple_multi == (1,2,3)
    assert file_import.data_set_multi == {1,2,3}
    assert file_import.data_str_multi == "\ndata1\n data2\n  data3\ndata4\n"
    
    ### Glyph Types ###

    # Symbols
    assert file_import.s1 == 1
    assert file_import.s2 == 1
    assert file_import.s3 == 1
    assert file_import.s4 == 1
    assert file_import.s5 == 1
    assert file_import.s6 == 1
    # Letters: lower
    assert file_import.l1 == 1
    assert file_import.l2 == 1
    assert file_import.l3_1 == 1
    assert file_import.l3_2 == 1
    assert file_import.l4 == 1
    assert file_import.l5_1 == 1
    assert file_import.l5_2 == 1
    # Letters: UPPER
    assert file_import.L1 == 1
    assert file_import.L2 == 1
    assert file_import.L3_1 == 1
    assert file_import.L3_2 == 1
    assert file_import.L4 == 1
    assert file_import.L5_1 == 1
    assert file_import.L5_2 == 1


# 21. Ensure Supported Glyph Syntax is Loadable - Import Glyphs with varying types and data
def test21_glyph_assignment_syntax():
    filename = '21_glyph_assignment_syntax.data'

    # File Import
    filepath = test_file_path + filename
    file_import = maci.load(filepath)

    # Test Attributes and Types

    # Single: lower
    assert file_import.d1 == "data"
    assert file_import.d2 == "data"
    assert file_import.d3_1 == "data"
    assert file_import.d3_2 == "data"
    assert file_import.d4_1 == "data"
    assert file_import.d4_2 == "data"
    assert file_import.d5 == [1,2,3]
    assert file_import.d6 == {'k1':1, 'k2':2, 'k3':3}
    # Single: UPPER
    assert file_import.d7 == {1,2,3}
    assert file_import.d8 == {1,2,3}
    assert file_import.d9_1 == {1,2,3}
    assert file_import.d9_2 == {1,2,3}
    assert file_import.d10_1 == {1,2,3}
    assert file_import.d10_2 == {1,2,3}
    assert file_import.d11 == (1,2,3)
    assert file_import.d12 == b'data'
    # Mixed: UPPER and lower
    assert file_import.d13 == "data"
    assert file_import.d14 == "data"
    assert file_import.d15 == "data"
    assert file_import.d16 == "data"
    assert file_import.d17 == "data"
    assert file_import.d18 == "data"
    assert file_import.d19 == "data"
    assert file_import.d20 == "data"
    assert file_import.d21 == "data"

    # Multi
    assert file_import.d1_multi == [1,2,3]
    assert file_import.d2_multi == {'k1':1, 'k2':2, 'k3':3}
    assert file_import.d3_multi == (1,2,3)
    assert file_import.d4_multi == {1,2,3}


# 22. Ensure DateTime Syntax is Loadable - Import DateTime data with varying formats
def test22_date_time_syntax():
    from datetime import datetime, date, time
    filename = '22_date_time_syntax.data'

    # File Import
    filepath = test_file_path + filename
    file_import = maci.load(filepath)

    # Test Attributes
    assert isinstance(file_import.custom_date_time, datetime) and str(file_import.custom_date_time) == "2023-03-13 22:06:00"
    assert isinstance(file_import.custom_date_timem, datetime) and str(file_import.custom_date_timem) == "2023-03-13 22:06:00.500000"
    assert isinstance(file_import.custom_date, date) and str(file_import.custom_date) == "2023-03-13"
    assert isinstance(file_import.custom_time, time) and str(file_import.custom_time) == "22:06:00"
    assert isinstance(file_import.custom_timem, time) and str(file_import.custom_timem) == "22:06:00.500000"
    assert isinstance(file_import.custom_time_date, datetime) and str(file_import.custom_time_date) == "2023-03-13 22:06:00"
    assert isinstance(file_import.custom_timem_date, datetime) and str(file_import.custom_timem_date) == "2023-03-13 22:06:00.500000"
    assert isinstance(file_import.date_time_iso8601, datetime) and str(file_import.date_time_iso8601) == "2023-03-13 22:06:00"


# 23. Check behavior of internal method check - Test with it ON/OFF
def test23_load_internal_method_check_off_on():
    filename = '23_internal_method_check.data'
    filepath = test_file_path + filename

    # OFF: File Import - All Attrs Import
    file_import = maci.load(filepath, attr_name_dedup=False, _ignore_maci_attr_check=True)

    # Test Attrs
    assert file_import.map_attr == [1,2,3]
    assert file_import.lock_attr == [1,2,3]
    assert file_import.data_str == 'data'
    assert file_import.data_int == 1

    # ON: File Import (ON by Default) - Raise Exception
    with pytest.raises(maci.error.Load):
        file_import = maci.load(filepath, attr_name_dedup=False)
