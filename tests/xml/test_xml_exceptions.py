# exceptions: xml - Tests
from src import maci
from os import remove
import time
import pytest

test_file_path = './tests/test_files/xml/'
file_delay_timer = 0.25


################################################################
# TESTS

### xmlbuildmanual ### - NO EXCEPTIONS AVAILABLE TO TEST AT THIS TIME


### xmldump ###

# 1. Xml Dump - Type Checks
def test1_exceptions_xmldump_types():
    # Build Data
    xml_data = maci.xmlloadstr('<data>xml_data</data>')

    # Tests
    with pytest.raises(maci.error.XmlDump):
        maci.xmldump(filename=1.0, data=xml_data)
    with pytest.raises(maci.error.XmlDump):
        maci.xmldump(filename='', data=1.0)
    with pytest.raises(maci.error.XmlDump):
        maci.xmldump(filename='', data=xml_data, append=1.0)
    with pytest.raises(maci.error.XmlDump):
        maci.xmldump(filename='', data=xml_data, encoding=1.0)


# 2. Xml Dump - Unsupported Options or Data
def test2_exceptions_xmldump_opts_data():
    filepath = test_file_path + 'exc_xmldump.xml'

    # Build Data
    xml_data = maci.xmlloadstr('<data>xml_data</data>')

    # Remove Any Existing Cache Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.XmlDump):
        maci.xmldump(filename='', data=xml_data)
    with pytest.raises(maci.error.XmlDump):
        maci.xmldump(filename=filepath, data=xml_data, encoding='')

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### xmldumpdict ###

# 1. Xml Dump Dict - Type Checks
def test1_exceptions_xmldumpdict_types():
    # Build Data
    xml_data = maci.xmlloadstrdict('<data>xml_data</data>')

    # Tests
    with pytest.raises(maci.error.XmlDumpDict):
        maci.xmldumpdict(filename=1.0, data=xml_data)
    with pytest.raises(maci.error.XmlDumpDict):
        maci.xmldumpdict(filename='', data=1.0)
    with pytest.raises(maci.error.XmlDumpDict):
        maci.xmldumpdict(filename='', data=xml_data, append=1.0)
    with pytest.raises(maci.error.XmlDumpDict):
        maci.xmldumpdict(filename='', data=xml_data, pretty=1.0)
    with pytest.raises(maci.error.XmlDumpDict):
        maci.xmldumpdict(filename='', data=xml_data, full_doc=1.0)


# 2. Xml Dump Dict - Unsupported Options or Data
def test2_exceptions_xmldumpdict_opts_data():
    filepath = test_file_path + 'exc_xmldumpdict.xml'

    # Build Data
    xml_data = maci.xmlloadstrdict('<data>xml_data</data>')

    # Remove Any Existing Cache Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.XmlDumpDict):
        maci.xmldumpdict(filename='', data=xml_data)
    with pytest.raises(maci.error.XmlDumpDict):
        maci.xmldumpdict(filename=filepath, data={1.0: 1.0})

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


### xmldumpstr ###

# 1. Xml Dump Str - Type Checks
def test1_exceptions_xmldumpstr_types():
    # Build Data
    xml_data = maci.xmlloadstr('<data>xml_data</data>')

    # Tests
    with pytest.raises(maci.error.XmlDumpStr):
        maci.xmldumpstr(data=1.0)
    with pytest.raises(maci.error.XmlDumpStr):
        maci.xmldumpstr(data=xml_data, encoding=1.0)


# 2. Xml Dump Str - Unsupported Options or Data
def test2_exceptions_xmldumpstr_opts_data():
    # Build Data
    xml_data = maci.xmlloadstr('<data>xml_data</data>')

    # Tests
    with pytest.raises(maci.error.XmlDumpStr):
        maci.xmldumpstr(data=xml_data, encoding='')


### xmldumpstrdict ###

# 1. Xml Dump Str Dict - Type Checks
def test1_exceptions_xmldumpstrdict_types():
    # Build Data
    xml_data = maci.xmlloadstrdict('<data>xml_data</data>')

    # Tests
    with pytest.raises(maci.error.XmlDumpStrDict):
        maci.xmldumpstrdict(data=1.0)
    with pytest.raises(maci.error.XmlDumpStrDict):
        maci.xmldumpstrdict(data=xml_data, pretty=1.0)
    with pytest.raises(maci.error.XmlDumpStrDict):
        maci.xmldumpstrdict(data=xml_data, full_doc=1.0)


# 2. Xml Dump Str Dict - Unsupported Options or Data
def test2_exceptions_xmldumpstrdict_opts_data():
    # Build Data
    xml_data = maci.xmlloadstrdict('<data>xml_data</data>')

    # Tests
    with pytest.raises(maci.error.XmlDumpStrDict):
        maci.xmldumpstrdict(data={1.0: 1.0})



### xmlload ###

# 1. Xml Load - Type Checks
def test1_exceptions_xmlload_types():
    # Tests
    with pytest.raises(maci.error.XmlLoad):
        maci.xmlload(filename=1.0)
    with pytest.raises(maci.error.XmlLoad):
        maci.xmlload(filename='', auto_get_root=1.0)


# 2. Xml Load - Unsupported Options or Data
def test2_exceptions_xmlload_opts_data():
    filepath = test_file_path + 'exc_xmlload.xml'

    # Tests
    with pytest.raises(maci.error.XmlLoad):
        maci.xmlload(filename='')
    with pytest.raises(maci.error.XmlLoad):
        maci.xmlload(filename=filepath)


### xmlloaddict ###

# 1. Xml Load Dict - Type Checks
def test1_exceptions_xmlloaddict_types():
    # Tests
    with pytest.raises(maci.error.XmlLoadDict):
        maci.xmlloaddict(filename=1.0)


# 2. Xml Load Dict - Unsupported Options or Data
def test2_exceptions_xmlloaddict_opts_data():
    filepath = test_file_path + 'exc_xmlload.xml'
    filepath_valid = '1_export_str_data.xml'

    # Tests
    with pytest.raises(maci.error.XmlLoadDict):
        maci.xmlloaddict(filename='')
    with pytest.raises(maci.error.XmlLoadDict):
        maci.xmlloaddict(filename=filepath)


### xmlloadstr ###

# 1. Xml Load Str - Type Checks
def test1_exceptions_xmlloadstr_types():
    # Tests
    with pytest.raises(maci.error.XmlLoadStr):
        maci.xmlloadstr(xml_str_data=1.0)


# 2. Xml Load Str - Unsupported Options or Data
def test2_exceptions_xmlloadstr_opts_data():
    # Tests
    with pytest.raises(maci.error.XmlLoadStr):
        maci.xmlloadstr(xml_str_data='')


### xmlloadstrdict ###

# 1. Xml Load Str Dict - Type Checks
def test1_exceptions_xmlloadstrdict_types():
    # Tests
    with pytest.raises(maci.error.XmlLoadStrDict):
        maci.xmlloadstrdict(xml_str_data=1.0)


# 2. Xml Load Str Dict - Unsupported Options or Data
def test2_exceptions_xmlloadstrdict_opts_data():
    # Tests
    with pytest.raises(maci.error.XmlLoadStrDict):
        maci.xmlloadstrdict(xml_str_data='')
