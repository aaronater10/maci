# yamlloadstr - Tests
from src import maci

test_file_path = './tests/test_files/yaml/'
file_delay_timer = 0.25


################################################################
# TESTS


# 1. YAML Data Import from str - Importing yaml data from str and test attributes
def test1_yaml_str_import():
    filename = '1_import_data_str.yml'
    filepath = test_file_path + filename    

    # Test Importing Data and it's Type
    yaml_raw = maci.loadraw(filepath)
    yaml_import = maci.yamlloadstr(yaml_raw)

    # Test Data
    assert (yaml_import['string_data'] == 'data') and (isinstance(yaml_import['string_data'], str))
    assert (yaml_import['int_data'] == 256) and (isinstance(yaml_import['int_data'], int))
    assert (yaml_import['array_data'] == [1,2,3]) and (isinstance(yaml_import['array_data'], list))
    assert (yaml_import['bool_data'] == True) and (isinstance(yaml_import['bool_data'], bool))
    assert (yaml_import['null_data'] == None) and (isinstance(yaml_import['null_data'], type(None)))
    assert (yaml_import['nested_data'] == {"k1": 1,"k2": 2,"k3": 3}) and (isinstance(yaml_import['nested_data'], dict))
    assert (yaml_import['list'] == [1,2,3]) and (isinstance(yaml_import['list'], list))