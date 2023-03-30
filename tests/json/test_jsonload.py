# jsonload - Tests
from src import maci

test_file_path = './tests/test_files/json/'


################################################################
# TESTS


# 1. JSON Data Import - Importing json file data and test attributes
def test1_json_file_import():
    filename = '1_import_data_file.json'
    filepath = test_file_path + filename    

    # Test Data and it's Type
    json_import = maci.jsonload(filepath)

    assert (json_import['string_data'] == 'data') and (isinstance(json_import['string_data'], str))
    assert (json_import['int_data'] == 256) and (isinstance(json_import['int_data'], int))
    assert (json_import['array_data'] == [1,2,3]) and (isinstance(json_import['array_data'], list))
    assert (json_import['bool_data'] == True) and (isinstance(json_import['bool_data'], bool))
    assert (json_import['null_data'] == None) and (isinstance(json_import['null_data'], type(None)))
