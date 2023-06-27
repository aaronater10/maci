# xmlbuildmanual - Tests
from src import maci
from os import remove, path
import time
import xml.etree.ElementTree as __xml_etree

test_file_path = './tests/test_files/xml/'
file_delay_timer = 0.25


################################################################
# TESTS

# 1. XML Buiild Data - Building xml data and test attributes
def test1_xml_build_manual():
    filename = '1_build_manual_data.xml'
    filepath = test_file_path + filename

    xml_build = maci.xmlbuildmanual()
    xml_tree_root = xml_build.Element("root_dummy")
    sub_ele = xml_build.SubElement(xml_tree_root, "sub_dummy_data")
    sub_ele.text = "Dummy Name"
    xml_tree_root.attrib = {'dummy_key': "dummy_value"}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    
    # Test data and it's Type
    xml_to_str_data = maci.xmldumpstr(xml_tree_root)
    xml_from_str_data = maci.xmlloadstr(xml_to_str_data)

    maci.xmldump(filepath, xml_from_str_data)
    time.sleep(file_delay_timer)
    file_import = maci.xmlload(filepath)

    # Root Element
    assert (file_import.attrib['dummy_key'] == "dummy_value") and isinstance(file_import, __xml_etree.Element)
    assert (file_import.tag == "root_dummy")
    # Sub Elements
    assert (file_import.find('sub_dummy_data').text == "Dummy Name") and isinstance(file_import.find('sub_dummy_data'), __xml_etree.Element)

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
