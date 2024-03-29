# names - Tests
from src import maci


################################################################
# Tests

# 1. Test all Function attr names are present
def test1_function_names_exist():
    # Native
    maci.load
    maci.loadstr
    maci.loadstrdict
    maci.loadraw
    maci.loadattrs
    maci.loaddict
    maci.dump
    maci.dumpstr
    maci.dumpraw
    maci.cleanformat
    maci.build
    # HASH
    maci.createfilehash
    maci.comparefilehash
    maci.createhash
    # JSON
    maci.jsonload
    maci.jsonloadstr
    maci.jsondump
    maci.jsondumpstr
    # YAML
    maci.yamlload
    maci.yamlloadall
    maci.yamlloadstr
    maci.yamldump
    maci.yamldumpall
    maci.yamldumpstr
    # TOML
    maci.tomlload
    maci.tomlloadstr
    maci.tomldump
    maci.tomldumpstr
    # INI
    maci.iniload
    maci.inidump
    maci.inibuildauto
    maci.inibuildmanual
    # XML
    maci._defuse_xml_stdlib
    maci.xmlload
    maci.xmlloaddict
    maci.xmlloadstr
    maci.xmlloadstrdict
    maci.xmldump
    maci.xmldumpdict
    maci.xmldumpstr
    maci.xmldumpstrdict
    maci.xmlbuildmanual
    # PICKLE
    maci.pickledumpbytes
    maci.pickleloadbytes


# 2. Test all Exception attr names are present
def test2_exception_names_exist():
    # General
    maci.error.GeneralError
    # Hints
    maci.error.Hint
    # Native
    maci.error.Load
    maci.error.LoadStr
    maci.error.LoadStrDict
    maci.error.LoadRaw
    maci.error.LoadAttrs
    maci.error.LoadDict
    maci.error.Dump
    maci.error.DumpStr
    maci.error.DumpRaw
    maci.error.CleanFormat
    # HASH
    maci.error.CreateFileHash
    maci.error.CompareFileHash
    maci.error.CreateHash
    # JSON
    maci.error.JsonLoad
    maci.error.JsonLoadStr
    maci.error.JsonDump
    maci.error.JsonDumpStr
    # YAML
    maci.error.YamlLoad
    maci.error.YamlLoadAll
    maci.error.YamlLoadStr
    maci.error.YamlDump
    maci.error.YamlDumpAll
    maci.error.YamlDumpStr
    # TOML
    maci.error.TomlLoad
    maci.error.TomlLoadStr
    maci.error.TomlDump
    maci.error.TomlDumpStr
    # INI
    maci.error.IniLoad
    maci.error.IniDump
    maci.error.IniBuildAuto
    # XML
    maci.error.XmlLoad
    maci.error.XmlLoadDict
    maci.error.XmlLoadStr
    maci.error.XmlLoadStrDict
    maci.error.XmlDump
    maci.error.XmlDumpDict
    maci.error.XmlDumpStr
    maci.error.XmlDumpStrDict
    # PICKLE
    maci.error.PickleDumpBytes
    maci.error.PickleLoadBytes


# 3. Test all MaciDataObj method names are present
def test3_macidataobj_method_names_exist():
    maci_obj = maci.build() # tests build name as well

    # MaciDataObj Method Names
    maci_obj.lock_attr
    maci_obj.unlock_attr
    maci_obj.hard_lock_attr
    maci_obj.map_attr
    maci_obj.unmap_attr
    maci_obj.get_attrs
    maci_obj.get_locked_list
    maci_obj.get_hard_locked_list
    maci_obj.get_all_maps
    maci_obj.get_parent_maps
    maci_obj.get_child_maps
    maci_obj.get_parent_map_chains
    maci_obj.load_attrs
    maci_obj.is_parent_map
    maci_obj.is_child_map
