# tomldumpstr - Tests
from src import maci
from os import remove, path
import time


################################################################
# TESTS

# 1. TOML Dump String - Dumping toml string data and test attributes
def test1_tomldumpstr_data():
    toml_data = {
    'string_data': 'data',
    'int_data': 256,
    'float_data': 1.7,
    'array_data': [1,2,3],
    'bool_data': True,
    'section': {'sub_section': {'string_data': 'data', 'int_data': 256}}
    }

    # Load and test data
    toml_str_data = maci.tomldumpstr(toml_data)
    toml_import = maci.tomlloadstr(toml_str_data)

    assert toml_import['string_data'] == 'data'
    assert toml_import['int_data'] == 256
    assert toml_import['float_data'] == 1.7
    assert toml_import['array_data'] == [1,2,3]
    assert toml_import['bool_data'] == True
    assert toml_import['section']['sub_section'] == {'string_data': 'data', 'int_data': 256}


# 2. TOML Multi-String Data - Test Multiline String toml data from file
def test2_tomldumpstr_multi_str():
    expected_toml_data = {'data': "my\nmulti\nstring\n"}
    expected_toml_str = '''\
data = """
my
multi
string
"""
'''

    # Load and test data
    toml_data = {'data': "my\nmulti\nstring\n"}
    toml_str_data = maci.tomldumpstr(toml_data, multi_line_str=True)
    toml_import = maci.tomlloadstr(toml_str_data)

    assert expected_toml_str == toml_str_data
    assert expected_toml_data['data'] == toml_import['data']
