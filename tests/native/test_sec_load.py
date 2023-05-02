# load - Security Tests
from src import maci
import unittest

test_file_path = './tests/test_files/native/sec_load_files/'


################################################################
# SECURITY TESTS

# 1. Value in Var Import - Importing Config File with a Value that is Code Executable
class Test1CodeNotExec(unittest.TestCase):

    def test1_code_notexec_import(self):
        filename = '1_code_notexec.data'
        filepath = test_file_path + filename
        with self.assertRaises(maci.error.MaciError):
            maci.load(filepath)


# 2. Code on Line Import - Importing Config File with a Line in File that contains Executable Code
class Test2CodeNotExec(unittest.TestCase):

    def test2_code_notexec_import(self):
        filename = '2_code_notexec.data'
        filepath = test_file_path + filename
        with self.assertRaises(maci.error.MaciError):
            maci.load(filepath)


# 3. Single-Line Attribute Protect - Halting Import of Config File with Duplicate Attributes
class Test3SingleAttrProtect(unittest.TestCase):

    def test3_single_attr_protect(self):
        filename = '3_singleline_attr_protect.data'
        filepath = test_file_path + filename
        with self.assertRaises(maci.error.MaciError):
            maci.load(filepath)


# 4. Multi-Line Attribute Protect - Halting Import of Config File with Duplicate Attributes
class Test4MultiAttrProtect(unittest.TestCase):

    def test4_multi_attr_protect(self):
        filename = '4_multiline_attr_protect.data'
        filepath = test_file_path + filename
        with self.assertRaises(maci.error.MaciError):
            maci.load(filepath)
