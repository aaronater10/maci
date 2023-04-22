# dumpstr - Tests
from src import maci
from os import path, remove
import time
import pytest

test_file_path = './tests/test_files/native/dumpstr_files/'
file_delay_timer = 0.25

################################################################
# TESTS

# 1. Dump Str Data - Testing a basic str dump
def test1_dumpstr_basic_dump_data():
    template_file = 'template_single_line.data'
    template_file = test_file_path + template_file

    # Import Template Data
    file_import = maci.load(template_file)

    # Test Data Type
    str_data = maci.dumpstr(file_import)
    assert isinstance(str_data, str)


# 2. Dump Str: maci - Testing str data and importing values to test formatting stored
def test2_dumpstr_str_formatting_maci():
    template_file = 'template_single_line.data'
    template_file = test_file_path + template_file

    # Import Template Data
    file_import_template = maci.load(template_file)

    # Import Data
    str_data = maci.dumpstr(file_import_template)
    str_import = maci.loadstr(str_data)

    # Test Imported Data
    assert str_import.data_str == "data"
    assert str_import.data_int == 1
    assert str_import.data_float == 1.0
    assert str_import.data_bool == True
    assert str_import.data_list == [1,2,3]
    assert str_import.data_dict == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_tuple == [1,2,3]
    assert str_import.data_set == [1,2,3]
    assert str_import.data_none == {'k1':1, 'k2':2, 'k3':3}
    assert str_import.data_bytes == b'data'


# 3. Dump Str: dict - Testing str data and importing values to test formatting stored
def test3_dumpstr_str_formatting_dict():
    template_file = 'template_single_line.data'
    template_file = test_file_path + template_file

    # Import Template Data
    file_import_template = maci.load(template_file)

    # Import Data
    str_data = maci.dumpstr(file_import_template.data_dict)
    str_import = maci.loadstr(str_data)

    # Test Imported Data
    assert str_import.k1 == 1
    assert str_import.k2 == 2
    assert str_import.k3 == 3


# 4. Dump Str: class - Testing str data and importing values to test formatting stored
def test4_dumpstr_str_formatting_class():
    # Test Data Custom Class
    class TemplateData:
        def __init__(self) -> None:
            self.data_list = [1,2,3]
            self.data_bool = True
            self.data_int = 1
    class_data = TemplateData()

    # Import Data
    str_data = maci.dumpstr(class_data)
    str_import = maci.loadstr(str_data)

    # Test Imported Data
    assert str_import.data_list == [1,2,3]
    assert str_import.data_bool == True
    assert str_import.data_int == 1


# 5. Dump Str: class - Testing Indentation
def test5_dumpstr_str_indentation_class():
    # Test Data Custom Class
    class TemplateData:
        def __init__(self) -> None:
            self.data_list = [1,2,3]
            self.data_bool = True
            self.data_int = 1
    class_data = TemplateData()

    # INDENTATION
    # Store Data
    str_data = maci.dumpstr(class_data, indentation_on=False)

    # Import Data and Set Line Count
    str_import_lines = len(str_data.splitlines())

    # Test Data
    expected_str_lines = 3
    assert str_import_lines == expected_str_lines

    # INDENT LEVEL
    # Store Data
    str_data = maci.dumpstr(class_data, indent_level=5)

    # Import Data
    str_import = maci.loadstr(str_data)

    # Test Data
    assert str_import.data_list == [1,2,3]



# ### PAUSE ###

# # 6. Save File: class - Testing Appending
# def test6_save_file_append_class():
#     filename = '6_save_file_append_class.data'
#     filepath = test_file_path + filename

#     # Test Data Custom Class
#     class TemplateData:
#         def __init__() -> None:
#             self.data_list = [1,2,3]
#             self.data_bool = True
#             self.data_int = 1
#     class_data = TemplateData()

#     # Store Data, then Append to it
#     maci.dumpstr(filepath, class_data, indentation_on=False)
#     maci.dumpstr(filepath, class_data, append=True, indentation_on=False)

#     # Import Data and Set Line Count
#     file_import = maci.loadraw(filepath)
#     file_data = maci.loadstr(file_import, attr_name_dedup=False)
#     file_import_lines = len(file_import.splitlines())

