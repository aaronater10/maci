# exceptions: maci - Tests
from src import maci
from os import remove
import time
import pytest

test_file_path = './tests/test_files/native/exception_files/'
file_delay_timer = 0.25


################################################################
# TESTS

### maci.dump ###

# 1. Maci Dump - Type Checks
def test1_exceptions_macidump_types():
    # Tests
    with pytest.raises(maci.error.Dump):
        maci.dump(filename=1.0, data={})
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, append=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, indent_level=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, indentation_on=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, multi_line_str=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, encoding=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_under_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_dunder_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, class_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_init_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_init_under_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_init_dunder_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_class_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_class_under_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, private_class_dunder_attrs=1.0)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={}, use_symbol_glyphs=1.0)


# 2. Maci Dump - Unsupported Options or Data
def test2_exceptions_macidump_opts_data():
    filepath = test_file_path + 'exc_macidump.maci'

    # Remove Any Existing Cache Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={})
    with pytest.raises(maci.error.Dump):
        maci.dump(filename=filepath, data={}, encoding="")

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass



### maci.cleanformat ###

# 1. Maci Clean Format - Type Checks
def test1_exceptions_macicleanformat_types():
    # Tests
    with pytest.raises(maci.error.CleanFormat):
        maci.cleanformat(data=1.0)
    with pytest.raises(maci.error.CleanFormat):
        maci.cleanformat(data={}, indent_level=1.0)

# 2. Maci Dump - Unsupported Options or Data
### NO OPTS TO TEST ###