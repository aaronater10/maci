# iniload - Tests
from src import maci

test_file_path = './tests/test_files/ini/'


################################################################
# TESTS

# 1. INI Data Import - Importing ini file data and test attributes
def test1_ini_file_import():
    filename = '1_import_file_data.ini'
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

    # Test imported data and it's Type
    file_import = maci.iniload(filepath)

    sections_match = ['str_data', 'int_data', 'float_data', 'bool_data', 'dict_data', 'list_data', 'tuple_data', 'set_data']
    assert (file_import.sections() == sections_match) and (isinstance(file_import.sections(), list))

    for section,_ in ini_data.items():
        assert str(ini_data[section]['key']) == file_import.get(section, 'key')
        assert isinstance(file_import.get(section, 'key'), str)


# 2. INI ExtendedInterpolation Import - Importing ini file data and test str interpolation and attributes
def test2_ini_extended_interpolation():
    filename = '2_import_interpolate_data.ini'
    filepath = test_file_path + filename
    str_interpolate_match = 'data-256-2.5-True'

    # Test imported data and it's Type
    file_import = maci.iniload(filepath)

    sections_match = ['str_data', 'int_data', 'float_data', 'bool_data', 'str_interpolate']
    assert (file_import.sections() == sections_match) and (isinstance(file_import.sections(), list))

    assert (file_import.get('str_interpolate', 'key') == str_interpolate_match) and (isinstance(file_import.get('str_interpolate', 'key'), str))
    assert (file_import.get('str_data', 'key') == 'data') and (isinstance(file_import.get('str_data', 'key'), str))
    assert (file_import.get('int_data', 'key') == '256') and (isinstance(file_import.get('int_data', 'key'), str))
    assert (file_import.get('float_data', 'key') == '2.5') and (isinstance(file_import.get('float_data', 'key'), str))
    assert (file_import.get('bool_data', 'key') == 'True') and (isinstance(file_import.get('bool_data', 'key'), str))