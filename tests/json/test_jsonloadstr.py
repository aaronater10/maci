# jsonloadstr - Tests
from src import maci

test_file_path = './tests/test_files/json/'
file_delay_timer = 0.25


################################################################
# TESTS


# 1. JSON Data Import from str - Importing json data from str and test attributes
def test1_json_str_import():
    filename = '1_import_data_str.json'
    filepath = test_file_path + filename    

    # Test Importing Data and it's Type
    json_raw = maci.loadraw(filepath)
    json_import = maci.jsonloadstr(json_raw)

    assert (json_import['string_data'] == 'data') and (isinstance(json_import['string_data'], str))
    assert (json_import['int_data'] == 256) and (isinstance(json_import['int_data'], int))
    assert (json_import['array_data'] == [1,2,3]) and (isinstance(json_import['array_data'], list))
    assert (json_import['bool_data'] == True) and (isinstance(json_import['bool_data'], bool))
    assert (json_import['null_data'] == None) and (isinstance(json_import['null_data'], type(None)))
    assert (json_import['nested_data'] == {"k1": 1,"k2": 2,"k3": 3}) and (isinstance(json_import['nested_data'], dict))