# xmldumpdict - Tests
from src import maci
from os import remove, path
import time
import xmltodict

test_file_path = './tests/test_files/xml/'
file_delay_timer = 0.25

################################################################
# TESTS

# 1. XML Dump Dict - Exporting xml file data and test attributes
def test1_xmldumpdict_export_file():
    filename = '1_xmldumpdict_data.xml'
    filepath = test_file_path + filename
    xml_data_build = {
        'dummy_root': {
            'dummy_data1': 'dummy_data1',
            'dummy_data2': 'dummy_data2',
            'dummy_data3': 'dummy_data3',
        }
    }
    
    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    maci.xmldumpdict(filename=filepath, data=xml_data_build)
    file_import = maci.xmlloaddict(filename=filepath)

    assert file_import['dummy_root']['dummy_data1'] == 'dummy_data1'
    assert file_import['dummy_root']['dummy_data2'] == 'dummy_data2'
    assert file_import['dummy_root']['dummy_data3'] == 'dummy_data3'

    # # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
