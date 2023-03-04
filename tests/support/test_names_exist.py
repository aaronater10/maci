# names - Tests
from src import maci


################################################################
# Tests

# 1. Test all Function attr names are present
def test1_function_names_exist():
    # Native
    maci.load
    maci.loadstr
    maci.loadraw
    maci.loadattrs
    maci.dump
    maci.dumpstr
    maci.dumpraw
    maci.cleanformat
    maci.build
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
def test2_exception_names_exist():
    # General
    maci.error.GeneralError
    # Native
    maci.error.Load
    maci.error.LoadStr
    maci.error.LoadRaw
    maci.error.LoadAttrs
    maci.error.Dump
    maci.error.DumpStr
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


# 3. Test all MaciDataObj method names are present
def test3_macidataobj_method_names_exist():
    maci_obj = maci.build() # tests build name as well

    # MaciDataObj Method Names
    maci_obj.lock_attr
    maci_obj.unlock_attr
    maci_obj.hard_lock_attr
    maci_obj.link_attr
    maci_obj.get_locked_list
    maci_obj.get_hard_locked_list
    maci_obj.get_all_links
