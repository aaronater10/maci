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