#     # Test Line Count
#     expected_file_lines = 6
#     self.assertEqual(file_import_lines, expected_file_lines)
#     # Test Data
#     self.assertEqual(file_data.data_list, [1,2,3])
#     self.assertEqual(file_data.data_bool, True)
#     self.assertEqual(file_data.data_int, 1)

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass



# ### MaciDataObj ###

# # 1. Dump File - Append: MaciDataObj - Test Appending
# def test1_dump_file_append_maciobj():
#     filename = '1_dump_file_append_maciobj.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = maci.build()
#     file_data.d1 = 'data1'
#     file_data.d2 = 'data2'
#     file_data.d3 = 'data3'

#     # Append Data
#     maci.dumpstr(filepath, file_data)
#     maci.dumpstr(filepath, file_data, append=True)

#     # Test Data
#     file_import = maci.load(filepath, attr_name_dedup=False)

#     assert file_import.d1 == 'data1'
#     assert file_import.d2 == 'data2'
#     assert file_import.d3 == 'data3'

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 2. Dump File - Indentation: MaciDataObj - Test Indenting and Indentation off
# def test2_dump_file_indentation_maciobj():
#     filename = '2_dump_file_indentation_maciobj.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = maci.build()
#     file_data.data_list = [1,2,3]
#     file_data.data_tuple = (1,2,3)
#     file_data.data_set = {1,2,3}

#     # Test Indent Level at 0 and its Data
#     maci.dumpstr(filepath, file_data, indent_level=0)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Test Indent Level at 7 and its Data
#     maci.dumpstr(filepath, file_data, indent_level=7)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Test Indentation OFF
#     maci.dumpstr(filepath, file_data, indentation_on=False)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 3. Dump File - Multi-Line String: MaciDataObj - Test Multi-Line String Format
# def test3_dump_file_multiline_str_maciobj():
#     filename = '3_dump_file_multiline_str_maciobj.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = maci.build()
#     file_data.data_int = 1
#     file_data.data_multi_str1 = "data line 1\ndata line 2\ndata line 3"
#     file_data.data_multi_str2 = "'data line 1\ndata line 2\ndata line 3'"
#     file_data.data_multi_str3 = '"data line 1\ndata line 2\ndata line 3"'
#     file_data.data_multi_str4 = '"""data line 1\ndata line 2\ndata line 3"""'
#     file_data.data_multi_str5 = "'''data line 1\ndata line 2\ndata line 3'''"
#     file_data.data_multi_str6 = "data line 1\ndata line ''' 2\ndata line 3"
#     file_data.data_multi_str7 = 'data line 1\ndata line """ 2\ndata line 3'
#     file_data.data_multi_str8 = 'data line 1\ndata line "" 2\ndata line 3'
#     file_data.data_multi_str9 = "data line 1\ndata line '' 2\ndata line 3"
#     file_data.data_bool = False

#     # Test Multi-Line String Dump and Load
#     maci.dumpstr(filepath, file_data, multi_line_str=True)
#     file_import = maci.load(filepath)

#     assert file_import.data_int == 1
#     assert file_import.data_multi_str1 == "\ndata line 1\ndata line 2\ndata line 3\n"
#     assert file_import.data_multi_str2 == "\n'data line 1\ndata line 2\ndata line 3'\n"
#     assert file_import.data_multi_str3 == '\n"data line 1\ndata line 2\ndata line 3"\n'
#     assert file_import.data_multi_str4 == '\n"""data line 1\ndata line 2\ndata line 3"""\n'
#     assert file_import.data_multi_str5 == "\n'''data line 1\ndata line 2\ndata line 3'''\n"
#     assert file_import.data_multi_str6 == "\ndata line 1\ndata line ''' 2\ndata line 3\n"
#     assert file_import.data_multi_str7 == '\ndata line 1\ndata line """ 2\ndata line 3\n'
#     assert file_import.data_multi_str8 == '\ndata line 1\ndata line "" 2\ndata line 3\n'
#     assert file_import.data_multi_str9 == "\ndata line 1\ndata line '' 2\ndata line 3\n"
#     assert file_import.data_bool == False

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 4. Encoding: MaciDataObj - Test some common encoding types
# def test4_dump_and_load_encodings_maciobj():
#     filename = '4_dump_file_encoding.data'
#     filepath = test_file_path + filename
#     encodings_to_test = {
#         'utf-8',
#         'utf-16',
#         'utf-32',
#         'ascii',
#         'iso-8859-1',
#         'cp1252',
#     }

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)
#     assert not path.exists(filepath)

