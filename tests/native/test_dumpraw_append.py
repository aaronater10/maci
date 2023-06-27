# dumpraw append - Tests
from src import maci
from os import path, remove
import time

test_file_path = './tests/test_files/native/appendfile_files/'
file_delay_timer = 0.25


################################################################
# TESTS

# 1. Basic File append - Appending an Empty File
def test1_basic_file_append():
    filename = '1_basic_file_append.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}

    # Remove Any Existing Test File, then Create New One
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)
    maci.dumpraw(filepath)
    assert path.exists(filepath)
    # Test Single Line Append and Verify
    maci.dumpraw(filepath, f"data = {data}", append=True)
    file_import = maci.load(filepath)
    assert (file_import.data == {'k1':1, 'k2':2, 'k3':3}) and (isinstance(file_import.data, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. Multi Data File Append - Appending a File with Multiple Data
def test2_multi_data_file_append():
    filename = '2_multi_data_file.data'
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
    assert not path.exists(filepath)
    maci.dumpraw(filepath)
    assert path.exists(filepath)
    # Test Multi Line Append and Verify
    maci.dumpraw(filepath, f"data1 = {data}", f"\ndata2 = {data}", f"\ndata3 = {data}", big_data, append=True)
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


# 3. Data Tamper File Append - Appending a File without Tampering with Data Already Present
def test3_data_tamper_file_append():
    filename = '3_data_tamper_file.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3}
    big_data = f"""# Comment
data_b1 = {data}
data_b2 = {data}
data_b3 = {data}"""

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)
    # Export File with "Present Data"
    maci.dumpraw(filepath, big_data)
    assert path.exists(filepath)
    # Test Append Without Tampering Present Data and Verify. Appending 3x Lines
    maci.dumpraw(filepath, f"data1 = {data}", f"data2 = {data}", f"data3 = {data}", append=True)
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


# 4. Newline Separator
def test4_dumpraw_newline_sep_on_off_append():
    filename = '6_dumpraw_newline_sep.data'
    filepath = test_file_path + filename

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)

    # Tests

    # ON: Newline Separator - Default ON
    maci.dumpraw(filepath) # create file
    maci.dumpraw(filepath, "data", [1,2,3], 1.0, append=True)
    file_import = maci.loadraw(filepath)
    assert "data\n[1, 2, 3]\n1.0" == file_import

    # OFF: Newline Separator
    maci.dumpraw(filepath) # re-create file
    maci.dumpraw(filepath, "data", [1,2,3], 1.0, newline_sep=False, append=True)
    file_import = maci.loadraw(filepath)
    assert "data[1, 2, 3]1.0" == file_import

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass
