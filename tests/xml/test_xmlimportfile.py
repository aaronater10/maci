# xmlload - Tests
from src import maci
import xml.etree.ElementTree as __xml_etree

test_file_path = './tests/test_files/xml/'


################################################################
# TESTS

# 1. XML Data Import - Importing xml file data and test attributes
def test1_xml_file_import():
    filename = '1_import_file_data.xml'
    filepath = test_file_path + filename

    # Test data and it's Type    
    file_import = maci.xmlload(filepath)

    # Root Attrib
    assert (file_import.attrib['test_attr'] == "attr_value") and isinstance(file_import, __xml_etree.Element)
    # Sub Elements
    valid_sub_element_count = 14
    i = 0
    for element in file_import.findall('dummy_data'):
        i += 1
        assert (element.text == f"Dummy Name {i}") and isinstance(element, __xml_etree.Element)
    assert i == valid_sub_element_count