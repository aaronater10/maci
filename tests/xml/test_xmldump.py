# xmldump - Tests
from src import maci
from os import remove, path
import time
import xml.etree.ElementTree as __xml_etree

test_file_path = './tests/test_files/xml/'
file_delay_timer = 0.25


################################################################
# TESTS

# 1. XML Data Export - Exporting xml file data and test attributes
def test1_xml_file_export():
    filename = '1_export_file_data.xml'
    filepath = test_file_path + filename
    xml_data_str = """<test_root test_attr="attr_value">
    <dummy_data>Dummy Name 1</dummy_data>
    <dummy_data>Dummy Name 2</dummy_data>
    <dummy_data>Dummy Name 3</dummy_data>
    <dummy_data>Dummy Name 4</dummy_data>
    <dummy_data>Dummy Name 5</dummy_data>
    <dummy_data>Dummy Name 6</dummy_data>
    <dummy_data>Dummy Name 7</dummy_data>
    <dummy_data>Dummy Name 8</dummy_data>
    <dummy_data>Dummy Name 9</dummy_data>
    <dummy_data>Dummy Name 10</dummy_data>
    <dummy_data>Dummy Name 11</dummy_data>
    <dummy_data>Dummy Name 12</dummy_data>
    <dummy_data>Dummy Name 13</dummy_data>
    <dummy_data>Dummy Name 14</dummy_data>
</test_root>
"""
    xml_data_build = maci.xmlloadstr(xml_data_str)
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Test Not Exist, Create, Exist, test data and it's Type
    assert not path.exists(filepath)
    maci.xmldump(filepath, xml_data_build)
    assert path.exists(filepath)
    file_import = maci.xmlload(filepath)

    # Test - ElementTree Load/Dump
    file_import_tree = maci.xmlload(filepath, auto_get_root=False)
    maci.xmldump(filepath, file_import_tree)

    # Root Attrib
    assert (file_import.attrib['test_attr'] == "attr_value") and isinstance(file_import, __xml_etree.Element)
    # Sub Elements
    valid_sub_element_count = 14
    i = 0
    for element in file_import.findall('dummy_data'):
        i += 1
        assert (element.text == f"Dummy Name {i}") and isinstance(element, __xml_etree.Element)
    assert i == valid_sub_element_count

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
