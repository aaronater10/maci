# tomldump - Tests
from src import maci
from os import remove, path
import time

test_file_path = './tests/test_files/toml/'
file_delay_timer = 0.25


################################################################
# TESTS


# 1. TOML Dump - Dumping toml file data and test attributes
def test1_tomldump_file():
    filename = '1_dump_data.toml'
    filepath = test_file_path + filename
    toml_data = {
    'string_data': 'data',
    'int_data': 256,
    'float_data': 1.7,
    'array_data': [1,2,3],
    'bool_data': True,
    'section': {'sub_section': {'string_data': 'data', 'int_data': 256}}
    }
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test Not Exist, Create, Exist, test data and it's Type
    assert not path.exists(filepath)
    maci.tomldump(filepath, toml_data)
    assert path.exists(filepath)
    toml_import = maci.tomlload(filepath)

    assert toml_import['string_data'] == 'data'
    assert toml_import['int_data'] == 256
    assert toml_import['float_data'] == 1.7
    assert toml_import['array_data'] == [1,2,3]
    assert toml_import['bool_data'] == True
    assert toml_import['section']['sub_section'] == {'string_data': 'data', 'int_data': 256}

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. TOML Data Append - Appending toml data to toml file and test data
def test2_tomldump_append():
    filename = '2_append_file_data.toml'
    filepath = test_file_path + filename
    expected_toml = {
        's0': {'int_data': 1, 'bool_data': True},
        's1': {'int_data': 1, 'bool_data': True},
        's2': {'int_data': 1, 'bool_data': True}
    }

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test not exist, create file by appending data, check if file exist, then test data
    assert not path.exists(filepath)
    append_times = 3
    for append_num in range(append_times):
        dump_data = {f's{append_num}': {'int_data': 1, 'bool_data': True}}
        maci.tomldump(filepath, dump_data, append=True)

    assert path.exists(filepath)
    file_import = maci.tomlload(filepath)

    # Test Data from File Load
    assert expected_toml == file_import

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. TOML Multi-String Data - Test Multiline String toml data from file
def test3_tomldump_multi_str():
    filename = '3_multiline_str_data.toml'
    filepath = test_file_path + filename
    expected_toml_data = {'data': "my\nmulti\nstring\n"}
    expected_toml_str = '''\
data = """
my
multi
string
"""
'''

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test not exist, create file by appending data, check if file exist, then test data
    assert not path.exists(filepath)

    toml_data = {'data': "my\nmulti\nstring\n"}
    maci.tomldump(filepath, toml_data, multi_line_str=True)

    assert path.exists(filepath)
    file_import_str = maci.loadraw(filepath)
    file_import_data = maci.tomlload(filepath)

    # Test Data from File Load
    assert expected_toml_str == file_import_str
    assert expected_toml_data['data'] == file_import_data['data']

    # # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
