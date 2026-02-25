# loaddict - Tests
from src import maci
import pytest
from os import path, remove
import time
import datetime

test_file_path = './tests/test_files/native/loaddict_files/'
file_delay_timer = 0.25

################################################################
# TESTS

# 1. Load Dict - Test loading attrs from file
def test1_loaddict_file_imports():
    filename = '1_loaddict_file_import.data'
    filename_empty = '1_loaddict_file_import_empty.data'
    filepath = test_file_path + filename
    filepath_empty = test_file_path + filename_empty
    matched_data = {
        'data_str': 'data',
        'data_int': 1,
        'data_float': 1.0,
        'data_bool': True,
        'data_list': [
            1,
            2,
            3,
        ],
        'data_dict': {
            'k1': 1,
            'k2': 2,
            'k3': 3,
        },
        'data_tuple': (
            1,
            2,
            3,
        ),
        'data_set': {
            1,
            2,
            3,
        },
        'data_none': None,
        'data_bytes': b'data',
        'data_datetime': datetime.datetime(2023, 3, 13, 22, 6),
    }

    # File Import
    file_import = maci.loaddict(filepath)

    # Test Data
    assert matched_data == file_import
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

    ### Empty Import ###
    assert maci.loaddict(filename=filepath_empty) == dict()

    # Unique Objects
    assert maci.loaddict(filepath) is not maci.loaddict(filepath)

# 2. Load Dict: Attr Dedup - Test Attr Dedup OFF/ON
def test2_loaddict_attr_dedup_off_on():
    filename = '2_loaddict_attr_dedup_off_on.data'
    filepath = test_file_path + filename

    # ATTR DEDUP OFF (Default): File Import
    file_import = maci.loaddict(filepath)

    # Test Data
    assert file_import['data_str'] == "changed data"

     # ATTR DEDUP ON: File Import
    with pytest.raises(maci.error.LoadDict):
        file_import = maci.loaddict(filepath, attr_name_dedup=True)


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