#     # Build Data
#     file_data = maci.build()
#     file_data.data_dict = {'key': 'data'}

#     # Test Dump and Load with Various Encodings
#     for encoding in encodings_to_test:
#         maci.dumpstr(filepath, file_data, encoding=encoding)
#         time.sleep(file_delay_timer)
#         file_import = maci.load(filepath, encoding=encoding)

#         # Test Section Data from File Load
#         assert 'data' == file_import.data_dict.get('key')

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 5. Dump File - Attr Types: MaciDataObj - Test different attribute types to dump and ensure data is maintained
# def test5_dump_file_attr_types_maciobj():
#     filename = '5_dump_file_attr_types_maciobj.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = maci.build()
#     file_data.norm_data1 = 'data1'
#     file_data._under_data = 'data'
#     file_data.__dunder_data = 'data'
#     file_data.norm_data2 = 'data2'
    
#     # Test: All Private Attrs
#     maci.dumpstr(filepath, file_data, private_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.norm_data1 == 'data1'
#     assert file_import._under_data == 'data'
#     assert file_import.__dunder_data == 'data'
#     assert file_import.norm_data2 == 'data2'

#     # Test: Private Under Attrs
#     maci.dumpstr(filepath, file_data, private_under_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.norm_data1 == 'data1'
#     assert file_import._under_data == 'data'
#     assert file_import.norm_data2 == 'data2'

#     # Test: Private Dunder Attrs
#     maci.dumpstr(filepath, file_data, private_dunder_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.norm_data1 == 'data1'
#     assert file_import.__dunder_data == 'data'
#     assert file_import.norm_data2 == 'data2'

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 6. Dump File - Use Symbol Glyphs: MaciDataObj - Test dump with symbol glyph representation
# def test6_dump_file_use_symbol_glyphs_maciobj():
#     filename = '6_dump_file_use_symbol_glyphs_maciobj.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = maci.build()
#     file_data.norm_data = 'data'
#     file_data.map_data = None
#     file_data.lock_data = 'data'
#     file_data.hard_lock_data = 'data'
#     file_data.map_lock = None
#     file_data.map_hard_lock = None

#     # Setup Attrs
#     file_data.map_attr('map_data', 'norm_data')
#     file_data.lock_attr('lock_data')
#     file_data.hard_lock_attr('hard_lock_data')

#     file_data.map_attr('map_lock', 'lock_data')
#     file_data.lock_attr('map_lock')

#     file_data.map_attr('map_hard_lock', 'hard_lock_data')
#     file_data.hard_lock_attr('map_hard_lock')

#     # Test dump with symbols and test data
#     maci.dumpstr(filepath, file_data, use_symbol_glyphs=True)
#     file_import = maci.load(filepath)

#     assert file_import.norm_data == 'data'
#     assert file_import.map_data == 'data'
#     assert file_import.lock_data == 'data'
#     assert file_import.hard_lock_data == 'data'
#     assert file_import.map_lock == 'data'
#     assert file_import.map_hard_lock == 'data'

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass



# ### DICT ###

# # 1. Dump File - Append: Dict - Test Appending
# def test1_dump_file_append_dict():
#     filename = '1_dump_file_append_dict.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = {
#         'd1': 'data1',
#         'd2': 'data2',
#         'd3': 'data3',
#     }

#     # Append Data
#     maci.dumpstr(filepath, file_data)
#     maci.dumpstr(filepath, file_data, append=True)

#     # Test Data
#     file_import = maci.load(filepath, attr_name_dedup=False)

#     assert file_import.d1 == 'data1'
#     assert file_import.d2 == 'data2'
#     assert file_import.d3 == 'data3'

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 2. Dump File - Indentation: Dict - Test Indenting and Indentation off
# def test2_dump_file_indentation_dict():
#     filename = '2_dump_file_indentation_dict.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = {
#     'data_list': [1,2,3],
#     'data_tuple': (1,2,3),
#     'data_set': {1,2,3},
#     }

