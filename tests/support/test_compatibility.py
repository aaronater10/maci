# compatibility - Tests
from src import maci
import pytest

'''
This is to test backwards compatibility to old, but still supported, names from sfcparse
'''

################################################################
# Tests

# 1. Test all prior Function attr names from 'sfcparse'
def test1_prior_function_names():
    # Native
    maci.importfile
    maci.importfileraw
    maci.importattrs
    maci.exportfile
    with pytest.raises(maci.error.GeneralError):
        maci.appendfile # appendfile name not supported
    maci.savefile
    maci.builddata
    # JSON
    maci.jsonimportfile
    maci.jsonimportstr
    maci.jsonexportfile
    maci.jsonexportstr
    # YAML
    maci.yamlimportfile
    maci.yamlimportstr
    maci.yamlexportfile
    maci.yamlexportstr
    # INI
    maci.iniimportfile
    maci.iniexportfile
    # XML
    maci.xmlimportfile
    maci.xmlimportstr
    maci.xmlexportfile
    maci.xmlexportstr        

# 2. Test all prior Exception names from 'sfcparse'
def test2_prior_exception_names():
    # Native
    maci.error.ImportFile
    maci.error.ImportFileRaw
    maci.error.ImportAttrs
    maci.error.SaveFile
    maci.error.ExportFile
    maci.error.AppendFile
    # JSON
    maci.error.JsonImportFile
    maci.error.JsonImportStr
    maci.error.JsonExportFile
    maci.error.JsonExportStr
    # YAML
    maci.error.YamlImportFile
    maci.error.YamlImportStr
    maci.error.YamlExportFile
    maci.error.YamlExportStr
    # INI
    maci.error.IniImportFile
    maci.error.IniExportFile
    # XML
    maci.error.XmlImportFile
    maci.error.XmlImportStr
    maci.error.XmlExportFile
    maci.error.XmlExportStr
