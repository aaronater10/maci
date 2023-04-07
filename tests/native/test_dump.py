# dump - Tests
from src import maci
from os import path, remove
import time
import unittest

test_file_path = './tests/test_files/native/dump_files/'
file_delay_timer = 0.25

################################################################
'''
NOTICE:
- Any new tests must not use the unittest class and instead use the pytest framework if needed.
- Add new tests below the "TestDump" class
- Old tests are still being used/kept to reference consistent functionality
- Ensure to still continue to number tests in order
'''
################################################################


################################################################
# TESTS

class TestDump(unittest.TestCase):

    # 1. Save File - Testing a basic save file
    def test1_basic_save_file(self):
        filename = '1_basic_save_file.data'
        template_file = 'template_single_line.data'
        filepath = test_file_path + filename
        template_file = test_file_path + template_file

        # Import Template Data
        file_import = maci.load(template_file)

        # Remove Any Existing Test File
        try: remove(filepath)
        except: pass
        time.sleep(file_delay_timer)

        # Test Not Exist, Create, Test Exist
        self.assertEqual(path.exists(filepath), False)
        maci.dump(filepath, file_import)
        self.assertEqual(path.exists(filepath), True)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 2. Save File: maci - Testing a save file and importing values to test formatting stored
    def test2_save_file_formatting_maci(self):
        filename = '2_save_file_formatting_maci.data'
        template_file = 'template_single_line.data'
        filepath = test_file_path + filename
        template_file = test_file_path + template_file

        # Import Template Data
        file_import_template = maci.load(template_file)

        # Store Data
        maci.dump(filepath, file_import_template)

        # Test Importing Data
        file_import = maci.load(filepath)

        # Test Imported Data
        self.assertEqual(file_import.data_str, "data")
        self.assertEqual(file_import.data_int, 1)
        self.assertEqual(file_import.data_float, 1.0)
        self.assertEqual(file_import.data_bool, True)
        self.assertEqual(file_import.data_list, [1,2,3])
        self.assertEqual(file_import.data_dict, {'k1':1, 'k2':2, 'k3':3})
        self.assertEqual(file_import.data_tuple, [1,2,3])
        self.assertEqual(file_import.data_set, [1,2,3])
        self.assertEqual(file_import.data_none, {'k1':1, 'k2':2, 'k3':3})
        self.assertEqual(file_import.data_bytes, b'data')

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass
    
    # 3. Save File: dict - Testing a save file and importing values to test formatting stored
    def test3_save_file_formatting_dict(self):
        filename = '3_save_file_formatting_dict.data'
        template_file = 'template_single_line.data'
        filepath = test_file_path + filename
        template_file = test_file_path + template_file

        # Import Template Data
        file_import_template = maci.load(template_file)

        # Store Data
        maci.dump(filepath, file_import_template.data_dict)

        # Test Importing Data
        file_import = maci.load(filepath)

        # Test Imported Data
        self.assertEqual(file_import.k1, 1)
        self.assertEqual(file_import.k2, 2)
        self.assertEqual(file_import.k3, 3)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 4. Save File: class - Testing a save file and importing values to test formatting stored
    def test4_save_file_formatting_class(self):
        filename = '4_save_file_formatting_class.data'
        filepath = test_file_path + filename

        # Test Data Custom Class
        class TemplateData:
            def __init__(self) -> None:
                self.data_list = [1,2,3]
                self.data_bool = True
                self.data_int = 1
        class_data = TemplateData()

        # Store Data
        maci.dump(filepath, class_data)

        # Test Importing Data
        file_import = maci.load(filepath)

        # Test Imported Data
        self.assertEqual(file_import.data_list, [1,2,3])
        self.assertEqual(file_import.data_bool, True)
        self.assertEqual(file_import.data_int, 1)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 5. Save File: class - Testing Indentation
    def test5_save_file_indentation_class(self):
        filename = '5_save_file_indentation_class.data'
        filepath = test_file_path + filename

        # Test Data Custom Class
        class TemplateData:
            def __init__(self) -> None:
                self.data_list = [1,2,3]
                self.data_bool = True
                self.data_int = 1
        class_data = TemplateData()

        # INDENTATION
        # Store Data
        maci.dump(filepath, class_data, indentation_on=False)

        # Import Data and Set Line Count
        file_import = maci.loadraw(filepath)
        file_import_lines = len(file_import.splitlines())

        # Test Data
        expected_file_lines = 3
        self.assertEqual(file_import_lines, expected_file_lines)

        # INDENT LEVEL
        # Store Data
        maci.dump(filepath, class_data, indent_level=5)

        # Import Data
        file_import = maci.load(filepath)

        # Test Data
        self.assertEqual(file_import.data_list, [1,2,3])

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 6. Save File: class - Testing Appending
    def test6_save_file_append_class(self):
        filename = '6_save_file_append_class.data'
        filepath = test_file_path + filename

        # Test Data Custom Class
        class TemplateData:
            def __init__(self) -> None:
                self.data_list = [1,2,3]
                self.data_bool = True
                self.data_int = 1
        class_data = TemplateData()

        # Store Data, then Append to it
        maci.dump(filepath, class_data, indentation_on=False)
        maci.dump(filepath, class_data, append=True, indentation_on=False)

        # Import Data and Set Line Count
        file_import = maci.loadraw(filepath)
        file_data = maci.loadstr(file_import, attr_name_dedup=False)
        file_import_lines = len(file_import.splitlines())

        # Test Line Count
        expected_file_lines = 6
        self.assertEqual(file_import_lines, expected_file_lines)
        # Test Data
        self.assertEqual(file_data.data_list, [1,2,3])
        self.assertEqual(file_data.data_bool, True)
        self.assertEqual(file_data.data_int, 1)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

