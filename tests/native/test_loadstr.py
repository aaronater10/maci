# loadstr - Tests
from src import maci
from os import path
import pytest

test_file_path = './tests/test_files/native/loadstr_files/'

################################################################
# Tests

# 1. Empty Str Import - Importing an Empty File as String
def test1_loadstr_empty_str_import():
    filename = '1_empty.data'
    filepath = test_file_path + filename
    
    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)
    
    # Test File is Empty and Data
    assert path.getsize(filepath) == 0, f"File Not Empty: {filename}"
    assert str_import == None, f"Not None {filename}"


# 2. Single Line Import - Importing Singles Lines of All Primitive Data Types
def test2_loadstr_single_line_import():
    filename = '2_single_line.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes
    assert str_import.data_str == "data"
    assert str_import.data_int == 1
    assert str_import.data_float == 1.0
    assert str_import.data_bool == True
    assert str_import.data_list == [1,2,3]
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}
    assert str_import.data_none == None
    assert str_import.data_bytes == b'data'


# 3. Multi Line Import - Importing Multi Line of All Accepted Data Types
def test3_loadstr_multi_line_import():
    filename = '3_multi_line.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes
    assert str_import.data_list == [1,2,3]
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}


# 4. Multi-Single Line Import - Importing Multi and Single Lines Together
def test4_loadstr_multi_single_line_import():
    filename = '4_multi-single_line.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types
    assert str_import.data_bool == True
    assert str_import.data_list == [1,2,3]
    assert str_import.data_str == "data"
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_none == None
    assert str_import.data_bytes == b'data'
    assert str_import.data_set == {1,2,3}


# 5. Multi-Single Comments Import - Importing Multi and Single Lines with Comments
def test5_loadstr_multi_single_comments_import():
    filename = '5_multi-single_comments.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types
    assert str_import.data_bool == True
    assert str_import.data_list == [1,2,3]
    assert str_import.data_str == "data"
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_none == None
    assert str_import.data_bytes == b'data'
    assert str_import.data_set == {1,2,3}


# 6. Nested Data Import - Importing Nested Data
def test6_loadstr_nested_data_import():
    filename = '6_nested.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types
    assert isinstance(str_import.data_list, list)
    assert str_import.data_list[0] == [1,2,3]
    assert str_import.data_list[1] == [1, 2, 3, 4, 5]
    assert str_import.data_list[2] == {'k1': 1, 'k2': 2, 'k3': 3}
    assert str_import.data_list[3] == (1, 2, 3)
    assert str_import.data_list[4] == {1, 2, 3}
    assert str_import.data_list[5] == [1, 2, 3]


# 7. White Space Import - Importing Data with White Space in Between
def test7_loadstr_white_space_import():
    filename = '7_white_space.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes
    assert str_import.data_list == [1,2,3]
    assert str_import.data_str == "data"
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_none == None
    assert str_import.data_bytes == b'data'
    assert str_import.data_float == 1.0
    assert str_import.data_set == {1,2,3}
    assert str_import.data_bool == True


# 8. All Multi-Single Line Types Import - Importing All Multi-Single Line Types Together
def test8_loadstr_all_multi_single_types_import():
    filename = '8_all_multi-single_types.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types

    # Multi
    assert str_import.data_list_m == [1,2,3]
    assert str_import.data_dict_m == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple_m == (1,2,3)
    assert str_import.data_set_m == {1,2,3}
    # Single
    assert str_import.data_str == "data"
    assert str_import.data_int == 1
    assert str_import.data_float == 1.0
    assert str_import.data_bool == True
    assert str_import.data_list == [1,2,3]
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}
    assert str_import.data_none == None
    assert str_import.data_bytes == b'data'


# 9. Big Data Import - Importing 100K+ Values of Data with Single Lines
def test9_loadstr_big_data_import():
    filename = '9_big_data_with_singles.data'
    filepath = test_file_path + filename
    big_data_len = 100_000

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types
    assert len(str_import.data_single) == big_data_len
    assert str_import.data_float == 1.0
    assert str_import.data_bool == True
    assert len(str_import.data_multi) == big_data_len
    assert str_import.data_none == None
    assert str_import.data_bytes == b'data'


