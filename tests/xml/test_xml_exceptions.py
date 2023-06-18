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


### xmlload ###

# 1. Xml Load - Type Checks
def test1_exceptions_xmlload_types():
    # Tests
    with pytest.raises(maci.error.XmlLoad):
        maci.xmlload(filename=1.0)


# 2. Xml Load - Unsupported Options or Data
def test2_exceptions_xmlload_opts_data():
    # Tests
    with pytest.raises(maci.error.XmlLoad):
        maci.xmlload(filename='')
