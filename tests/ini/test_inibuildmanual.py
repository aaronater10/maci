# inibuildmanual - Tests
from src import maci
from os import remove, path
import time
from configparser import ConfigParser

test_file_path = './tests/test_files/ini/'
file_delay_timer = 0.25


################################################################
# TESTS

# 1. INI Manual Build Data - Building ini data manually and test attributes
def test1_ini_build_manual_data():
    filename = '1_build_data_manual.ini'
    filepath = test_file_path + filename
    ini_data = {
    'str_data': {'key': 'data'},
    'int_data': {'key': 256},
    'float_data': {'key': 2.5},
    'bool_data': {'key': True},
    'dict_data': {'key': {'k1': 1}},
    'list_data': {'key': [1,2,3]},
    'tuple_data': {'key': (1,2,3)},
    'set_data': {'key': {1,2,3}}
    }

    # Test if instance matches it's unique type
    ini_data_build = maci.inibuildmanual()
    assert isinstance(ini_data_build, ConfigParser)

    # Manually build out ini data
    for key,value in ini_data.items():
        ini_data_build[key] = value
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test Not Exist, Create, Exist, test data and it's Type
    assert not path.exists(filepath)
    maci.inidump(filepath, ini_data_build)
    assert path.exists(filepath)
    file_import = maci.iniload(filepath)

    sections_match = ['str_data', 'int_data', 'float_data', 'bool_data', 'dict_data', 'list_data', 'tuple_data', 'set_data']
    assert (file_import.sections() == sections_match) and (isinstance(file_import.sections(), list))

    for section,_ in ini_data.items():
        assert str(ini_data[section]['key']) == file_import.get(section, 'key')
        assert isinstance(file_import.get(section, 'key'), str)

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass