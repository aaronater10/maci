# exceptions: toml - Tests
from src import maci
from os import remove
import time
import pytest

test_file_path = './tests/test_files/toml/'
file_delay_timer = 0.25


################################################################
# TESTS

### tomldump ###

# 1. Toml Dump - Type Checks
def test1_exceptions_tomldump_types():
    # Tests
    with pytest.raises(maci.error.TomlDump):
        maci.tomldump(filename=1.0, data={})
    with pytest.raises(maci.error.TomlDump):
        maci.tomldump(filename='', data=1.0)
    with pytest.raises(maci.error.TomlDump):
        maci.tomldump(filename='', data={}, append=1.0)
    with pytest.raises(maci.error.TomlDump):
        maci.tomldump(filename='', data={}, multi_line_str=1.0)


# 2. Toml Dump - Unsupported Options or Data
def test2_exceptions_tomldump_opts_data():
    filepath = test_file_path + 'exc_tomldump.toml'

    # Tests
    with pytest.raises(maci.error.TomlDump):
        maci.tomldump(filename='', data={})
    with pytest.raises(maci.error.TomlDump):
        maci.tomldump(filename=filepath, data={'k': None})
    
    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### tomldumpstr ###

# 1. Toml Dump Str - Type Checks
def test1_exceptions_tomldumpstr_types():
    # Tests
    with pytest.raises(maci.error.TomlDumpStr):
        maci.tomldumpstr(data=1.0)
    with pytest.raises(maci.error.TomlDumpStr):
        maci.tomldumpstr(data={}, multi_line_str=1.0)


# 2. Toml Dump Str - Unsupported Options or Data
def test2_exceptions_tomldumpstr_opts_data():
    # Tests
    with pytest.raises(maci.error.TomlDumpStr):
        maci.tomldumpstr(data={'k': None})


# ### tomlload ###

# 1. Toml Load - Type Checks
def test1_exceptions_tomlload_types():
    # Tests
    with pytest.raises(maci.error.TomlLoad):
        maci.tomlload(filename=1.0)


# 2. Toml Load - Unsupported Options or Data
def test2_exceptions_tomlload_opts_data():
    filepath = test_file_path + 'exc_tomlload.toml'

    # Tests
    with pytest.raises(maci.error.TomlLoad):
        maci.tomlload(filename='')
    with pytest.raises(maci.error.TomlLoad):
        maci.tomlload(filename='*')
    with pytest.raises(maci.error.TomlLoad):
        maci.tomlload(filename=filepath)
    


### tomlloadstr ###

# 1. Toml Load Str - Type Checks
def test1_exceptions_tomlloadstr_types():
    # Tests
    with pytest.raises(maci.error.TomlLoadStr):
        maci.tomlloadstr(toml_str_data=1.0)


# 2. Toml Load Str - Unsupported Options or Data
def test2_exceptions_tomlloadstr_opts_data():
    # Tests
    with pytest.raises(maci.error.TomlLoadStr):
        maci.tomlloadstr(toml_str_data='k = {1,2,3}')
