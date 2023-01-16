# loadattrs - Tests
from src import maci
import unittest

test_file_path = './tests/test_files/native/loadattrs_files/'

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
