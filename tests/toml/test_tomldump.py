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
# def test2_tomldump_append():
#     filename = '2_append_file_data.toml'
#     filepath = test_file_path + filename
#     expected_toml = """\
# {
#     "key": "data"
# }
# {
#     "key": "data"
# }
# {
#     "key": "data"
# }"""
    
#     # Remove Any Existing Test File
#     try: remove(filepath)
#     except: pass
#     time.sleep(file_delay_timer)

#     # Test not exist, create file by appending data, check if file exist, then test data
#     assert not path.exists(filepath)
#     append_times = 3
#     toml_data = {'key': 'data'}
#     for _ in range(append_times):
#         maci.tomldump(filepath, toml_data, append=True)

#     assert path.exists(filepath)

#     file_import = maci.loadraw(filepath)

#     # Test Section Data from File Load
#     assert expected_toml == file_import

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass


# # 3. Encoding - Test some common encoding types
# def test3_tomldump_and_tomlload_encodings():
#     filename = '3_toml_encoding.toml'
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

#     # Setup Toml Data
#     toml_data = {'key': 'data'}

#     # Test Dump and Load with Various Encodings
#     for encoding in encodings_to_test:
#         maci.tomldump(filepath, toml_data, encoding=encoding)
#         time.sleep(file_delay_timer)
#         file_import = maci.tomlload(filepath, encoding=encoding)

#         # Test Section Data from File Load
#         assert 'data' == file_import.get('key')

#     # Remove Test File
#     time.sleep(file_delay_timer)
#     try: remove(filepath)
#     except: pass
