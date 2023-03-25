# exceptions: ini - Tests
from src import maci
from os import remove, path
import time
from configparser import ConfigParser
import pytest

test_file_path = './tests/test_files/ini/'
file_delay_timer = 0.25


################################################################
# TESTS

### inibuildauto ###

# 1. Ini Build Auto - Type Checks
def test1_exceptions_inibuildauto_types():
    with pytest.raises(maci.error.IniBuildAuto):
        maci.inibuildauto(1.0)


# 2. Ini Build Auto - Unsupported Options or Data
def test2_exceptions_inibuildauto_opts_data():
    with pytest.raises(maci.error.IniBuildAuto):
        maci.inibuildauto({'invalid structure1': []})


### inibuildmanual ### - NO EXCEPTIONS AVAILABLE TO TEST AT THIS TIME


### inidump ###

# 1. Ini Dump - Type Checks
def test1_exceptions_inidump_types():
    config_parser_obj = ConfigParser()

    # Tests
    with pytest.raises(maci.error.IniDump):
        maci.inidump(filename=1.0, ini_data=config_parser_obj)
    with pytest.raises(maci.error.IniDump):
        maci.inidump(filename='', ini_data=1.0)
    with pytest.raises(maci.error.IniDump):
        maci.inidump(filename='', ini_data=config_parser_obj, append=1.0)
    with pytest.raises(maci.error.IniDump):
        maci.inidump(filename='', ini_data=config_parser_obj, append=False, encoding=1.0)


# 2. Ini Dump - Unsupported Options or Data
def test2_exceptions_inidump_opts_data():
    filepath = test_file_path + 'exc_inidump.ini'
    config_parser_obj = ConfigParser()

    # Remove Any Existing Cache Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.IniDump):
        maci.inidump(filename='', ini_data=config_parser_obj)
    with pytest.raises(maci.error.IniDump):
        maci.inidump(filename=filepath, ini_data=config_parser_obj, append=False, encoding='')

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### iniload ###

# 1. Ini Load - Type Checks
def test1_exceptions_iniload_types():
    config_parser_obj = ConfigParser()

    # Tests
    with pytest.raises(maci.error.IniLoad):
        maci.iniload(filename=1.0)
    with pytest.raises(maci.error.IniLoad):
        maci.iniload(filename='', encoding=1.0)


# 2. Ini Load - Unsupported Options or Data
def test2_exceptions_iniload_opts_data():
    filepath = test_file_path + 'exc_iniload.ini'

    # Tests
    with pytest.raises(maci.error.IniLoad):
        maci.iniload(filename='')
    with pytest.raises(maci.error.IniLoad):
        maci.iniload(filename=filepath, encoding='')