#     # Test Indent Level at 0 and its Data
#     maci.dumpstr(filepath, file_data, indent_level=0)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Test Indent Level at 7 and its Data
#     maci.dumpstr(filepath, file_data, indent_level=7)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Test Indentation OFF
#     maci.dumpstr(filepath, file_data, indentation_on=False)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 3. Dump File - Multi-Line String: Dict - Test Multi-Line String Format
# def test3_dump_file_multiline_str_dict():
#     filename = '3_dump_file_multiline_str_dict.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     file_data = {
#     'data_int': 1,
#     'data_multi_str1': "data line 1\ndata line 2\ndata line 3",
#     'data_multi_str2': "'data line 1\ndata line 2\ndata line 3'",
#     'data_multi_str3': '"data line 1\ndata line 2\ndata line 3"',
#     'data_multi_str4': '"""data line 1\ndata line 2\ndata line 3"""',
#     'data_multi_str5': "'''data line 1\ndata line 2\ndata line 3'''",
#     'data_multi_str6': "data line 1\ndata line ''' 2\ndata line 3",
#     'data_multi_str7': 'data line 1\ndata line """ 2\ndata line 3',
#     'data_multi_str8': 'data line 1\ndata line "" 2\ndata line 3',
#     'data_multi_str9': "data line 1\ndata line '' 2\ndata line 3",
#     'data_bool': False,
#     }

#     # Test Multi-Line String Dump and Load
#     maci.dumpstr(filepath, file_data, multi_line_str=True)
#     file_import = maci.load(filepath)

#     assert file_import.data_int == 1
#     assert file_import.data_multi_str1 == "\ndata line 1\ndata line 2\ndata line 3\n"
#     assert file_import.data_multi_str2 == "\n'data line 1\ndata line 2\ndata line 3'\n"
#     assert file_import.data_multi_str3 == '\n"data line 1\ndata line 2\ndata line 3"\n'
#     assert file_import.data_multi_str4 == '\n"""data line 1\ndata line 2\ndata line 3"""\n'
#     assert file_import.data_multi_str5 == "\n'''data line 1\ndata line 2\ndata line 3'''\n"
#     assert file_import.data_multi_str6 == "\ndata line 1\ndata line ''' 2\ndata line 3\n"
#     assert file_import.data_multi_str7 == '\ndata line 1\ndata line """ 2\ndata line 3\n'
#     assert file_import.data_multi_str8 == '\ndata line 1\ndata line "" 2\ndata line 3\n'
#     assert file_import.data_multi_str9 == "\ndata line 1\ndata line '' 2\ndata line 3\n"
#     assert file_import.data_bool == False

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 4. Encoding: Dict - Test some common encoding types
# def test4_dump_and_load_encodings_dict():
#     filename = '4_dump_file_encoding.data'
#     filepath = test_file_path + filename
#     encodings_to_test = {
#         'utf-8',
#         'utf-16',
#         'utf-32',
#         'ascii',
#         'iso-8859-1',
#         'cp1252',
#     }

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)
#     assert not path.exists(filepath)

#     # Build Data
#     file_data = {'key': 'data'}

#     # Test Dump and Load with Various Encodings
#     for encoding in encodings_to_test:
#         maci.dumpstr(filepath, file_data, encoding=encoding)
#         time.sleep(file_delay_timer)
#         file_import = maci.load(filepath, encoding=encoding)

#         # Test Section Data from File Load
#         assert 'data' == file_import.key

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass



# ### Class ###

# # 1. Dump File - Append: Class - Test Appending
# def test1_dump_file_append_class():
#     filename = '1_dump_file_append_class.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     class CustomClass:
#         def __init__():
#             self.d1 = 'data1'
#             self.d2 = 'data2'
#             self.d3 = 'data3'
#     file_data = CustomClass()

#     # Append Data
#     maci.dumpstr(filepath, file_data)
#     maci.dumpstr(filepath, file_data, append=True)

#     # Test Data
#     file_import = maci.load(filepath, attr_name_dedup=False)

#     assert file_import.d1 == 'data1'
#     assert file_import.d2 == 'data2'
#     assert file_import.d3 == 'data3'

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 2. Dump File - Indentation: Class - Test Indenting and Indentation off
# def test2_dump_file_indentation_class():
#     filename = '2_dump_file_indentation_class.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     class CustomClass:
#         def __init__():
#             self.data_list = [1,2,3]
#             self.data_tuple = (1,2,3)
#             self.data_set = {1,2,3}
#     file_data = CustomClass()

#     # Test Indent Level at 0 and its Data
#     maci.dumpstr(filepath, file_data, indent_level=0)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Test Indent Level at 7 and its Data
#     maci.dumpstr(filepath, file_data, indent_level=7)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Test Indentation OFF
#     maci.dumpstr(filepath, file_data, indentation_on=False)
#     file_import = maci.load(filepath)

#     assert file_import.data_list == [1,2,3]
#     assert file_import.data_tuple == (1,2,3)
#     assert file_import.data_set == {1,2,3}

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 3. Dump File - Multi-Line String: Class - Test Multi-Line String Format
# def test3_dump_file_multiline_str_class():
#     filename = '3_dump_file_multiline_str_class.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     class CustomClass:
#         def __init__():
#             self.data_int = 1
#             self.data_multi_str1 = "data line 1\ndata line 2\ndata line 3"
#             self.data_multi_str2 = "'data line 1\ndata line 2\ndata line 3'"
#             self.data_multi_str3 = '"data line 1\ndata line 2\ndata line 3"'
#             self.data_multi_str4 = '"""data line 1\ndata line 2\ndata line 3"""'
#             self.data_multi_str5 = "'''data line 1\ndata line 2\ndata line 3'''"
#             self.data_multi_str6 = "data line 1\ndata line ''' 2\ndata line 3"
#             self.data_multi_str7 = 'data line 1\ndata line """ 2\ndata line 3'
#             self.data_multi_str8 = 'data line 1\ndata line "" 2\ndata line 3'
#             self.data_multi_str9 = "data line 1\ndata line '' 2\ndata line 3"
#             self.data_bool = False
#     file_data = CustomClass()

#     # Test Multi-Line String Dump and Load
#     maci.dumpstr(filepath, file_data, multi_line_str=True)
#     file_import = maci.load(filepath)

#     assert file_import.data_int == 1
#     assert file_import.data_multi_str1 == "\ndata line 1\ndata line 2\ndata line 3\n"
#     assert file_import.data_multi_str2 == "\n'data line 1\ndata line 2\ndata line 3'\n"
#     assert file_import.data_multi_str3 == '\n"data line 1\ndata line 2\ndata line 3"\n'
#     assert file_import.data_multi_str4 == '\n"""data line 1\ndata line 2\ndata line 3"""\n'
#     assert file_import.data_multi_str5 == "\n'''data line 1\ndata line 2\ndata line 3'''\n"
#     assert file_import.data_multi_str6 == "\ndata line 1\ndata line ''' 2\ndata line 3\n"
#     assert file_import.data_multi_str7 == '\ndata line 1\ndata line """ 2\ndata line 3\n'
#     assert file_import.data_multi_str8 == '\ndata line 1\ndata line "" 2\ndata line 3\n'
#     assert file_import.data_multi_str9 == "\ndata line 1\ndata line '' 2\ndata line 3\n"
#     assert file_import.data_bool == False

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 4. Encoding: Class - Test some common encoding types
# def test4_dump_and_load_encodings_class():
#     filename = '4_dump_file_encoding.data'
#     filepath = test_file_path + filename
#     encodings_to_test = {
#         'utf-8',
#         'utf-16',
#         'utf-32',
#         'ascii',
#         'iso-8859-1',
#         'cp1252',
#     }

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)
#     assert not path.exists(filepath)

#     # Build Data
#     class CustomClass:
#         def __init__():
#             self.data_dict = {'key': 'data'}
#     file_data = CustomClass()

#     # Test Dump and Load with Various Encodings
#     for encoding in encodings_to_test:
#         maci.dumpstr(filepath, file_data, encoding=encoding)
#         time.sleep(file_delay_timer)
#         file_import = maci.load(filepath, encoding=encoding)

#         # Test Section Data from File Load
#         assert 'data' == file_import.data_dict.get('key')

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 5. Dump File - Attr Types: Class - Test different attribute types to dump and ensure data is maintained
# def test5_dump_file_attr_types_class():
#     filename = '5_dump_file_attr_types_class.data'
#     filepath = test_file_path + filename

#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Build Data
#     class CustomClass:
#         # Class Attrs
#         cls_norm_data1 = 'data1'
#         _cls_under_data = 'data'
#         __cls_dunder_data = 'data'
#         cls_norm_data2 = 'data2'
#         def __init__():
#             # Init Attrs
#             self.init_norm_data1 = 'data1'
#             self._init_under_data = 'data'
#             self.__init_dunder_data = 'data'
#             self.init_norm_data2 = 'data2'
#     file_data = CustomClass()

#     ### INIT & CLASS ###

#     # Test: All Normal Init & Class Attrs
#     maci.dumpstr(filepath, file_data, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: All Normal/Private Init & Class Attrs
#     maci.dumpstr(filepath, file_data, private_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: All Normal/Under Init & Class Attrs
#     maci.dumpstr(filepath, file_data, private_under_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: All Normal/Dunder Init & Class Attrs
#     maci.dumpstr(filepath, file_data, private_dunder_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal Init & Normal/Private Class Attrs
#     maci.dumpstr(filepath, file_data, private_class_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal Init & Normal/Under Class Attrs
#     maci.dumpstr(filepath, file_data, private_class_under_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal Init & Normal/Dunder Class Attrs
#     maci.dumpstr(filepath, file_data, private_class_dunder_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal Class & Normal/Private Init Attrs
#     maci.dumpstr(filepath, file_data, private_init_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.cls_norm_data2 == 'data2'
    
#     # Test: Normal Class & Normal/Under Init Attrs
#     maci.dumpstr(filepath, file_data, private_init_under_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal Class & Normal/Dunder Init Attrs
#     maci.dumpstr(filepath, file_data, private_init_dunder_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'
#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.cls_norm_data2 == 'data2'


#     ### CLASS ONLY ###

#     # Test: Normal Class Attrs
#     maci.dumpstr(filepath, type(file_data), class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal/Private Class Attrs
#     maci.dumpstr(filepath, type(file_data), private_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal/Private Class Attrs - Alternate Option
#     maci.dumpstr(filepath, type(file_data), private_class_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal/Under Class Attrs
#     maci.dumpstr(filepath, type(file_data), private_under_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal/Under Class Attrs - Alternate Option
#     maci.dumpstr(filepath, type(file_data), private_class_under_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import._cls_under_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal/Dunder Class Attrs
#     maci.dumpstr(filepath, type(file_data), private_dunder_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'

#     # Test: Normal/Dunder Class Attrs - Alternate Option
#     maci.dumpstr(filepath, type(file_data), private_class_dunder_attrs=True, class_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.cls_norm_data1 == 'data1'
#     assert file_import.__cls_dunder_data == 'data'
#     assert file_import.cls_norm_data2 == 'data2'


#     ### INIT ONLY ###

#     # Test: Normal Init Attrs
#     maci.dumpstr(filepath, file_data)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.init_norm_data2 == 'data2'

#     # Test: Normal/Private Init Attrs
#     maci.dumpstr(filepath, file_data, private_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'

#     # Test: Normal/Private Init Attrs - Alternate Option
#     maci.dumpstr(filepath, file_data, private_init_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'

#     # Test: Normal/Under Init Attrs
#     maci.dumpstr(filepath, file_data, private_under_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'

#     # Test: Normal/Under Init Attrs - Alternate Option
#     maci.dumpstr(filepath, file_data, private_init_under_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import._init_under_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'

#     # Test: Normal/Dunder Init Attrs
#     maci.dumpstr(filepath, file_data, private_dunder_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'

#     # Test: Normal/Dunder Init Attrs - Alternate Option
#     maci.dumpstr(filepath, file_data, private_init_dunder_attrs=True)
#     file_import = maci.load(filepath)

#     assert file_import.init_norm_data1 == 'data1'
#     assert file_import.__init_dunder_data == 'data'
#     assert file_import.init_norm_data2 == 'data2'

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass
