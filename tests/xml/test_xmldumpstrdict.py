# xmldumpdict - Tests
from src import maci
import xmltodict

################################################################
# TESTS

# 1. XML Dump Str Dict - Exporting xml str data and test attributes
def test1_xmldumpstrdict_export_str():
    xml_data_build = {
        'dummy_root': {
            'dummy_data1': 'dummy_data1',
            'dummy_data2': 'dummy_data2',
            'dummy_data3': 'dummy_data3',
        }
    }    

    # Tests
    str_data = maci.xmldumpstrdict(data=xml_data_build)
    str_import = maci.xmlloadstrdict(str_data)
    

    assert str_import['dummy_root']['dummy_data1'] == 'dummy_data1'
    assert str_import['dummy_root']['dummy_data2'] == 'dummy_data2'
    assert str_import['dummy_root']['dummy_data3'] == 'dummy_data3'
