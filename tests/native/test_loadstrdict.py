# loadstrdict - Tests
from src import maci
import pytest
import datetime

test_file_path = './tests/test_files/native/loadstrdict_files/'

################################################################
# TESTS

# 1. Load Str Dict - Test loading attrs from string
def test1_loadstrdict_str_import():
    filename = '1_loadstrdict_str_import.data'
    filepath = test_file_path + filename
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

    # String Import
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstrdict(str_data)

    # Test Data
    assert matched_data == str_import
    assert str_import['data_str'] == "data"
    assert str_import['data_int'] == 1
    assert str_import['data_float'] == 1.0
    assert str_import['data_bool'] == True
    assert str_import['data_list'] == [1,2,3]
    assert str_import['data_dict'] == {'k1':1, 'k2':2, 'k3':3}
    assert str_import['data_tuple'] == (1,2,3)
    assert str_import['data_set'] == {1,2,3}
    assert str_import['data_none'] == None
    assert str_import['data_bytes'] == b'data'
    assert str(str_import['data_datetime']) == "2023-03-13 22:06:00"

    # Unique Objects
    assert maci.loadstrdict(str_data) is not maci.loadstrdict(str_data)


# 2. Load Str Dict: Attr Dedup - Test Attr Dedup OFF/ON
def test2_loadstrdict_attr_dedup_off_on():
    filename = '2_loadstrdict_attr_dedup_off_on.data'
    filepath = test_file_path + filename

    # ATTR DEDUP OFF (Default): String Import
    str_data = maci.loadraw(filepath)
    str_import = maci.loadstrdict(str_data)

    # Test Data
    assert str_import['data_str'] == "changed data"

     # ATTR DEDUP ON: File Import
    with pytest.raises(maci.error.LoadStrDict):
        maci.loadstrdict(str_data, attr_name_dedup=True)


# 3. Load Str Dict: Attr Dedup - Test Attr Dedup OFF/ON
def test3_loadstrdict_returns_none():
    # Tests
    assert maci.loadstrdict('') == dict()