### END OF OLD TESTS ###
################################################################
# SEE AT TOP ABOVE FOR THIS
################################################################
### NEW TESTS BELOW ###


### MaciDataObj ###

# 1. Dump File - Append: MaciDataObj - Test Appending
def test1_dump_file_append_maciobj():
    filename = '1_dump_file_append_maciobj.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Build Data
    file_data = maci.build()
    file_data.d1 = 'data1'
    file_data.d2 = 'data2'
    file_data.d3 = 'data3'

    # Append Data
    maci.dump(filepath, file_data)
    maci.dump(filepath, file_data, append=True)

    # Test Data
    file_import = maci.load(filepath, attr_name_dedup=False)

    assert file_import.d1 == 'data1'
    assert file_import.d2 == 'data2'
    assert file_import.d3 == 'data3'

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. Dump File - Indentation: MaciDataObj - Test Indenting and Indentation off
def test2_dump_file_indentation_maciobj():
    filename = '2_dump_file_indentation_maciobj.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Build Data
    file_data = maci.build()
    file_data.data_list = [1,2,3]
    file_data.data_tuple = (1,2,3)
    file_data.data_set = {1,2,3}

    # Test Indent Level at 0 and its Data
    maci.dump(filepath, file_data, indent_level=0)
    file_import = maci.load(filepath)

    assert file_import.data_list == [1,2,3]
    assert file_import.data_tuple == (1,2,3)
    assert file_import.data_set == {1,2,3}

    # Test Indent Level at 7 and its Data
    maci.dump(filepath, file_data, indent_level=7)
    file_import = maci.load(filepath)

    assert file_import.data_list == [1,2,3]
    assert file_import.data_tuple == (1,2,3)
    assert file_import.data_set == {1,2,3}

    # Test Indentation OFF
    maci.dump(filepath, file_data, indentation_on=False)
    file_import = maci.load(filepath)

    assert file_import.data_list == [1,2,3]
    assert file_import.data_tuple == (1,2,3)
    assert file_import.data_set == {1,2,3}

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Dump File - Multi-Line String: MaciDataObj - Test Multi-Line String Format
def test3_dump_file_multiline_str_maciobj():
    filename = '3_dump_file_multiline_str_maciobj.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Build Data
    file_data = maci.build()
    file_data.data_int = 1
    file_data.data_multi_str1 = "data line 1\ndata line 2\ndata line 3"
    file_data.data_multi_str2 = "'data line 1\ndata line 2\ndata line 3'"
    file_data.data_multi_str3 = '"data line 1\ndata line 2\ndata line 3"'
    file_data.data_multi_str4 = '"""data line 1\ndata line 2\ndata line 3"""'
    file_data.data_multi_str5 = "'''data line 1\ndata line 2\ndata line 3'''"
    file_data.data_multi_str6 = "data line 1\ndata line ''' 2\ndata line 3"
    file_data.data_multi_str7 = 'data line 1\ndata line """ 2\ndata line 3'
    file_data.data_multi_str8 = 'data line 1\ndata line "" 2\ndata line 3'
    file_data.data_multi_str9 = "data line 1\ndata line '' 2\ndata line 3"
    file_data.data_bool = False

    # Test Multi-Line String Dump and Load
    maci.dump(filepath, file_data, multi_line_str=True)
    file_import = maci.load(filepath)

    assert file_import.data_int == 1
    assert file_import.data_multi_str1 == "\ndata line 1\ndata line 2\ndata line 3\n"
    assert file_import.data_multi_str2 == "\n'data line 1\ndata line 2\ndata line 3'\n"
    assert file_import.data_multi_str3 == '\n"data line 1\ndata line 2\ndata line 3"\n'
    assert file_import.data_multi_str4 == '\n"""data line 1\ndata line 2\ndata line 3"""\n'
    assert file_import.data_multi_str5 == "\n'''data line 1\ndata line 2\ndata line 3'''\n"
    assert file_import.data_multi_str6 == "\ndata line 1\ndata line ''' 2\ndata line 3\n"
    assert file_import.data_multi_str7 == '\ndata line 1\ndata line """ 2\ndata line 3\n'
    assert file_import.data_multi_str8 == '\ndata line 1\ndata line "" 2\ndata line 3\n'
    assert file_import.data_multi_str9 == "\ndata line 1\ndata line '' 2\ndata line 3\n"
    assert file_import.data_bool == False

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 4. Encoding: MaciDataObj - Test some common encoding types
def test4_dump_and_load_encodings():
    filename = '4_dump_file_encoding.data'
    filepath = test_file_path + filename
    encodings_to_test = {
        'utf-8',
        'utf-16',
        'utf-32',
        'ascii',
        'iso-8859-1',
        'cp1252',
    }

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)

    # Build Data
    file_data = maci.build()
    file_data.data_dict = {'key': 'data'}

    # Test Dump and Load with Various Encodings
    for encoding in encodings_to_test:
        maci.dump(filepath, file_data, encoding=encoding)
        time.sleep(file_delay_timer)
        file_import = maci.load(filepath, encoding=encoding)

        # Test Section Data from File Load
        assert 'data' == file_import.data_dict.get('key')

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 5. Dump File - Attr Types: MaciDataObj - Test different attribute types to dump and ensure data is maintained
def test5_dump_file_attr_types_maciobj():
    filename = '5_dump_file_attr_types_maciobj.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Build Data
    file_data = maci.build()
    file_data.norm_data1 = 'data1'
    file_data._under_data = 'data'
    file_data.__dunder_data = 'data'
    file_data.norm_data2 = 'data2'
    
    # Test: All Private Attrs
    maci.dump(filepath, file_data, private_attrs=True)
    file_import = maci.load(filepath)

    assert file_import.norm_data1 == 'data1'
    assert file_import._under_data == 'data'
    assert file_import.__dunder_data == 'data'
    assert file_import.norm_data2 == 'data2'

    # Test: Private Under Attrs
    maci.dump(filepath, file_data, private_under_attrs=True)
    file_import = maci.load(filepath)

    assert file_import.norm_data1 == 'data1'
    assert file_import._under_data == 'data'
    assert file_import.norm_data2 == 'data2'

    # Test: Private Dunder Attrs
    maci.dump(filepath, file_data, private_dunder_attrs=True)
    file_import = maci.load(filepath)

    assert file_import.norm_data1 == 'data1'
    assert file_import.__dunder_data == 'data'
    assert file_import.norm_data2 == 'data2'

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 6. Dump File - Use Symbol Glyphs: MaciDataObj - Test dump with symbol glyph representation
def test6_dump_file_use_symbol_glyphs_maciobj():
    filename = '6_dump_file_use_symbol_glyphs_maciobj.data'
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
    maci.dump(filepath, file_data, use_symbol_glyphs=True)
    file_import = maci.load(filepath)

    assert file_import.norm_data == 'data'
    assert file_import.map_data == 'data'
    assert file_import.lock_data == 'data'
    assert file_import.hard_lock_data == 'data'
    assert file_import.map_lock == 'data'
    assert file_import.map_hard_lock == 'data'

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
