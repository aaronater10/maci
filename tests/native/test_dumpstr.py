# dumpstr - Tests
from src import maci

test_file_path = './tests/test_files/native/dumpstr_files/'

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
def test5_dumpstr_str_indentation_class1():
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


### MaciDataObj ###

# 1. Dump Str - Indentation: MaciDataObj - Test Indenting and Indentation off
def test1_dumpstr_str_indentation_maciobj():
    # Build Data
    str_data_build = maci.build()
    str_data_build.data_list = [1,2,3]
    str_data_build.data_tuple = (1,2,3)
    str_data_build.data_set = {1,2,3}

    # Test Indent Level at 0 and its Data
    str_data = maci.dumpstr(str_data_build, indent_level=0)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}

    # Test Indent Level at 7 and its Data
    str_data = maci.dumpstr(str_data_build, indent_level=7)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}

    # Test Indentation OFF
    str_data = maci.dumpstr(str_data_build, indentation_on=False)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}


# 2. Dump Str - Multi-Line String: MaciDataObj - Test Multi-Line String Format
def test2_dumpstr_str_multiline_str_maciobj():
    # Build Data
    str_data_build = maci.build()
    str_data_build.data_int = 1
    str_data_build.data_multi_str1 = "data line 1\ndata line 2\ndata line 3"
    str_data_build.data_multi_str2 = "'data line 1\ndata line 2\ndata line 3'"
    str_data_build.data_multi_str3 = '"data line 1\ndata line 2\ndata line 3"'
    str_data_build.data_multi_str4 = '"""data line 1\ndata line 2\ndata line 3"""'
    str_data_build.data_multi_str5 = "'''data line 1\ndata line 2\ndata line 3'''"
    str_data_build.data_multi_str6 = "data line 1\ndata line ''' 2\ndata line 3"
    str_data_build.data_multi_str7 = 'data line 1\ndata line """ 2\ndata line 3'
    str_data_build.data_multi_str8 = 'data line 1\ndata line "" 2\ndata line 3'
    str_data_build.data_multi_str9 = "data line 1\ndata line '' 2\ndata line 3"
    str_data_build.data_bool = False

    # Test Multi-Line String Dump and Load
    str_data = maci.dumpstr(str_data_build, multi_line_str=True)
    str_import = maci.loadstr(str_data)

    assert str_import.data_int == 1
    assert str_import.data_multi_str1 == "\ndata line 1\ndata line 2\ndata line 3\n"
    assert str_import.data_multi_str2 == "\n'data line 1\ndata line 2\ndata line 3'\n"
    assert str_import.data_multi_str3 == '\n"data line 1\ndata line 2\ndata line 3"\n'
    assert str_import.data_multi_str4 == '\n"""data line 1\ndata line 2\ndata line 3"""\n'
    assert str_import.data_multi_str5 == "\n'''data line 1\ndata line 2\ndata line 3'''\n"
    assert str_import.data_multi_str6 == "\ndata line 1\ndata line ''' 2\ndata line 3\n"
    assert str_import.data_multi_str7 == '\ndata line 1\ndata line """ 2\ndata line 3\n'
    assert str_import.data_multi_str8 == '\ndata line 1\ndata line "" 2\ndata line 3\n'
    assert str_import.data_multi_str9 == "\ndata line 1\ndata line '' 2\ndata line 3\n"
    assert str_import.data_bool == False


# 3. Dump Str - Attr Types: MaciDataObj - Test different attribute types to dump and ensure data is maintained
def test3_dumpstr_str_attr_types_maciobj():
    # Build Data
    str_data_build = maci.build()
    str_data_build.norm_data1 = 'data1'
    str_data_build._under_data = 'data'
    str_data_build.__dunder_data = 'data'
    str_data_build.norm_data2 = 'data2'
    
    # Test: All Private Attrs
    str_data = maci.dumpstr(str_data_build, private_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.norm_data1 == 'data1'
    assert str_import._under_data == 'data'
    assert str_import.__dunder_data == 'data'
    assert str_import.norm_data2 == 'data2'

    # Test: Private Under Attrs
    str_data = maci.dumpstr(str_data_build, private_under_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.norm_data1 == 'data1'
    assert str_import._under_data == 'data'
    assert str_import.norm_data2 == 'data2'

    # Test: Private Dunder Attrs
    str_data = maci.dumpstr(str_data_build, private_dunder_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.norm_data1 == 'data1'
    assert str_import.__dunder_data == 'data'
    assert str_import.norm_data2 == 'data2'


# 4. Dump Str - Use Symbol Glyphs: MaciDataObj - Test dump with symbol glyph representation
def test4_dumpstr_str_use_symbol_glyphs_maciobj():
    # Build Data
    str_data_build = maci.build()
    str_data_build.norm_data = 'data'
    str_data_build.map_data = None
    str_data_build.lock_data = 'data'
    str_data_build.hard_lock_data = 'data'
    str_data_build.map_lock = None
    str_data_build.map_hard_lock = None

    # Setup Attrs
    str_data_build.map_attr('map_data', 'norm_data')
    str_data_build.lock_attr('lock_data')
    str_data_build.hard_lock_attr('hard_lock_data')

    str_data_build.map_attr('map_lock', 'lock_data')
    str_data_build.lock_attr('map_lock')

    str_data_build.map_attr('map_hard_lock', 'hard_lock_data')
    str_data_build.hard_lock_attr('map_hard_lock')

    # Test dump with symbols and test data
    str_data = maci.dumpstr(str_data_build, use_symbol_glyphs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.norm_data == 'data'
    assert str_import.map_data == 'data'
    assert str_import.lock_data == 'data'
    assert str_import.hard_lock_data == 'data'
    assert str_import.map_lock == 'data'
    assert str_import.map_hard_lock == 'data'


### DICT ###

# 1. Dump Str - Indentation: Dict - Test Indenting and Indentation off
def test1_dumpstr_str_indentation_dict():
    # Build Data
    str_data_dict = {
    'data_list': [1,2,3],
    'data_tuple': (1,2,3),
    'data_set': {1,2,3},
    }

    # Test Indent Level at 0 and its Data
    str_data = maci.dumpstr(str_data_dict, indent_level=0)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}

    # Test Indent Level at 7 and its Data
    str_data = maci.dumpstr(str_data_dict, indent_level=7)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}

    # Test Indentation OFF
    str_data = maci.dumpstr(str_data_dict, indentation_on=False)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}


# 2. Dump Str - Multi-Line String: Dict - Test Multi-Line String Format
def test2_dumpstr_str_multiline_str_dict():
    # Build Data
    str_data_dict = {
    'data_int': 1,
    'data_multi_str1': "data line 1\ndata line 2\ndata line 3",
    'data_multi_str2': "'data line 1\ndata line 2\ndata line 3'",
    'data_multi_str3': '"data line 1\ndata line 2\ndata line 3"',
    'data_multi_str4': '"""data line 1\ndata line 2\ndata line 3"""',
    'data_multi_str5': "'''data line 1\ndata line 2\ndata line 3'''",
    'data_multi_str6': "data line 1\ndata line ''' 2\ndata line 3",
    'data_multi_str7': 'data line 1\ndata line """ 2\ndata line 3',
    'data_multi_str8': 'data line 1\ndata line "" 2\ndata line 3',
    'data_multi_str9': "data line 1\ndata line '' 2\ndata line 3",
    'data_bool': False,
    }

    # Test Multi-Line String Dump and Load
    str_data = maci.dumpstr(str_data_dict, multi_line_str=True)
    str_import = maci.loadstr(str_data)

    assert str_import.data_int == 1
    assert str_import.data_multi_str1 == "\ndata line 1\ndata line 2\ndata line 3\n"
    assert str_import.data_multi_str2 == "\n'data line 1\ndata line 2\ndata line 3'\n"
    assert str_import.data_multi_str3 == '\n"data line 1\ndata line 2\ndata line 3"\n'
    assert str_import.data_multi_str4 == '\n"""data line 1\ndata line 2\ndata line 3"""\n'
    assert str_import.data_multi_str5 == "\n'''data line 1\ndata line 2\ndata line 3'''\n"
    assert str_import.data_multi_str6 == "\ndata line 1\ndata line ''' 2\ndata line 3\n"
    assert str_import.data_multi_str7 == '\ndata line 1\ndata line """ 2\ndata line 3\n'
    assert str_import.data_multi_str8 == '\ndata line 1\ndata line "" 2\ndata line 3\n'
    assert str_import.data_multi_str9 == "\ndata line 1\ndata line '' 2\ndata line 3\n"
    assert str_import.data_bool == False


### Class ###

# 1. Dump Str - Indentation: Class - Test Indenting and Indentation off
def test1_dumpstr_str_indentation_class2():
    # Build Data
    class CustomClass:
        def __init__(self):
            self.data_list = [1,2,3]
            self.data_tuple = (1,2,3)
            self.data_set = {1,2,3}
    str_data_class = CustomClass()

    # Test Indent Level at 0 and its Data
    str_data = maci.dumpstr(str_data_class, indent_level=0)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}

    # Test Indent Level at 7 and its Data
    str_data = maci.dumpstr(str_data_class, indent_level=7)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}

    # Test Indentation OFF
    str_data = maci.dumpstr(str_data_class, indentation_on=False)
    str_import = maci.loadstr(str_data)

    assert str_import.data_list == [1,2,3]
    assert str_import.data_tuple == (1,2,3)
    assert str_import.data_set == {1,2,3}


