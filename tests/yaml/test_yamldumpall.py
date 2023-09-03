# yamldumpall - Tests
from src import maci
from os import remove, path
import time

test_file_path = './tests/test_files/yaml/'
file_delay_timer = 0.25
py_list = [
    {'k1': 1},
    {'k1': 2},
    {'k1': 3}
]


################################################################
# TESTS

# 1. Export Yaml Docs to File = Export a yaml file and validate attributes can be imported and match
def test1_yamldumpall_export_file():
    file_to_export = '1_yamldumpall_export.yml'    
    filepath = test_file_path + file_to_export
    reference_key = 'k1'
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    maci.yamldumpall(filepath, py_list)
    yaml_imported = maci.yamlloadall(filepath)

    for match_value,doc in enumerate(yaml_imported, start=1):
        assert match_value == doc[reference_key]

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. YAML Dump All Append - Appending yaml docs to yaml file and test data
def test2_yamldumpall_append():
    file_to_export = '1_yamldumpall_export.yml'    
    filepath = test_file_path + file_to_export
    reference_key = 'k1'
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    maci.yamldumpall(filepath, py_list)
    maci.yamldumpall(filepath, py_list, append=True)
    maci.yamldumpall(filepath, py_list, append=True)
    yaml_imported = maci.yamlloadall(filepath)

    match_value = 1
    for doc in yaml_imported:
        assert match_value == doc[reference_key]

        if match_value == 3:
            match_value = 1
            continue
        match_value += 1

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Encoding - Test some common encoding types
def test3_yamldumpall_and_yamlloadall_encodings():
    filename = '3_yaml_dumpall_loadall_encoding.yaml'
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
    yaml_data = [{'key': 'data'}]

    # Test Dump and Load with Various Encodings
    for encoding in encodings_to_test:
        maci.yamldumpall(filepath, yaml_data, encoding=encoding)
        time.sleep(file_delay_timer)
        file_import = maci.yamlloadall(filepath, encoding=encoding)

        # Test Section Data from File Load
        for yaml_doc in file_import:
            assert 'data' == yaml_doc.get('key')

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
