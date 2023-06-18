# xmldumpstr - Tests
from src import maci
from os import path

test_file_path = './tests/test_files/xml/'


################################################################
# TESTS

# 1. XML Data Export to Str - Exporting xml data to str and test attributes
def test1_xml_str_export():
    filename = '1_export_str_data.xml'
    filepath = test_file_path + filename
    xml_data_str_match = """<test_root test_attr="attr_value">
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
</test_root>"""

    # Test exist, data and it's Type    
    assert path.exists(filepath)
    file_import = maci.xmlload(filepath)
    xml_data_to_str = maci.xmldumpstr(file_import)

    assert (xml_data_to_str == xml_data_str_match) and (isinstance(xml_data_to_str, str))
