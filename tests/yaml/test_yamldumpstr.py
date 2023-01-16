# yamldumpstr - Tests
from src import maci
from os import remove, path
import time

test_file_path = './tests/test_files/yaml/'
file_delay_timer = 0.5


################################################################
# TESTS


# 1. YAML Data Export to str - Exporting dict data returning str, and test attributes
def test1_yaml_str_export():
    filename = '1_export_data_str.yml'
    filepath = test_file_path + filename
    yaml_data = {
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

    # Test Not Exist, Create, Exist, Data and it's Type
    assert not path.exists(filepath)
    yaml_str = maci.yamldumpstr(yaml_data)
    maci.dumpraw(filepath, yaml_str)
    assert path.exists(filepath)
    yaml_import = maci.yamlload(filepath)

    # Test Data
    assert (yaml_import['string_data'] == 'data') and (isinstance(yaml_import['string_data'], str))
    assert (yaml_import['int_data'] == 256) and (isinstance(yaml_import['int_data'], int))
    assert (yaml_import['array_data'] == [1,2,3]) and (isinstance(yaml_import['array_data'], list))
    assert (yaml_import['bool_data'] == True) and (isinstance(yaml_import['bool_data'], bool))
    assert (yaml_import['null_data'] == None) and (isinstance(yaml_import['null_data'], type(None)))
    
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass