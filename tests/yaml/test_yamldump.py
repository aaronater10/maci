# yamldump - Tests
from src import maci
from os import remove, path
import time

test_file_path = './tests/test_files/yaml/'
file_delay_timer = 0.25
py_dict = {
    'k1': 10, 
    'k2': "data", 
    'k3': True,
    'sub_list': [1,2,3],
    'sub_set': {1,2,3},
    'sub_dict': {'k1':1, 'k2':2, 'k3':3}
}


################################################################
# TESTS

# 1. Export Yaml File = Export a yaml file from py data and validate attributes can be imported and match
def test1_yaml_export_file():
    file_to_export = '1_yaml_export.yml'    
    filepath = test_file_path + file_to_export    
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test Not Exist, Create, Check Exist, then import
    assert not path.exists(filepath)
    maci.yamldump(filepath, py_dict)
    assert path.exists(filepath)
    yaml_imported = maci.yamlload(filepath)

    # Attrib Tests
    assert (yaml_imported['k1'] == 10) and (isinstance(yaml_imported['k1'], int))
    assert (yaml_imported['k2'] == "data") and (isinstance(yaml_imported['k2'], str))
    assert (yaml_imported['k3'] == True) and (isinstance(yaml_imported['k3'], bool))
    assert (yaml_imported['sub_list'] == [1,2,3]) and (isinstance(yaml_imported['sub_list'], list))
    assert (yaml_imported['sub_set'] == {1,2,3}) and (isinstance(yaml_imported['sub_set'], set))
    assert (yaml_imported['sub_dict'] == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(yaml_imported['sub_dict'], dict))

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. YAML Data Append - Appending yaml data to yaml file and test data
def test2_yamldump_append():
    filename = '2_append_file_data.yaml'
    filepath = test_file_path + filename
    expected_yaml = {
        'd0': {'int_data': 1, 'bool_data': True},
        'd1': {'int_data': 1, 'bool_data': True},
        'd2': {'int_data': 1, 'bool_data': True}
    }

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test not exist, create file by appending data, check if file exist, then test data
    assert not path.exists(filepath)
    append_times = 3
    for append_num in range(append_times):
        dump_data = {f'd{append_num}': {'int_data': 1, 'bool_data': True}}
        maci.yamldump(filepath, dump_data, append=True)

    assert path.exists(filepath)
    file_import = maci.yamlload(filepath)

    # Test Data from File Load
    assert expected_yaml == file_import

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Encoding - Test some common encoding types
def test3_yamldump_and_yamlload_encodings():
    filename = '3_yaml_encoding.yaml'
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

    # Setup Yaml Data
    yaml_data = {'key': 'data'}

    # Test Dump and Load with Various Encodings
    for encoding in encodings_to_test:
        maci.yamldump(filepath, yaml_data, encoding=encoding)
        time.sleep(file_delay_timer)
        file_import = maci.yamlload(filepath, encoding=encoding)

        # Test Section Data from File Load
        assert 'data' == file_import.get('key')

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