# 10. Misc Behavior Import - Importing Misc, Odd, or Unique Data Inputs
def test10_loadstr_misc_data_import():
    filename = '10_misc.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types
    assert str_import.data_single_tuple_1 == (1,)
    assert str_import.data_single_tuple_2 == (1,)
    assert str_import.data_tuple_int_1 == 1
    assert str_import.data_tuple_int_2 == 1
    assert str_import.data_str_1 == "data with internal spaces"
    assert str_import.data_str_2 == " data with internal and end spaces "
    assert str_import.data_list == [1,2,3]
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}
    assert str_import.data_token1 == ['normal value', "var = 'value'", 'normal value']
    assert str_import.data_end_token1 == ['normal value', "var = 'value'", 'normal value']


# 11. Single-Line Attr Dedup OFF - Turning OFF Attribute Dedup Feature Test
def test11_loadstr_single_attr_dedup_off():
    filename = '11_attr_dedup_off_single.data'
    filepath = test_file_path + filename

    # Test Turn OFF Attr Dedup Protection
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data, attr_name_dedup=False)

    # Test Attributes and Types - Confirm data and it's type was in fact changed inside string
    assert (str_import.data_dict == "changed data") and (isinstance(str_import.data_dict, str))


# 12. Multi-Line Attr Dedup OFF - Turning OFF Attribute Dedup Feature Test
def test12_loadstr_multi_attr_dedup_off():
    filename = '12_attr_dedup_off_multi.data'
    filepath = test_file_path + filename

    # Test Turn OFF Attr Dedup Protection
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data, attr_name_dedup=False)

    # Test Attributes and Types - Confirm data and it's type was in fact changed inside string
    assert (str_import.data_list == "changed data") and (isinstance(str_import.data_list, str))


# 13. Single-Line Attr Lock - Attribute Locked and Cannot Re-Assign
def test13_loadstr_single_attr_lock():
    filename = '13_attr_lock_single.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes - Confirm attr values not changed and match expected
    change_value = 'changed_value'

    with pytest.raises(maci.error.MaciError): str_import.data_str = change_value
    assert str_import.data_str == "data"

    with pytest.raises(maci.error.MaciError): str_import.data_int = change_value
    assert str_import.data_int == 1

    with pytest.raises(maci.error.MaciError): str_import.data_float = change_value
    assert str_import.data_float == 1.0

    with pytest.raises(maci.error.MaciError): str_import.data_bool = change_value
    assert str_import.data_bool == True

    with pytest.raises(maci.error.MaciError): str_import.data_list = change_value
    assert str_import.data_list == [1,2,3]

    with pytest.raises(maci.error.MaciError): str_import.data_dict = change_value
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}

    with pytest.raises(maci.error.MaciError): str_import.data_tuple = change_value
    assert str_import.data_tuple == (1,2,3)

    with pytest.raises(maci.error.MaciError): str_import.data_set = change_value
    assert str_import.data_set == {1,2,3}

    with pytest.raises(maci.error.MaciError): str_import.data_none = change_value
    assert str_import.data_none == None

    with pytest.raises(maci.error.MaciError): str_import.data_bytes = change_value
    assert str_import.data_bytes == b'data'


# 14. Single-Line Attr Lock - Attribute Locked and Cannot Re-Assign
def test14_loadstr_multi_attr_lock():
    filename = '14_attr_lock_multi.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes - Confirm attr values not changed and match expected
    change_value = 'changed_value'

    with pytest.raises(maci.error.MaciError): str_import.data_list = change_value
    assert str_import.data_list == [1,2,3]

    with pytest.raises(maci.error.MaciError): str_import.data_dict = change_value
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}

    with pytest.raises(maci.error.MaciError): str_import.data_tuple = change_value
    assert str_import.data_tuple == (1,2,3)

    with pytest.raises(maci.error.MaciError): str_import.data_set = change_value
    assert str_import.data_set == {1,2,3}


