# exceptions: yaml - Tests
from src import maci
from os import remove
import time
import pytest

test_file_path = './tests/test_files/yaml/'
file_delay_timer = 0.25


################################################################
# TESTS

### yamldump ###

# 1. Yaml Dump - Type Checks
def test1_exceptions_yamldump_types():
    # Tests
    with pytest.raises(maci.error.YamlDump):
        maci.yamldump(filename=1.0, data={})
    with pytest.raises(maci.error.YamlDump):
        maci.yamldump(filename='', data={}, append=1.0)
    with pytest.raises(maci.error.YamlDump):
        maci.yamldump(filename='', data={}, encoding=1.0)


# 2. Yaml Dump - Unsupported Options or Data
def test2_exceptions_yamldump_opts_data():
    filepath = test_file_path + 'exc_yamldump.yaml'

    # Tests
    with pytest.raises(maci.error.YamlDump):
        maci.yamldump(filename='', data={})
    with pytest.raises(maci.error.YamlDump):
        maci.yamldump(filename=filepath, data={}, encoding='')

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### yamldumpstr ###

# 1. Yaml Dump Str - Type Checks
def test1_exceptions_yamldumpstr_types():
    class CustomData:
        data = 1

    # Tests
    with pytest.raises(maci.error.YamlDumpStr):
        maci.yamldumpstr(data=CustomData())


# 2. Yaml Dump Str - Unsupported Options or Data
def test2_exceptions_yamldumpstr_opts_data():
    class CustomData:
        data = 1

    # Tests
    with pytest.raises(maci.error.YamlDump):
        maci.yamldumpstr(data={'k': CustomData})


# # ### yamlload ###

# # 1. Yaml Load - Type Checks
# def test1_exceptions_yamlload_types():
#     # Tests
#     with pytest.raises(maci.error.YamlLoad):
#         maci.yamlload(filename=1.0)


# # 2. Yaml Load - Unsupported Options or Data
# def test2_exceptions_yamlload_opts_data():
#     # Tests
#     with pytest.raises(maci.error.YamlLoad):
#         maci.yamlload(filename='')


# # ### yamlloadstr ###

# # 1. Yaml Load Str - Type Checks
# def test1_exceptions_yamlloadstr_types():
#     # Tests
#     with pytest.raises(maci.error.YamlLoadStr):
#         maci.yamlloadstr(yaml_str_data=1.0)


# # 2. Yaml Load Str - Unsupported Options or Data
# def test2_exceptions_yamlloadstr_opts_data():
#     # Tests
#     with pytest.raises(maci.error.YamlLoadStr):
#         maci.yamlloadstr(yaml_str_data='k = {1,2,3}')
