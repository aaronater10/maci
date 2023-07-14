# build - Tests
from src import maci
from os import path, remove
import time
import unittest

test_file_path = './tests/test_files/native/builddata_files/'
file_delay_timer = 0.25

################################################################
'''
NOTICE:
- Any new tests must not use the unittest class and instead use the pytest framework if needed.
- Add new tests below the "TestBuildData" class
- Old tests are still being used/kept to reference consistent functionality
- Ensure to still continue to number tests in order, or what makes sense for the type of test category
'''
################################################################


################################################################
# TESTS

class TestBuildData(unittest.TestCase):

    # 1. Build Data - Testing raw data build storing to file and importing
    def test1_build_data_maci(self):
        filename = '1_build_data_maci.data'
        filepath = test_file_path + filename

        # Build Data
        build_data = maci.build()
        build_data.data_str = "data"
        build_data.data_int = 1
        build_data.data_float = 1.0
        build_data.data_bool = True
        build_data.data_list = [1,2,3]
        build_data.data_dict = {'k1':1, 'k2':2, 'k3':3}
        build_data.data_tuple = (1,2,3)
        build_data.data_set = {1,2,3}
        build_data.data_none = None
        build_data.data_bytes = b'data'

        # Store Data
        maci.dump(filepath, build_data)

        # Test Importing Data
        file_import = maci.load(filepath)

        # Test Imported Data
        self.assertEqual(file_import.data_str, "data")
        self.assertEqual(file_import.data_int, 1)
        self.assertEqual(file_import.data_float, 1.0)
        self.assertEqual(file_import.data_bool, True)
        self.assertEqual(file_import.data_list, [1,2,3])
        self.assertEqual(file_import.data_dict, {'k1':1, 'k2':2, 'k3':3})
        self.assertEqual(file_import.data_tuple, (1,2,3))
        self.assertEqual(file_import.data_set, {1,2,3})
        self.assertEqual(file_import.data_none, None)
        self.assertEqual(file_import.data_bytes, b'data')

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

    # 2. Build Data - Testing raw data build and method concepts, storing to file and importing method retention
    def test2_build_data_methods_maci(self):
        filename = '2_build_data_methods_maci.data'
        filepath = test_file_path + filename

        # Build Data
        build_data = maci.build()
        build_data.data_str = "data"
        build_data.data_int = 1
        build_data.data_float = 1.0
        build_data.data_bool = True
        build_data.data_dict = {'k1':1, 'k2':2, 'k3':3}
        build_data.data_list = [1,2,3]
        build_data.data_tuple = (1,2,3)
        build_data.data_set = {1,2,3}
        build_data.data_none = None
        build_data.data_bytes = b'data'

        # LOCKING
        build_data.lock_attr('data_none')

        # Test Locked Attribute
        with self.assertRaises(maci.error.MaciError): build_data.data_none = True
        self.assertEqual(build_data.data_none, None)


        # UNLOCKING
        build_data.unlock_attr('data_none')

        # Test Unlocking Attribute
        build_data.data_none = True
        self.assertEqual(build_data.data_none, True)
        
        # Test Unlocking Exception when already Unlocked
        with self.assertRaises(maci.error.MaciError): build_data.unlock_attr('data_none')
    
        
        # REFERENCE
        build_data.map_attr('data_none', 'data_list')

        # Test Attribute Reference
        self.assertEqual(build_data.data_none, [1,2,3])
        # Reset back to Normal
        build_data.data_none = None

        # REFERENCE LOCK
        build_data.map_attr('data_none', 'data_list')
        build_data.lock_attr('data_none')

        # Test Attribute Reference Value and Lock
        with self.assertRaises(maci.error.MaciError): build_data.data_none = True
        self.assertEqual(build_data.data_none, [1,2,3])
        # Reset back to Normal
        build_data.unlock_attr('data_none')
        build_data.data_none = None


        # Save and Import Mixed Setups
        # Setup Different Locked and Reference Locked Values, Unlock a value from file import as well
        
        # Tuple
        build_data.lock_attr('data_tuple')
        # Str
        build_data.lock_attr('data_str')
        # List
        build_data.map_attr('data_list', 'data_dict')
        # Set
        build_data.map_attr('data_set', 'data_bool')
        build_data.lock_attr('data_set')
        maci.dump(filepath, build_data)

        # Test Importing Data
        file_import = maci.load(filepath)

        # Test Imported Data
        
        # Tuple
        with self.assertRaises(maci.error.MaciError): file_import.data_tuple = True
        self.assertEqual(file_import.data_tuple, (1,2,3))

        # Str
        with self.assertRaises(maci.error.MaciError): file_import.data_str = True
        self.assertEqual(file_import.data_str, "data")

        # List
        self.assertEqual(file_import.data_list, {'k1':1, 'k2':2, 'k3':3})

        # Set
        with self.assertRaises(maci.error.MaciError): file_import.data_set = False
        self.assertEqual(file_import.data_set, True)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass

### END OF OLD TESTS ###
################################################################
# SEE AT TOP ABOVE FOR THIS
################################################################
### NEW TESTS BELOW ###

# 3. Test MaciDataObj Bool from Empty or With Data
def test3_build_data_maciobj_bool():
    # Build Data
    maci_data = maci.build()

    # Tests
    
    # Empty Object
    assert bool(maci_data) == False

    # Object has data
    maci_data.data_str = 'data'
    assert bool(maci_data) == True


# 4. Test MaciDataObj EQ Comparison
def test4_build_data_maciobj_eq():
    # Build Data
    maci_data = maci.build()

    # Tests
    
    # Equal Objects: both empty
    assert (maci_data == maci.build()) == True

    # Unequal Objects: one has data
    maci_data.data_str = 'data'
    assert (maci_data == maci.build()) == False

    # Unlike Objects: 2 different object types compared
    assert (maci_data == []) == False

# 5. Test MaciDataObj dir
def test5_build_data_maciobj_dir():
    # Build Data
    maci_data = maci.build()

    # Tests
    assert isinstance(dir(maci_data), list)


# 6. Test MaciDataObj dir - test can pull value with getattr
def test6_build_data_maciobj_getattr():
    # Build Data
    maci_data = maci.build()
    maci_data.d1 = 'data'

    # Tests
    assert getattr(maci_data, 'd1') == 'data'
