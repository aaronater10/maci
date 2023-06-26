# dumpraw - Tests
from src import maci
from os import path, remove
import time

test_file_path = './tests/test_files/native/dumpraw_files/'
file_delay_timer = 0.25


################################################################
# TESTS

# 1. Basic File Export - Exporting an Empty File
def test1_basic_file_export():
    filename = '1_empty.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Not Exist, Create, Exist
    assert not path.exists(filepath)
    maci.dumpraw(filepath)
    assert path.exists(filepath)
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. Data File Export - Exporting a File with Data
def test2_data_file_export():
    filename = '2_data_file.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Not Exist, Create, Exist, Data and it's Type
    assert not path.exists(filepath)
    maci.dumpraw(filepath, f"data = {data}")
    assert path.exists(filepath)
    file_import = maci.load(filepath)
    assert (file_import.data == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. Multi Data File Export - Exporting a File with Multiple Data
def test3_multi_data_file_export():
    filename = '3_multi_data_file.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}
    big_data = f"""\n\n# Comment
data_b1 = {data}
data_b2 = {data}
data_b3 = {data}
"""

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Not Exist, Create, Exist, Data and it's Type
    assert not path.exists(filepath)
    maci.dumpraw(filepath, f"data1 = {data}", f"\ndata2 = {data}", f"\ndata3 = {data}", big_data)
    assert path.exists(filepath)
    file_import = maci.load(filepath)
    assert (file_import.data1 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data1, dict))
    assert (file_import.data2 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data2, dict))
    assert (file_import.data3 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data3, dict))
    assert (file_import.data_b1 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_b1, dict))
    assert (file_import.data_b2 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_b2, dict))
    assert (file_import.data_b3 == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data_b3, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 4. Data Bytes Export - Exporting a file with bytes and validate character
def test4_data_bytes_export():
    filename = '4_data_bytes.data'
    filename_append = '4_data_bytes_append.data'
    filepath = test_file_path + filename
    filepath_append = test_file_path + filename_append
    data_bytes = b'\xC3\xA9'
    bytes_match = "é"

    # Remove Any Existing Test Files
    try:
        remove(filepath)
        remove(filepath_append)
    except: pass
    time.sleep(file_delay_timer)

    ### Write File ###
    # Test Not Exist, Create, Exist, Data and it's Type
    assert not path.exists(filepath)
    maci.dumpraw(filepath, data_bytes, byte_data=True)
    file_import = maci.loadraw(filepath, byte_data=True)
    assert (file_import.decode() == bytes_match) and (isinstance(file_import, bytes))

    ### Append File ###
    # Test Not Exist, Create, Exist, Data and it's Type
    assert not path.exists(filepath_append)
    maci.dumpraw(filepath_append)
    maci.dumpraw(filepath_append, data_bytes, append=True, byte_data=True)
    file_import = maci.loadraw(filepath_append, byte_data=True)
    assert (file_import.decode().strip() == bytes_match) and (isinstance(file_import, bytes))

    # Remove Test Files
    time.sleep(file_delay_timer)
    try:
        remove(filepath)
        remove(filepath_append)
    except: pass


# 5. Encoding: Raw - Test some common encoding types
def test5_dumpraw_and_loadraw_encodings():
    filename = '5_dumpraw_loadraw_file_encodings.data'
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
        maci.dumpraw(filepath, file_data, encoding=encoding)
        time.sleep(file_delay_timer)
        file_import = maci.loadraw(filepath, encoding=encoding)

        # Test Section Data from File Load
        assert "{'key': 'data'}" == file_import

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 6. Newline Separator
def test6_dumpraw_newline_sep_on_off():
    filename = '6_dumpraw_newline_sep.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests

    # ON: Newline Separator - Default ON
    maci.dumpraw(filepath, "data", [1,2,3])
    file_import = maci.loadraw(filepath)
    assert "data\n[1, 2, 3]" == file_import

    # OFF: Newline Separator
    maci.dumpraw(filepath, "data", [1,2,3], newline_sep=False)
    file_import = maci.loadraw(filepath)
    assert "data[1, 2, 3]" == file_import

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