# 2. Dump Str - Multi-Line String: Class - Test Multi-Line String Format
def test2_dumpstr_str_multiline_str_class():
    # Build Data
    class CustomClass:
        def __init__(self):
            self.data_int = 1
            self.data_multi_str1 = "data line 1\ndata line 2\ndata line 3"
            self.data_multi_str2 = "'data line 1\ndata line 2\ndata line 3'"
            self.data_multi_str3 = '"data line 1\ndata line 2\ndata line 3"'
            self.data_multi_str4 = '"""data line 1\ndata line 2\ndata line 3"""'
            self.data_multi_str5 = "'''data line 1\ndata line 2\ndata line 3'''"
            self.data_multi_str6 = "data line 1\ndata line ''' 2\ndata line 3"
            self.data_multi_str7 = 'data line 1\ndata line """ 2\ndata line 3'
            self.data_multi_str8 = 'data line 1\ndata line "" 2\ndata line 3'
            self.data_multi_str9 = "data line 1\ndata line '' 2\ndata line 3"
            self.data_bool = False
    str_data_class = CustomClass()

    # Test Multi-Line String Dump and Load
    str_data = maci.dumpstr(str_data_class, multi_line_str=True)
    str_import = maci.loadstr(str_data)

    assert str_import.data_int == 1
    assert str_import.data_multi_str1 == "\ndata line 1\ndata line 2\ndata line 3\n"
    assert str_import.data_multi_str2 == "\n'data line 1\ndata line 2\ndata line 3'\n"
    assert str_import.data_multi_str3 == '\n"data line 1\ndata line 2\ndata line 3"\n'
    assert str_import.data_multi_str4 == '\n"""data line 1\ndata line 2\ndata line 3"""\n'
    assert str_import.data_multi_str5 == "\n'''data line 1\ndata line 2\ndata line 3'''\n"
    assert str_import.data_multi_str6 == "\ndata line 1\ndata line ''' 2\ndata line 3\n"
    assert str_import.data_multi_str7 == '\ndata line 1\ndata line """ 2\ndata line 3\n'
    assert str_import.data_multi_str8 == '\ndata line 1\ndata line "" 2\ndata line 3\n'
    assert str_import.data_multi_str9 == "\ndata line 1\ndata line '' 2\ndata line 3\n"
    assert str_import.data_bool == False


