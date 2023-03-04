# build - Tests
from src import maci
from os import path, remove
import time
import unittest

test_file_path = './tests/test_files/native/builddata_files/'
file_delay_timer = 0.5

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
        with self.assertRaises(Exception): build_data.data_none = True
        self.assertEqual(build_data.data_none, None)


        # UNLOCKING
        build_data.unlock_attr('data_none')

        # Test Unlocking Attribute
        build_data.data_none = True
        self.assertEqual(build_data.data_none, True)
        
        # Test Unlocking Exception when already Unlocked
        with self.assertRaises(Exception): build_data.unlock_attr('data_none')
    
        
        # REFERENCE
        build_data.link_attr('data_none', 'data_list')

        # Test Attribute Reference
        self.assertEqual(build_data.data_none, [1,2,3])
        # Reset back to Normal
        build_data.data_none = None

        # REFERENCE LOCK
        build_data.link_attr('data_none', 'data_list')
        build_data.lock_attr('data_none')

        # Test Attribute Reference Value and Lock
        with self.assertRaises(Exception): build_data.data_none = True
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
        build_data.link_attr('data_list', 'data_dict')
        # Set
        build_data.link_attr('data_set', 'data_bool')
        build_data.lock_attr('data_set')
        maci.dump(filepath, build_data)

        # Test Importing Data
        file_import = maci.load(filepath)

        # Test Imported Data
        
        # Tuple
        with self.assertRaises(Exception): file_import.data_tuple = True
        self.assertEqual(file_import.data_tuple, (1,2,3))

        # Str
        with self.assertRaises(Exception): file_import.data_str = True
        self.assertEqual(file_import.data_str, "data")

        # List
        self.assertEqual(file_import.data_list, {'k1':1, 'k2':2, 'k3':3})

        # Set
        with self.assertRaises(Exception): file_import.data_set = False
        self.assertEqual(file_import.data_set, True)

        # Remove Test File
        time.sleep(file_delay_timer)
        try: remove(filepath)
        except: pass
