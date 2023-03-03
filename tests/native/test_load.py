# load - Tests
from src import maci
from os import path
import unittest
import pytest

test_file_path = './tests/test_files/native/load_files/'

################################################################
'''
NOTICE:
- Any new tests must not use the unittest class and instead use the pytest framework.
- Add new tests below the "TestLoad" class
- Old tests are still being used/kept to reference consistent functionality
- Ensure to number tests in order
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

        with self.assertRaises(Exception): file_import.data_str = change_value
        self.assertEqual(file_import.data_str, "data")

        with self.assertRaises(Exception): file_import.data_int = change_value
        self.assertEqual(file_import.data_int, 1)

        with self.assertRaises(Exception): file_import.data_float = change_value
        self.assertEqual(file_import.data_float, 1.0)

        with self.assertRaises(Exception): file_import.data_bool = change_value
        self.assertEqual(file_import.data_bool, True)

        with self.assertRaises(Exception): file_import.data_list = change_value
        self.assertEqual(file_import.data_list, [1,2,3])

        with self.assertRaises(Exception): file_import.data_dict = change_value
        self.assertEqual(file_import.data_dict, {'k1':1, 'k2':2, 'k3':3})

        with self.assertRaises(Exception): file_import.data_tuple = change_value
        self.assertEqual(file_import.data_tuple, (1,2,3))

        with self.assertRaises(Exception): file_import.data_set = change_value
        self.assertEqual(file_import.data_set, {1,2,3})

        with self.assertRaises(Exception): file_import.data_none = change_value
        self.assertEqual(file_import.data_none, None)

        with self.assertRaises(Exception): file_import.data_bytes = change_value
        self.assertEqual(file_import.data_bytes, b'data')

    # 14. Single-Line Attr Lock - Attribute Locked and Cannot Re-Assign
    def test14_multi_attr_lock(self):
        filename = '14_attr_lock_multi.data'
        filepath = test_file_path + filename

        # Test File Import
        file_import = maci.load(filepath)

        # Test Attributes and Types - Confirm attr values not changed and match expected
        change_value = 'changed_value'

        with self.assertRaises(Exception): file_import.data_list = change_value
        self.assertEqual(file_import.data_list, [1,2,3])

        with self.assertRaises(Exception): file_import.data_dict = change_value
        self.assertEqual(file_import.data_dict, {'k1':1, 'k2':2, 'k3':3})

        with self.assertRaises(Exception): file_import.data_tuple = change_value
        self.assertEqual(file_import.data_tuple, (1,2,3))

        with self.assertRaises(Exception): file_import.data_set = change_value
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
        with self.assertRaises(Exception): file_import.data_list_multi = change_value

        self.assertEqual(file_import.data_float, {'k1':1, 'k2':2, 'k3':3})
        with self.assertRaises(Exception): file_import.data_float = change_value

        self.assertEqual(file_import.data_bool, {'k1':1, 'k2':2, 'k3':3})
        with self.assertRaises(Exception): file_import.data_bool = change_value

        self.assertEqual(file_import.data_set, (1,2,3))
        with self.assertRaises(Exception): file_import.data_set = change_value

### END OF OLD TESTS ###
################################################################
# SEE AT TOP ABOVE FOR THIS
################################################################
### NEW TESTS BELOW ###

# 18. Ignore Glyph in Value Str Check - Import Single Line Value String Containing a Glyph
    def test18_ignore_glyph_in_value_str(self):
        filename = '18_glyph_in_value.data'
        filepath = test_file_path + filename

        # Test File Import
        assert maci.load(filepath)
        file_import = maci.load(filepath)

        # Test Attributes and Types
        assert (file_import.data_str1 == "data with = glyph")
        assert (file_import.data_str2 == "data with == glyph")
        assert (file_import.data_str3 == "data with $= glyph")
        assert (file_import.data_str4 == "data with $$= glyph")
        assert (file_import.data_str5 == "data with $== glyph")
        assert (file_import.data_str6 == "data with $$== glyph")
