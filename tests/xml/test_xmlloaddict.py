# xmlloaddict - Tests
from src import maci

test_file_path = './tests/test_files/xml/'


################################################################
# TESTS

# 1. XML Data Import Dict - Importing xml file data and test values
def test1_xml_load_dict():
    filename = '1_import_file_data.xml'
    filepath = test_file_path + filename
   
    # Tests
    file_import = maci.xmlloaddict(filepath)
    print(file_import)

    for idx,element_data in enumerate(file_import['test_root']['dummy_data'], start=1):
        assert (element_data == f"Dummy Name {idx}")

