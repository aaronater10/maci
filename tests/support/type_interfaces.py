"""
This test is to be ran by a type checker to evaluate correct types being
used from input/output within the API interface functions and methods
"""
from typing import Optional
from typing import Union
from typing import Any
from typing import Dict
from typing import List
from types import ModuleType
from src import maci

### Data for Tests ###
class MyClass: ...

################################################################
# Functions

### Native ###
build: maci.hint.MaciDataObj = maci.build()
load: maci.hint.MaciDataObj = maci.load(
    filename='',
    attr_name_dedup=True, 
    encoding=None, 
    _ignore_maci_attr_check=False
)
maci.loadattrs(
    filename='',
    class_object=MyClass(),
    encoding=None, 
    attr_name_dedup=True, 
    _ignore_maci_attr_check=True
)
loaddict: dict = maci.loaddict(
    filename='',
    attr_name_dedup=True,
    encoding=None
)
loadraw: Union[str, bytes] = maci.loadraw(
    filename='',
    byte_data=False,
    encoding=None
)
loadstr: maci.hint.MaciDataObj = maci.loadstr(
    maci_str_data='',
    attr_name_dedup=True
)
loadstrdict: dict = maci.loadstrdict(
    maci_str_data='',
    attr_name_dedup=True
)
maci.dump(
    filename='',
    data=MyClass(),
    append=False,
    indent_level=1,
    indentation_on=True,
    multi_line_str=False,
    encoding=None,
    private_attrs=False,
    private_under_attrs=False,
    private_dunder_attrs=False,
    class_attrs=False,
    private_init_attrs=False,
    private_init_under_attrs=False,
    private_init_dunder_attrs=False,
    private_class_attrs=False,
    private_class_under_attrs=False,
    private_class_dunder_attrs=False,
    use_symbol_glyphs=False
)
maci.dumpraw(
    filename='',
    data=[],
    append=False,
    byte_data=False,
    newline_sep=True,
    encoding=None
)
dumpstr: Optional[str] = maci.dumpstr(
    data=MyClass(),
    indent_level=1,
    indentation_on=True,
    multi_line_str=False,
    private_attrs=False,
    private_under_attrs=False,
    private_dunder_attrs=False,
    class_attrs=False,
    private_init_attrs=False,
    private_init_under_attrs=False,
    private_init_dunder_attrs=False,
    private_class_attrs=False,
    private_class_under_attrs=False,
    private_class_dunder_attrs=False,
    use_symbol_glyphs=False
)
cleanformat: str = maci.cleanformat(
    data=[],
    indent_level=1
)

### Hash ###
comparefilehash: bool = maci.comparefilehash(
    file_to_hash='',
    stored_hash_file='',
    hash_algorithm='',
    encoding=None
)
createfilehash: str = maci.createfilehash(
    file_to_hash='',
    file_to_store_hash='',
    hash_algorithm='',
    encoding=None
)
createhash: str = maci.createhash(
    data_to_hash='',
    hash_algorithm='',
    encoding=''
)

### INI ###
inibuildauto: maci.hint.ConfigParser = maci.inibuildauto(
    data={'k': {'k': 1}}
)
inibuildmanual: maci.hint.ConfigParser = maci.inibuildmanual()
maci.inidump(
    filename='',
    data=maci.inibuildmanual(),
    append=False,
    encoding=None
)
iniload: maci.hint.ConfigParser = maci.iniload(
    filename='',
    encoding=None
)

### JSON ###
maci.jsondump(
    filename='',
    data={},
    append=False,
    indent_level=4,
    encoding=None
)
jsondumpstr: str = maci.jsondumpstr(
    data={},
    indent_level=4
)
jsonload: Union[list, dict, str, int, float, bool, None] = maci.jsonload(
    filename='',
    encoding=None
)
jsonloadstr: Union[list, dict, str, int, float, bool, None] = maci.jsonloadstr(
    json_str_data=''
)

### TOML ###
maci.tomldump(
    filename='',
    data={'k': 1},
    append=False,
    multi_line_str=False
)
tomldumpstr: str = maci.tomldumpstr(
    data={'k': 1},
    multi_line_str=False
)
tomlload: Dict[str, Any] = maci.tomlload(
    filename=''
)
tomlloadstr: Dict[str, Any] = maci.tomlloadstr(
    toml_str_data=''
)

### XML ###
xmlbuildmanual: ModuleType = maci.xmlbuildmanual()
maci.xmldump(
    filename='',
    data=maci.xmlloadstr(''),
    append=False,
    encoding=None
)
maci.xmldumpdict(
    filename='',
    data={},
    append=False,
    pretty=True,
    full_doc=True
)
xmldumpstr: str = maci.xmldumpstr(
    data=maci.xmlloadstr(''),
    encoding=''
)
xmldumpstrdict: str = maci.xmldumpstrdict(
    data={},
    pretty=True,
    full_doc=True
)
xmlload: Union[maci.hint.Element, maci.hint.ElementTree] = maci.xmlload(
    filename='',
    auto_get_root=True
)
xmlloaddict: dict = maci.xmlloaddict(
    filename='',
)
xmlloadstr: maci.hint.Element = maci.xmlloadstr(
    xml_str_data=''
)
xmlloadstrdict: dict = maci.xmlloadstrdict(
    xml_str_data=''
)
defuse_xml_stdlib: dict = maci._defuse_xml_stdlib()

### YAML ###
maci.yamldump(
    filename='',
    data={},
    append=False,
    encoding=None
)
yamldumpstr: str = maci.yamldumpstr(
    data={}
)
yamlload: Any = maci.yamlload(
    filename='',
    encoding=None
)
yamlloadstr: Any = maci.yamlloadstr(
    yaml_str_data=''
)


################################################################
# Methods
maci_data = maci.build()
get_all_maps: Dict[str, Dict[str, Any]] = maci_data.get_all_maps()
get_child_maps: Dict[str, str] = maci_data.get_child_maps()
get_hard_locked_list: List[str] = maci_data.get_hard_locked_list()
get_locked_list: List[str] = maci_data.get_locked_list()
get_parent_map_chains: Union[Dict[str, List[str]], List[str]] = maci_data.get_parent_map_chains(
    parent_attr=None,
    dup_link_check=True
)
get_parent_maps: Dict[str, Dict[str, str]] = maci_data.get_parent_maps()
maci_data.hard_lock_attr(attr_name='')
is_child_map: bool = maci_data.is_child_map(attr_name='')
is_parent_map: bool = maci_data.is_parent_map(attr_name='')
maci_data.lock_attr(attr_name='')
maci_data.map_attr(child_attr='', parent_attr='')
maci_data.unlock_attr(attr_name='')
maci_data.unmap_attr(attr_name='')
maci_data.load_attrs(data={})
get_attrs: Dict[str, Any] = maci_data.get_attrs()
