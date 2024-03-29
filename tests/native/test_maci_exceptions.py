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
        maci.dump(filename="", data=maci.data.MaciDataObj)
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

    # Build Data
    maci_obj = maci.build()
    maci_data = maci.build()
    maci_data.maci_obj = maci_obj
    dict_data = {'k1': maci_obj}


    # Remove Any Existing Cache Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data={})
    with pytest.raises(maci.error.Dump):
        maci.dump(filename=filepath, data={}, encoding="")
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data=maci_data)
    with pytest.raises(maci.error.Dump):
        maci.dump(filename="", data=dict_data)

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### maci.dumpraw ###

# 1. Maci Dump Raw - Type Checks
def test1_exceptions_macidumpraw_types():
    # Tests
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename=1.0)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename="", append=1.0)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename="", byte_data=1.0)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename="", encoding=1.0)


# 2. Maci Dump Raw - Unsupported Options or Data
def test2_exceptions_macidumpraw_opts_data():
    filepath = test_file_path + 'exc_macidumpraw.maci'

    # Remove Any Existing Cache Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename="")
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename="", byte_data=True)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename="", append=True)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename=filepath)
        maci.dumpraw(filepath, "data", append=True, byte_data=True)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename=filepath, append=True, encoding="")
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename="", append=True, byte_data=True)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filepath, 1.0, byte_data=True)
    with pytest.raises(maci.error.DumpRaw):
        maci.dumpraw(filename=filepath, encoding="")

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### maci.dumpstr ###

# 1. Maci Dump Str - Type Checks
def test1_exceptions_macidumpstr_types():
    # Tests
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data=maci.data.MaciDataObj)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, indent_level=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, indentation_on=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, multi_line_str=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_under_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_dunder_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, class_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_init_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_init_under_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_init_dunder_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_class_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_class_under_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, private_class_dunder_attrs=1.0)
    with pytest.raises(maci.error.DumpStr):
        maci.dumpstr(data={}, use_symbol_glyphs=1.0)

# 2. Maci Dump Str - Unsupported Options or Data
### NO OPTS TO TEST ###


### maci.cleanformat ###

# 1. Maci Clean Format - Type Checks
def test1_exceptions_macicleanformat_types():
    # Tests
    with pytest.raises(maci.error.CleanFormat):
        maci.cleanformat(data=1.0)
    with pytest.raises(maci.error.CleanFormat):
        maci.cleanformat(data={}, indent_level=1.0)

# 2. Maci Clean Format - Unsupported Options or Data
### NO OPTS TO TEST ###


### maci.load ###

# 1. Maci Load - Type Checks
def test1_exceptions_maciload_types():
    # Tests
    with pytest.raises(maci.error.Load):
        maci.load(filename=1.0)
    with pytest.raises(maci.error.Load):
        maci.load(filename="", attr_name_dedup=1.0)
    with pytest.raises(maci.error.Load):
        maci.load(filename="", encoding=1.0)
    with pytest.raises(maci.error.Load):
        maci.load(filename="", _ignore_maci_attr_check=1.0)


# 2. Maci Load - Unsupported Options or Data
### load Note: Syntax/Parse Errors are already tested in functionality
def test2_exceptions_maciload_opts_data():
    filepath = test_file_path + 'exc_maciload.maci'

    # Tests
    with pytest.raises(maci.error.Load):
        maci.load(filename="")
    with pytest.raises(maci.error.Load):
        maci.load(filename="*")
    with pytest.raises(maci.error.Load):
        maci.load(filename=filepath, encoding="")


### maci.loadattrs ###

# 1. Maci Load Attrs - Type Checks
def test1_exceptions_maciloadattrs_types():
    # Build Data
    maci_data = maci.build()
    class CustomData: ...

    # Tests
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename=1.0, class_object=CustomData())
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename="", class_object=maci_data)
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename="", class_object=type(maci_data))
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename="", class_object={})
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename="", class_object=CustomData(), encoding=1.0)
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename="", class_object=CustomData(), attr_name_dedup=1.0)
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename="", class_object=CustomData(), _ignore_maci_attr_check=1.0)


# 2. Maci Load Attrs- Unsupported Options or Data
def test2_exceptions_maciloadattrs_opts_data():
    filepath = test_file_path + 'exc_maciloadattrs.maci'

    # Build Data
    class CustomData: ...

    # Tests
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename="", class_object=CustomData())
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filename=filepath, class_object=CustomData(), encoding="")


### maci.loaddict ###

# 1. Maci Load Dict - Type Checks
def test1_exceptions_maciloaddict_types():
    # Tests
    with pytest.raises(maci.error.LoadDict):
        maci.loaddict(filename=1.0)
    with pytest.raises(maci.error.LoadDict):
        maci.loaddict(filename="", attr_name_dedup=1.0)
    with pytest.raises(maci.error.LoadDict):
        maci.loaddict(filename="", encoding=1.0)


# 2. Maci Load Dict - Unsupported Options or Data
def test2_exceptions_maciloaddict_opts_data():
    filepath = test_file_path + 'exc_maciloaddict.maci'

    # Tests
    with pytest.raises(maci.error.LoadDict):
        maci.loaddict(filename="")
    with pytest.raises(maci.error.LoadDict):
        maci.loaddict(filename="*")
    with pytest.raises(maci.error.LoadDict):
        maci.loaddict(filename=filepath, encoding="")


### maci.loadraw ###

# 1. Maci Load Raw - Type Checks
def test1_exceptions_maciloadraw_types():
    # Tests
    with pytest.raises(maci.error.LoadRaw):
        maci.loadraw(filename=1.0)
    with pytest.raises(maci.error.LoadRaw):
        maci.loadraw(filename="", byte_data=1.0)
    with pytest.raises(maci.error.LoadRaw):
        maci.loadraw(filename="", encoding=1.0)


# 2. Maci Load Raw - Unsupported Options or Data
def test2_exceptions_maciloadraw_opts_data():
    filepath = test_file_path + 'exc_maciloadraw.maci'

    # Tests
    with pytest.raises(maci.error.LoadRaw):
        maci.loadraw(filename="")
    with pytest.raises(maci.error.LoadRaw):
        maci.loadraw(filename="", byte_data=True)
    with pytest.raises(maci.error.LoadRaw):
        maci.loadraw(filename=filepath, encoding="")


### maci.loadstr ###

# 1. Maci Load Str - Type Checks
def test1_exceptions_maciloadstr_types():
    # Tests
    with pytest.raises(maci.error.LoadStr):
        maci.loadstr(maci_str_data=1.0)
    with pytest.raises(maci.error.LoadStr):
        maci.loadstr(maci_str_data="", attr_name_dedup=1.0)

# 2. Maci Load Str - Unsupported Options or Data
### NO OPTS TO TEST ### - Syntax/Parse Errors are already tested in functionality


### maci.loadstrdict ###

# 1. Maci Load Str Dict - Type Checks
def test1_exceptions_maciloadstrdict_types():
    # Tests
    with pytest.raises(maci.error.LoadStrDict):
        maci.loadstrdict(maci_str_data=1.0)
    with pytest.raises(maci.error.LoadStrDict):
        maci.loadstrdict(maci_str_data="", attr_name_dedup=1.0)

# 2. Maci Load Str Dict - Unsupported Options or Data
### NO OPTS TO TEST ### - Syntax/Parse Errors are already tested in functionality


### MISC: maci ###

# 1. Test MaciDataObj getattr - test attr error thrown
def test1_exceptions_maciobj_getattr():
    # Build Data
    maci_data = maci.build()

    # Tests
    with pytest.raises(AttributeError):
        maci_data.data_str
