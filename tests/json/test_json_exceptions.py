# exceptions: json - Tests
from src import maci
from os import remove
import time
import pytest

test_file_path = './tests/test_files/json/'
file_delay_timer = 0.25


################################################################
# TESTS

### jsondump ###

# 1. Json Dump - Type Checks
def test1_exceptions_jsondump_types():
    # Tests
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename=1.0, data='')
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename='', data={1,2,3})
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename='', data=[], append=1.0)
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename='', data=[], indent_level='')
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename='', data=[], encoding=1.0)


# 2. Json Dump - Unsupported Options or Data
def test2_exceptions_jsondump_opts_data():
    filepath = test_file_path + 'exc_jsondump.json'

    # Remove Any Existing Cache Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename='', data='')
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename=filepath, data={'k': {1,2,3}})
    with pytest.raises(maci.error.JsonDump):
        maci.jsondump(filename=filepath, data=[], encoding='')

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### jsondumpstr ###

# 1. Json DumpStr - Type Checks
def test1_exceptions_jsondumpstr_types():
    # Tests
    with pytest.raises(maci.error.JsonDumpStr):
        maci.jsondumpstr(data={1,2,3})
    with pytest.raises(maci.error.JsonDumpStr):
        maci.jsondumpstr(data=[], indent_level='')


# 2. Json DumpStr - Unsupported Options or Data
def test2_exceptions_jsondumpstr_opts_data():
    # Tests
    with pytest.raises(maci.error.JsonDumpStr):
        maci.jsondumpstr(data={'k': {1,2,3}})


### jsonload ###

# 1. Json Load - Type Checks
def test1_exceptions_jsonload_types():
    # Tests
    with pytest.raises(maci.error.JsonLoad):
        maci.jsonload(filename=1.0)
    with pytest.raises(maci.error.JsonLoad):
        maci.jsonload(filename='', encoding=1.0)


# 2. Json Load - Unsupported Options or Data
def test2_exceptions_jsonload_opts_data():
    filepath = test_file_path + 'exc_jsonload.json'
    filepath_err = test_file_path + 'exc_jsonload_err.json'

    # Tests
    with pytest.raises(maci.error.JsonLoad):
        maci.jsonload(filename='')
    with pytest.raises(maci.error.JsonLoad):
        maci.jsonload(filename='*')
    with pytest.raises(maci.error.JsonLoad):
        maci.jsonload(filename=filepath, encoding='')
    with pytest.raises(maci.error.JsonLoad):
        maci.jsonload(filename=filepath_err)


### jsonloadstr ###

# 1. Json Load Str - Type Checks
def test1_exceptions_jsonloadstr_types():
    # Tests
    with pytest.raises(maci.error.JsonLoadStr):
        maci.jsonloadstr(json_str_data=1.0)


# 2. Json Load Str - Unsupported Options or Data
def test2_exceptions_jsonloadstr_opts_data():
    # Tests
    with pytest.raises(maci.error.JsonLoadStr):
        maci.jsonloadstr(json_str_data='{"k": {1,2,3}}')
