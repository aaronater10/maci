# xmlloadstr - Tests
from src import maci
import xml.etree.ElementTree as __xml_etree

################################################################
# TESTS

# 1. XML Data Import Str - Importing xml str data and test attributes
def test1_xml_str_import():
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
    # Test data and it's Type    
    xml_str_import = maci.xmlloadstr(xml_data_str)

    # Root Attrib
    assert (xml_str_import.attrib['test_attr'] == "attr_value") and isinstance(xml_str_import, __xml_etree.Element)
    # Sub Elements
    valid_sub_element_count = 14
    i = 0
    for element in xml_str_import.findall('dummy_data'):
        i += 1
        assert (element.text == f"Dummy Name {i}") and isinstance(element, __xml_etree.Element)
    assert i == valid_sub_element_count