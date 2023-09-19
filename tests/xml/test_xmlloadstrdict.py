# xmlloadstrdict - Tests
from src import maci

test_file_path = './tests/test_files/xml/'


################################################################
# TESTS

# 1. XML Data Import Dict - Importing xml file data and test values
def test1_xml_load_str_dict():
    xml_data = """\
<test_root test_attr="attr_value">
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
   
    # Tests
    str_import = maci.xmlloadstrdict(xml_data)
    print(str_import)

    for idx,element_data in enumerate(str_import['test_root']['dummy_data'], start=1):
        assert (element_data == f"Dummy Name {idx}")

