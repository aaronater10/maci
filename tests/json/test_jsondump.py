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