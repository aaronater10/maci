# inidump - Tests
from src import maci
from os import remove, path
import time

test_file_path = './tests/test_files/ini/'
file_delay_timer = 0.5


################################################################
# TESTS

# 1. INI Data Dump - Exporting ini file data and test attributes
def test1_inidump_export():
    filename = '1_export_file_data.ini'
    filepath = test_file_path + filename
    ini_data = {
    'str_data': {'key': 'data'},
    'int_data': {'key': 256},
    'float_data': {'key': 2.5},
    'bool_data': {'key': True},
    'dict_data': {'key': {'k1': 1}},
    'list_data': {'key': [1,2,3]},
    'tuple_data': {'key': (1,2,3)},
    'set_data': {'key': {1,2,3}}
    }
    ini_data_build = maci.inibuildauto(ini_data)
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test Not Exist, Create, Exist, test data and it's Type
    assert not path.exists(filepath)
    maci.inidump(filepath, ini_data_build)
    assert path.exists(filepath)
    file_import = maci.iniload(filepath)

    sections_match = ['str_data', 'int_data', 'float_data', 'bool_data', 'dict_data', 'list_data', 'tuple_data', 'set_data']
    assert (file_import.sections() == sections_match) and (isinstance(file_import.sections(), list))

    for section,_ in ini_data.items():
        assert str(ini_data[section]['key']) == file_import.get(section, 'key')
        assert isinstance(file_import.get(section, 'key'), str)

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. INI Data Append - Appending ini data to ini file and test data
def test2_inidump_append():
    filename = '2_append_file_data.ini'
    filepath = test_file_path + filename
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test not exist, create file by appending data, check if file exist, then test data
    assert not path.exists(filepath)
    append_times = 3
    sections_match = []
    for append_num in range(append_times):
        section_name = f'str_data_{append_num}'
        ini_data = {section_name: {'key': 'data'}}
        ini_data_build = maci.inibuildauto(ini_data)
        maci.inidump(filepath, ini_data_build, append=True)
        sections_match.append(section_name)

    assert path.exists(filepath)
    file_import = maci.iniload(filepath)

    # Test Sections Match
    assert (file_import.sections() == sections_match)

    # Test Section Data from File Load
    for section in sections_match:
        assert 'data' == file_import.get(section, 'key')

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Encoding - Test some common encoding types
def test3_inidump_and_iniload_encodings():
    filename = '3_ini_encoding.ini'
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

    # Setup Ini Data
    section_name = 'str_data'
    ini_data = {section_name: {'key': 'data'}}
    ini_data_build = maci.inibuildauto(ini_data)

    # Test Dump and Load with Various Encodings
    for encoding in encodings_to_test:
        maci.inidump(filepath, ini_data_build, encoding=encoding)
        time.sleep(file_delay_timer)
        file_import = maci.iniload(filepath, encoding=encoding)

        # Test Section Match
        assert (file_import.sections() == [section_name])

        # Test Section Data from File Load
        assert 'data' == file_import.get(section_name, 'key')

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
