# names - Tests
from src import maci
import unittest


################################################################
# TESTS

class TestNamesExist(unittest.TestCase):

    # 1. Test all Function attr names are present
    def test1_function_names_exist(self):
        # Native
        maci.load
        maci.loadstr
        maci.loadraw
        maci.loadattrs
        maci.dump
        maci.dumpraw
        maci.cleanformat
        maci.builddata
        # HASH
        maci.createfilehash
        maci.comparefilehash
        # JSON
        maci.jsonload
        maci.jsonloadstr
        maci.jsondump
        maci.jsondumpstr
        # YAML
        maci.yamlload
        maci.yamlloadstr
        maci.yamldump
        maci.yamldumpstr
        # INI
        maci.iniload
        maci.inidump
        maci.inibuildauto
        maci.inibuildmanual
        # XML
        maci.xmlload
        maci.xmlloadstr
        maci.xmldump
        maci.xmldumpstr
        maci.xmlbuildmanual    

    # 2. Test all Exception attr names are present
    def test2_exception_names_exist(self):
        # General
        maci.error.GeneralError
        # Native
        maci.error.Load
        maci.error.LoadStr
        maci.error.LoadRaw
        maci.error.LoadAttrs
        maci.error.Dump
        maci.error.DumpRaw
        maci.error.CleanFormat
        # HASH
        maci.error.CreateFileHash
        maci.error.CompareFileHash
        # JSON
        maci.error.JsonLoad
        maci.error.JsonLoadStr
        maci.error.JsonDump
        maci.error.JsonDumpStr
        # YAML
        maci.error.YamlLoad
        maci.error.YamlLoadStr
        maci.error.YamlDump
        maci.error.YamlDumpStr
        # INI
        maci.error.IniLoad
        maci.error.IniDump
        maci.error.IniBuildAuto
        # XML
        maci.error.XmlLoad
        maci.error.XmlLoadStr
        maci.error.XmlDump
        maci.error.XmlDumpStr
