# pickledumpbytes - Tests
from src import maci

################################################################
# TESTS

# 1. PICKLE Dump Bytes - Dumping pickle byte data and test attributes
def test1_pickledumpbytes_data():
    pickle_data = {
    'string_data': 'data',
    'int_data': 256,
    'float_data': 1.7,
    'array_data': [1,2,3],
    'bool_data': True,
    'section': {'sub_section': {'string_data': 'data', 'int_data': 256}}
    }

    # Load and test data
    pickle_byte_data = maci.pickledumpbytes(pickle_data)
    pickle_import = maci.pickleloadbytes(pickle_byte_data)

    assert pickle_import['string_data'] == 'data'
    assert pickle_import['int_data'] == 256
    assert pickle_import['float_data'] == 1.7
    assert pickle_import['array_data'] == [1,2,3]
    assert pickle_import['bool_data'] == True
    assert pickle_import['section']['sub_section'] == {'string_data': 'data', 'int_data': 256}
