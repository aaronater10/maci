# loaddict - Tests
from src import maci
import pytest
from os import path, remove
import time

test_file_path = './tests/test_files/native/loaddict_files/'
file_delay_timer = 0.25

################################################################
# TESTS
def test1_loadict_file_import():
    filename = '1_loaddict_file_import.data'
    filepath = test_file_path + filename

    # File Import
    file_import = maci.loaddict(filepath)

    # Test Data
    assert file_import['data_str'] == "data"
    assert file_import['data_int'] == 1
    assert file_import['data_float'] == 1.0
    assert file_import['data_bool'] == True
    assert file_import['data_list'] == [1,2,3]
    assert file_import['data_dict'] == {'k1':1, 'k2':2, 'k3':3}
    assert file_import['data_tuple'] == (1,2,3)
    assert file_import['data_set'] == {1,2,3}
    assert file_import['data_none'] == None
    assert file_import['data_bytes'] == b'data'
    assert str(file_import['data_datetime']) == "2023-03-13 22:06:00"


def test2_loadict_attr_dedup_off_on():
    filename = '2_loaddict_attr_dedup_off_on.data'
    filepath = test_file_path + filename

    # ATTR DEDUP OFF: File Import
    file_import = maci.loaddict(filepath, attr_name_dedup=False)

    # Test Data
    assert file_import['data_str'] == "changed data"

     # ATTR DEDUP ON (Default): File Import
    with pytest.raises(maci.error.LoadDict):
        file_import = maci.loaddict(filepath)


# 3. Encoding: Dict - Test some common encoding types
def test3_loaddict_and_dump_dict_encodings():
    filename = '3_loaddict_and_dump_dict_encoding.data'
    filepath = test_file_path + filename
    encodings_to_test = {
        'utf-8',
        'utf-16',
        'utf-32',
        'ascii',
        'iso-8859-1',
        'cp1252',
    }

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)

    # Build Data
    file_data = {'key': 'data'}

    # Test Dump and Load with Various Encodings
    for encoding in encodings_to_test:
        maci.dump(filepath, file_data, encoding=encoding)
        time.sleep(file_delay_timer)
        file_import = maci.loaddict(filepath, encoding=encoding)

        # Test Section Data from File Load
        assert 'data' == file_import['key']

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
