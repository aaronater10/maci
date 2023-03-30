# jsondump - Tests
from src import maci
from os import remove, path
import time

test_file_path = './tests/test_files/json/'
file_delay_timer = 0.25


################################################################
# TESTS


# 1. JSON Data Export - Exporting json file data and test attributes
def test1_json_file_export():
    filename = '1_export_data.json'
    filepath = test_file_path + filename
    json_data = {
    'string_data': 'data',
    'int_data': 256,
    'array_data': [1,2,3],
    'bool_data': True,
    'null_data': None
    }
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test Not Exist, Create, Exist, test data and it's Type
    assert not path.exists(filepath)
    maci.jsondump(filepath, json_data)
    assert path.exists(filepath)
    json_import = maci.jsonload(filepath)

    assert (json_import['string_data'] == 'data') and (isinstance(json_import['string_data'], str))
    assert (json_import['int_data'] == 256) and (isinstance(json_import['int_data'], int))
    assert (json_import['array_data'] == [1,2,3]) and (isinstance(json_import['array_data'], list))
    assert (json_import['bool_data'] == True) and (isinstance(json_import['bool_data'], bool))
    assert (json_import['null_data'] == None) and (isinstance(json_import['null_data'], type(None)))
    
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. JSON Data Append - Appending json data to json file and test data
def test2_jsondump_append():
    filename = '2_append_file_data.json'
    filepath = test_file_path + filename
    expected_json = """\
{
    "key": "data"
}
{
    "key": "data"
}
{
    "key": "data"
}"""
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test not exist, create file by appending data, check if file exist, then test data
    assert not path.exists(filepath)
    append_times = 3
    json_data = {'key': 'data'}
    for _ in range(append_times):
        maci.jsondump(filepath, json_data, append=True)

    assert path.exists(filepath)

    file_import = maci.loadraw(filepath)

    # Test Section Data from File Load
    assert expected_json == file_import

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Encoding - Test some common encoding types
def test3_jsondump_and_jsonload_encodings():
    filename = '3_json_encoding.json'
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

    # Setup Json Data
    json_data = {'key': 'data'}

    # Test Dump and Load with Various Encodings
    for encoding in encodings_to_test:
        maci.jsondump(filepath, json_data, encoding=encoding)
        time.sleep(file_delay_timer)
        file_import = maci.jsonload(filepath, encoding=encoding)

        # Test Section Data from File Load
        assert 'data' == file_import.get('key')

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