# 3. Dump Str - Attr Types: Class - Test different attribute types to dump and ensure data is maintained
def test3_dumpstr_str_attr_types_class():
    # Build Data
    class CustomClass:
        # Class Attrs
        cls_norm_data1 = 'data1'
        _cls_under_data = 'data'
        __cls_dunder_data = 'data'
        cls_norm_data2 = 'data2'
        def __init__(self):
            # Init Attrs
            self.init_norm_data1 = 'data1'
            self._init_under_data = 'data'
            self.__init_dunder_data = 'data'
            self.init_norm_data2 = 'data2'
    str_data_class = CustomClass()

    ### INIT & CLASS ###

    # Test: All Normal Init & Class Attrs
    str_data = maci.dumpstr(str_data_class, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: All Normal/Private Init & Class Attrs
    str_data = maci.dumpstr(str_data_class, private_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: All Normal/Under Init & Class Attrs
    str_data = maci.dumpstr(str_data_class, private_under_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: All Normal/Dunder Init & Class Attrs
    str_data = maci.dumpstr(str_data_class, private_dunder_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal Init & Normal/Private Class Attrs
    str_data = maci.dumpstr(str_data_class, private_class_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal Init & Normal/Under Class Attrs
    str_data = maci.dumpstr(str_data_class, private_class_under_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal Init & Normal/Dunder Class Attrs
    str_data = maci.dumpstr(str_data_class, private_class_dunder_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal Class & Normal/Private Init Attrs
    str_data = maci.dumpstr(str_data_class, private_init_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.cls_norm_data2 == 'data2'
    
    # Test: Normal Class & Normal/Under Init Attrs
    str_data = maci.dumpstr(str_data_class, private_init_under_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal Class & Normal/Dunder Init Attrs
    str_data = maci.dumpstr(str_data_class, private_init_dunder_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'
    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.cls_norm_data2 == 'data2'


    ### CLASS ONLY ###

    # Test: Normal Class Attrs
    str_data = maci.dumpstr(type(str_data_class), class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal/Private Class Attrs
    str_data = maci.dumpstr(type(str_data_class), private_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal/Private Class Attrs - Alternate Option
    str_data = maci.dumpstr(type(str_data_class), private_class_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal/Under Class Attrs
    str_data = maci.dumpstr(type(str_data_class), private_under_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal/Under Class Attrs - Alternate Option
    str_data = maci.dumpstr(type(str_data_class), private_class_under_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.cls_norm_data1 == 'data1'
    assert str_import._cls_under_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal/Dunder Class Attrs
    str_data = maci.dumpstr(type(str_data_class), private_dunder_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'

    # Test: Normal/Dunder Class Attrs - Alternate Option
    str_data = maci.dumpstr(type(str_data_class), private_class_dunder_attrs=True, class_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.cls_norm_data1 == 'data1'
    assert str_import.__cls_dunder_data == 'data'
    assert str_import.cls_norm_data2 == 'data2'


    ### INIT ONLY ###

    # Test: Normal Init Attrs
    str_data = maci.dumpstr(str_data_class)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.init_norm_data2 == 'data2'

    # Test: Normal/Private Init Attrs
    str_data = maci.dumpstr(str_data_class, private_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'

    # Test: Normal/Private Init Attrs - Alternate Option
    str_data = maci.dumpstr(str_data_class, private_init_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'

    # Test: Normal/Under Init Attrs
    str_data = maci.dumpstr(str_data_class, private_under_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.init_norm_data2 == 'data2'

    # Test: Normal/Under Init Attrs - Alternate Option
    str_data = maci.dumpstr(str_data_class, private_init_under_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import._init_under_data == 'data'
    assert str_import.init_norm_data2 == 'data2'

    # Test: Normal/Dunder Init Attrs
    str_data = maci.dumpstr(str_data_class, private_dunder_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'

    # Test: Normal/Dunder Init Attrs - Alternate Option
    str_data = maci.dumpstr(str_data_class, private_init_dunder_attrs=True)
    str_import = maci.loadstr(str_data)

    assert str_import.init_norm_data1 == 'data1'
    assert str_import.__init_dunder_data == 'data'
    assert str_import.init_norm_data2 == 'data2'
