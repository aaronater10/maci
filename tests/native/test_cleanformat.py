# cleanformat - Tests
from src import maci
from os import path, remove
import time

test_file_path = './tests/test_files/native/cleanformat_files/'
file_delay_timer = 0.5


################################################################
# TESTS

# 1. Default Data Format - Formatting Data Cleanly
def test1_default_format_export():
    filename = '1_data_format.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Formatted Data then Export it and Read it
    data_formatted = maci.cleanformat(data)
    assert not path.exists(filepath)
    maci.dumpraw(filepath, f"data = {data_formatted}")
    assert path.exists(filepath)
    file_import = maci.load(filepath)
    assert (file_import.data == {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}) and (isinstance(file_import.data, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 2. Indent Change Format - Formatting Data with Different Indent Levels
def test2_indent_format_export():
    filename = '2_indent_format.data'
    filepath = test_file_path + filename
    data = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Formatted Data with Indent Change then Export it and Read it
    data_formatted1 = maci.cleanformat(data, 0)
    data_formatted2 = maci.cleanformat(data, 7)
    assert not path.exists(filepath)
    maci.dumpraw(filepath, f"data1 = {data_formatted1}")
    assert path.exists(filepath)
    maci.dumpraw(filepath, f"data2 = {data_formatted2}", append=True)
    file_import = maci.load(filepath)
    assert (file_import.data1 == {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}) and (isinstance(file_import.data1, dict))
    assert (file_import.data2 == {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}) and (isinstance(file_import.data2, dict))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 3. All Data Formats - Formatting All Accepted Data Cleanly
def test3_all_formats_export():
    filename = '3_all_data_format.data'
    filepath = test_file_path + filename
    data_dict = {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}
    data_list = [1,2,3,4,5]
    data_tuple = (1,2,3,4,5)
    data_set = {1, 2, 3, 4, 5}

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    # Test Formatted Data then Export it and Read it
    data_dict = maci.cleanformat(data_dict)
    data_list = maci.cleanformat(data_list)
    data_tuple = maci.cleanformat(data_tuple)
    data_set = maci.cleanformat(data_set)

    assert not path.exists(filepath)
    maci.dumpraw(filepath,
        f"data_dict = {data_dict}\n",
        f"data_list = {data_list}\n",
        f"data_tuple = {data_tuple}\n",
        f"data_set = {data_set}\n"
    )
    
    assert path.exists(filepath)
    file_import = maci.load(filepath)
    assert (file_import.data_dict == {'k1':1, 'k2':2, 'k3':3, 'k4':4, 'k5':5}) and (isinstance(file_import.data_dict, dict))
    assert (file_import.data_list == [1,2,3,4,5]) and (isinstance(file_import.data_list, list))
    assert (file_import.data_tuple == (1,2,3,4,5)) and (isinstance(file_import.data_tuple, tuple))
    assert (file_import.data_set == {1, 2, 3, 4, 5}) and (isinstance(file_import.data_set, set))
    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass