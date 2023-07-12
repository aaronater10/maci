# loadattrs - Tests
from src import maci
import unittest
import pytest
from os import path, remove
import time

test_file_path = './tests/test_files/native/loadattrs_files/'
file_delay_timer = 0.25

################################################################
'''
NOTICE:
- Any new tests must not use the unittest class and instead use the pytest framework if needed.
- Add new tests below the "TestLoadAttrs" class
- Old tests are still being used/kept to reference consistent functionality
- Ensure to still continue to number tests in order, or what makes sense for the type of test category
'''
################################################################


################################################################
# TESTS

class TestLoadAttrs(unittest.TestCase):

    # 1. Importing Attrs - Testing importing attributes from file to Custom Class / New Class
    def test1_import_attrs_class(self):
        filename = '1_import_attrs_class.data'
        filepath = test_file_path + filename

        # Test Data Custom Class
        class TemplateData:
            def __init__(self) -> None:
                self.data_list = [1,2,3]
                self.data_bool = True
                self.data_int = 1
        class_data = TemplateData()

        class NewObjData: pass

        # Original Class
        # Update Values to Simulate Restore from Original to Prove Import
        class_data.data_bool = False
        class_data.data_list.append(4)
        class_data.data_int = 2

        # Test Importing Attrs Back
        maci.loadattrs(filepath, class_data)

        # Test Imported Data of their Original Values Stored
        self.assertEqual(class_data.data_list, [1,2,3])
        self.assertEqual(class_data.data_bool, True)
        self.assertEqual(class_data.data_int, 1)

        # Instance Object
        # Test Importing Attrs to New Object
        new_class_data = NewObjData()
        maci.loadattrs(filepath, new_class_data)

        # Test Imported Data of their Original Values Stored from Instance
        self.assertEqual(new_class_data.data_list, [1,2,3])
        self.assertEqual(new_class_data.data_bool, True)
        self.assertEqual(new_class_data.data_int, 1)

        # Root Class
        # Test Importing Attrs to Root Class Object
        maci.loadattrs(filepath, NewObjData)

        # Test Imported Data of their Original Values Stored from Root Class
        self.assertEqual(NewObjData.data_list, [1,2,3])
        self.assertEqual(NewObjData.data_bool, True)
        self.assertEqual(NewObjData.data_int, 1)


### END OF OLD TESTS ###
################################################################
# SEE AT TOP ABOVE FOR THIS
################################################################
### NEW TESTS BELOW ###

# 2. Load Attrs: Attr Dedup - Test Attr Dedup ON/OFF
def test2_loadattrs_attr_dedup_on_off():
    filename = '2_loadattrs_attr_dedup_on_off.data'
    filepath = test_file_path + filename

    # Data Custom Class
    class TemplateData:
        def __init__(self) -> None:
            ...
    class_data = TemplateData()

    # ATTR DEDUP OFF (Off by Default): File Import
    maci.loadattrs(filepath, class_data)

    # Test Data
    assert class_data.data_str == "changed data"

     # ATTR DEDUP ON (Default): File Import
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filepath, class_data, attr_name_dedup=True)


# 3. Encoding: Load Attrs - Test some common encoding types
def test3_loadattrs_and_dump_encodings():
    filename = '3_loadattrs_and_dump_encoding.data'
    filepath = test_file_path + filename
    encodings_to_test = {
        'utf-8',
        'utf-16',
        'utf-32',
        'ascii',
        'iso-8859-1',
        'cp1252',
    }

    # Dump: Data Custom Class
    class TemplateDataDump:
        def __init__(self) -> None:
            self.key = 'data'
    class_data_dump = TemplateDataDump()

    # Load: Data Custom Class
    class TemplateDataLoad:
        def __init__(self) -> None:
            self.key = 'data'
    class_data_load = TemplateDataLoad()

    # Remove Any Existing Test File
    try: remove(filepath)
    except: pass
    time.sleep(file_delay_timer)
    assert not path.exists(filepath)

    # Test Dump and Load with Various Encodings
    for encoding in encodings_to_test:
        maci.dump(filepath, class_data_dump, encoding=encoding)
        time.sleep(file_delay_timer)
        maci.loadattrs(filepath, class_data_load, encoding=encoding)

        # Test Section Data from File Load
        assert 'data' == class_data_load.key

    # Remove Test File
    time.sleep(file_delay_timer)
    try: remove(filepath)
    except: pass


# 4. Check behavior of internal method check - Test with it ON/OFF
def test4_loadattrs_internal_method_check_off_on():
    from datetime import datetime, date, time
    filename_no_spaces = '4_loadattrs_internal_method_check_off_on.data'
    filepath = test_file_path + filename_no_spaces

    # Data Custom Class
    class TemplateData:
        def __init__(self) -> None:
            ...
    class_data = TemplateData()

    # OFF (Off by Default): File Import - All Attrs Import
    maci.loadattrs(filepath, class_data)

    # Test Attrs
    assert class_data.map_attr == [1,2,3]
    assert class_data.lock_attr == [1,2,3]
    assert class_data.data_str == 'data'
    assert class_data.data_int == 1

    # ON: File Import - Raise Exception
    with pytest.raises(maci.error.LoadAttrs):
        maci.loadattrs(filepath, class_data, _ignore_maci_attr_check=False)