# 15. Mixed Attr/Regular Imports - Confirm Importing Attribute Locked and Regular Values in One String
def test15_loadstr_attr_lock_mixed_imports():
    filename = '15_attr_lock_mixed_imports.data'
    filepath = test_file_path + filename

    # Test String Data Load
    str_data = maci.loadraw(filepath)
    assert maci.loadstr(str_data), "Could not load string data. Could be empty or bad syntax"


# 16. Attr Referencing - Reference Pre-Defined Attr's Value and Confirm Assigned
def test16_loadstr_attr_ref_single_multi():
    filename = '16_attr_ref_single-multi.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes
    assert str_import.data_list_multi == 1
    assert str_import.data_float == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_bool == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_set == (1,2,3)


# 17. Attr Referencing Lock - Reference Pre-Defined Attr's Value, Confirm Assigned, and Locked
def test17_loadstr_attr_ref_lock_single_multi():
    filename = '17_attr_ref_lock_single-multi.data'
    filepath = test_file_path + filename

    # Load String Data
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types - Locked Values Check, then Test Re-Assignment
    change_value = 'changed_value'
    
    assert str_import.data_list_multi, 1
    with pytest.raises(maci.error.MaciError): str_import.data_list_multi = change_value

    assert str_import.data_float, {'k1':1, 'k2':2, 'k3':3}
    with pytest.raises(maci.error.MaciError): str_import.data_float = change_value

    assert str_import.data_bool, {'k1':1, 'k2':2, 'k3':3}
    with pytest.raises(maci.error.MaciError): str_import.data_bool = change_value

    assert str_import.data_set, (1,2,3)
    with pytest.raises(maci.error.MaciError): str_import.data_set = change_value


# 18. Ignore Glyph in Value Str Check - Import Single Line Value String Containing a Glyph
def test18_loadstr_ignore_glyph_in_value_str():
    filename = '18_glyph_in_value.data'
    filepath = test_file_path + filename

    # String Import
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes: Symbols
    assert str_import.data_str1 == "data with = glyph"
    assert str_import.data_str2 == "data with == glyph"
    assert str_import.data_str3 == "data with $= glyph"
    assert str_import.data_str4 == "data with $$= glyph"
    assert str_import.data_str5 == "data with $== glyph"
    assert str_import.data_str6 == "data with $$== glyph"

    # Test Attributes: Letters
    assert str_import.data_let1 == "data with +m= glyph"
    assert str_import.data_let2 == "data with +l= glyph"
    assert str_import.data_let3 == "data with +h= glyph"
    assert str_import.data_let4 == "data with +ml= glyph"
    assert str_import.data_let5 == "data with +mh= glyph"
    assert str_import.data_let6 == "data with +lm= glyph"
    assert str_import.data_let7 == "data with +hm= glyph"


# 19. Check if Error Raised on Value Empty - Import Single Line Value with Empty Value
def test19_loadstr_raise_on_value_empty():
    filename_no_spaces = '19_raise_on_value_empty_no_spaces.data'
    filename_spaces = '19_raise_on_value_empty_spaces.data'

    # String Import: No Spaces
    filepath = test_file_path + filename_no_spaces
    with pytest.raises(maci.error.LoadStr):
        str_data = maci.loadraw(filepath)
        maci.loadstr(str_data)
    
    # String Import: Value Empty with Spaces
    filepath = test_file_path + filename_spaces
    with pytest.raises(maci.error.LoadStr):
        str_data = maci.loadraw(filepath)
        maci.loadstr(str_data)


# 20. Check Pythonic Assignment Syntax - Import Values and Glyphs with varying spaced or connected assignments
def test20_loadstr_python_assignment_syntax():
    filename = '20_python_assignment_syntax.data'

    # String Import
    filepath = test_file_path + filename
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types

    # Single
    assert str_import.data_str == "data"
    assert str_import.data_int == 1
    assert str_import.data_float == 1.0
    assert str_import.data_bool == True
    assert str_import.data_list == [1,2,3]
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}
    assert str_import.data_none == None
    assert str_import.data_bytes == b'data'
    # Multi
    assert str_import.data_list_multi == [1,2,3]
    assert str_import.data_dict_multi == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple_multi == (1,2,3)
    assert str_import.data_set_multi == {1,2,3}
    assert str_import.data_str_multi == "\ndata1\n data2\n  data3\ndata4\n"
    
    ### Glyph Types ###

    # Symbols
    assert str_import.s1 == 1
    assert str_import.s2 == 1
    assert str_import.s3 == 1
    assert str_import.s4 == 1
    assert str_import.s5 == 1
    assert str_import.s6 == 1
    # Letters: lower
    assert str_import.l1 == 1
    assert str_import.l2 == 1
    assert str_import.l3_1 == 1
    assert str_import.l3_2 == 1
    assert str_import.l4 == 1
    assert str_import.l5_1 == 1
    assert str_import.l5_2 == 1
    # Letters: UPPER
    assert str_import.L1 == 1
    assert str_import.L2 == 1
    assert str_import.L3_1 == 1
    assert str_import.L3_2 == 1
    assert str_import.L4 == 1
    assert str_import.L5_1 == 1
    assert str_import.L5_2 == 1


# 21. Ensure Supported Glyph Syntax is Loadable - Import Glyphs with varying types and data
def test21_loadstr_glyph_assignment_syntax():
    filename = '21_glyph_assignment_syntax.data'

    # String Import
    filepath = test_file_path + filename
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes and Types

    # Single: lower
    assert str_import.d1 == "data"
    assert str_import.d2 == "data"
    assert str_import.d3_1 == "data"
    assert str_import.d3_2 == "data"
    assert str_import.d4_1 == "data"
    assert str_import.d4_2 == "data"
    assert str_import.d5 == [1,2,3]
    assert str_import.d6 == {'k1':1, 'k2':2, 'k3':3}
    # Single: UPPER
    assert str_import.d7 == {1,2,3}
    assert str_import.d8 == {1,2,3}
    assert str_import.d9_1 == {1,2,3}
    assert str_import.d9_2 == {1,2,3}
    assert str_import.d10_1 == {1,2,3}
    assert str_import.d10_2 == {1,2,3}
    assert str_import.d11 == (1,2,3)
    assert str_import.d12 == b'data'
    # Mixed: UPPER and lower
    assert str_import.d13 == "data"
    assert str_import.d14 == "data"
    assert str_import.d15 == "data"
    assert str_import.d16 == "data"
    assert str_import.d17 == "data"
    assert str_import.d18 == "data"
    assert str_import.d19 == "data"
    assert str_import.d20 == "data"
    assert str_import.d21 == "data"

    # Multi
    assert str_import.d1_multi == [1,2,3]
    assert str_import.d2_multi == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.d3_multi == (1,2,3)
    assert str_import.d4_multi == {1,2,3}


# 22. Ensure DateTime Syntax is Loadable - Import DateTime data with varying formats
def test22_loadstr_date_time_syntax():
    from datetime import datetime, date, time
    filename = '22_date_time_syntax.data'

    # String Import
    filepath = test_file_path + filename
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstr(str_data)

    # Test Attributes
    assert isinstance(str_import.custom_date_time, datetime) and str(str_import.custom_date_time) == "2023-03-13 22:06:00"
    assert isinstance(str_import.custom_date_timem, datetime) and str(str_import.custom_date_timem) == "2023-03-13 22:06:00.500000"
    assert isinstance(str_import.custom_date, date) and str(str_import.custom_date) == "2023-03-13"
    assert isinstance(str_import.custom_time, time) and str(str_import.custom_time) == "22:06:00"
    assert isinstance(str_import.custom_timem, time) and str(str_import.custom_timem) == "22:06:00.500000"
    assert isinstance(str_import.custom_time_date, datetime) and str(str_import.custom_time_date) == "2023-03-13 22:06:00"
    assert isinstance(str_import.custom_timem_date, datetime) and str(str_import.custom_timem_date) == "2023-03-13 22:06:00.500000"
    assert isinstance(str_import.date_time_iso8601, datetime) and str(str_import.date_time_iso8601) == "2023-03-13 22:06:00"
