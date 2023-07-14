# stub file to document public api functions, errors, object types, and doc string comments
"""
maci - by aaronater10

A Pythonic Configuration Language & Thin Wrapper Library

Version 0.5.0

Tutorials and docs: https://docs.macilib.org

Source: https://github.com/aaronater10/maci
"""
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List
from typing import Tuple as _Tuple
from typing import Union as _Union
from typing import Optional as _Optional
from typing import Set as _Set
from types import ModuleType as _ModuleType
from configparser import ConfigParser as _ConfigParser
from xml.etree.ElementTree import ElementTree as _ElementTree
from xml.etree.ElementTree import Element as _Element
from .hint import MaciDataObj as _MaciDataObj
from .hint import __ClassObject as _ClassObject  # type: ignore  # ignoring attr export

#########################################################################################################
# Stub data: Exceptions, Hints

### Exceptions ###
from . import error

### Hints ###
from . import hint


#########################################################################################################
# Stub data: Functions

### Native Lib ###
def load(filename: str, *, attr_name_dedup: bool=True, encoding: _Optional[str]=None, _ignore_maci_attr_check: bool=False) -> _MaciDataObj:
    """
    Loads maci (pythonic) data from a file

    Returns a 'MaciDataObj' object with maci features. Returns empty object if file empty

    [Example: Usage]

    load('path/to/filename.any')

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.

    Maci docs: https://docs.macilib.org
    """

def loaddict(filename: str, *, attr_name_dedup: bool=True, encoding: _Optional[str]=None) -> dict:
    """
    Loads maci (pythonic) data from a file

    Returns a dict representing your attributes & data values. Returns empty dict if file empty

    [Example: Usage]

    loaddict('path/to/filename.any')

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.

    Maci docs: https://docs.macilib.org
    """

def loadstr(maci_str_data: str, *, attr_name_dedup: bool=True) -> _MaciDataObj:
    """
    Loads maci (pythonic) data from a string

    Returns a 'MaciDataObj' object with maci features. Returns empty object if string empty

    [Example: Usage]

    loadstr('string with maci data')

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a string that has already been created.

    Maci docs: https://docs.macilib.org
    """

def loadstrdict(maci_str_data: str, *, attr_name_dedup: bool=True) -> dict:
    """
    Loads maci (pythonic) data from a string

    Returns a dict representing your attributes & data values. Returns empty dict if string empty

    [Example: Usage]

    loadstrdict('string with maci data')

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a string that has already been created.

    Maci docs: https://docs.macilib.org
    """

def loadraw(filename: str, *, byte_data: bool=False, encoding: _Union[str, None]=None) -> _Union[str, bytes]:
    """
    Loads raw data from a file

    Returns a str or bytes. Returns empty string if file truly empty. Returns any whitespace if found in file

    [Options]

    byte_data: set to True if loading byte data

    [Example: Usage]

    loadraw('path/to/filename.any')

    Maci docs: https://docs.macilib.org
    """

def loadattrs(filename: str, class_object: _ClassObject, *, encoding: _Union[str, None]=None, attr_name_dedup: bool=False, _ignore_maci_attr_check: bool=True) -> None:
    """
    Load attribute data from file into a custom class/object. This is done in-place

    [Example: Usage]

    loadattrs('path/of/filename.any', custom_object)

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.

    Maci docs: https://docs.macilib.org
    """

def dump(
    filename: str, 
    data: _Union['_MaciDataObj', dict, _ClassObject], 
    *,
    append: bool=False,
    indent_level: int=1,
    indentation_on: bool=True,
    multi_line_str: bool=False,
    encoding: _Union[str, None]=None,
    private_attrs: bool=False,
    private_under_attrs: bool=False,
    private_dunder_attrs: bool=False,
    class_attrs: bool=False,
    private_init_attrs: bool=False,
    private_init_under_attrs: bool=False,
    private_init_dunder_attrs: bool=False,
    private_class_attrs: bool=False,
    private_class_under_attrs: bool=False,
    private_class_dunder_attrs: bool=False,
    use_symbol_glyphs: bool=False,
    ) -> None:
    """
    Dumps maci, dict, or custom object data to a file. Output in file
    is structured in maci (pythonic) style format

    [Partner Functions]

    load: Load data from file returning a MaciDataObj with maci features

    loadattrs: Load attrs & data from file into a custom class/object. This is done in-place

    loaddict: Load data from file returning a dict representing your attrs & data

    [Options]

    append: set to True to append data to a file - Default=False, which writes a new file each time

    indent_level: set indent level for data being list, dict, tuple, or set - Default=1

    [Example: Usage]

    dump('path/of/filename', data)

    Maci docs: https://docs.macilib.org
    """

def dumpstr(
    data: _Union['_MaciDataObj', dict, _ClassObject], 
    *,
    indent_level: int=1,
    indentation_on: bool=True,
    multi_line_str: bool=False,
    private_attrs: bool=False,
    private_under_attrs: bool=False,
    private_dunder_attrs: bool=False,
    class_attrs: bool=False,
    private_init_attrs: bool=False,
    private_init_under_attrs: bool=False,
    private_init_dunder_attrs: bool=False,
    private_class_attrs: bool=False,
    private_class_under_attrs: bool=False,
    private_class_dunder_attrs: bool=False,
    use_symbol_glyphs: bool=False,
    ) -> _Optional[str]:
    """
    Dumps maci, dict, or custom object data to a string. Output in string
    is structured in maci (pythonic) style format

    [Partner Functions]

    loadstr: Load data from str returning a MaciDataObj with maci features

    loadstrdict: Load data from str returning a dict representing your attrs & data

    [Options]

    indent_level: set indent level for data being list, dict, tuple, or set - Default=1

    [Example: Usage]

    dumpstr(data)

    Maci docs: https://docs.macilib.org
    """

def dumpraw(filename: str, *data: _Any, append: bool=False, byte_data: bool=False, newline_sep: bool=True, encoding: _Union[str, None]=None) -> None:
    """
    Dumps a new file with the data raw

    [Options]
    append: set to True to append data to a file - Default=False, which writes a new file each time

    byte_data: set to True to write byte data - Default=False

    [Example: Usage]

    dumpraw('path/of/filename', data)

    Maci docs: https://docs.macilib.org
    """

def cleanformat(data: _Union[dict,list,tuple,set], indent_level: int=1) -> str:
    """
    Formats a single dictionary, list, tuple, or set, to a clean multiline form

    Note: Higher indent levels will decrease performance, and indentation is applied to the main level data set only.

    Tip: Changing indent level to 0 increases format performance by approx 5%, but output will have no indentation (Default level = 1).

    [Example: Usage]
    
    var = cleanformat([1,2,3])

    Maci docs: https://docs.macilib.org
    """

def build() -> _MaciDataObj:
    """
    Returns an empty 'MaciDataObj' object to manually build data with maci features

    Use attribute assignment as you normally would to build out data

    [Example: Usage]

    var = maci.build()

    [Example: Assign Data]

    var.my_list = [1,2,3]

    Maci docs: https://docs.macilib.org
    """


### Hash Lib ###
def createfilehash(file_to_hash: str, file_to_store_hash: _Union[str,None], hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> str:
    """
    Creates a hash of any file, and stores the hash data to a new created file

    Always returns a str of the hashed file

    [Partner Functions]

    comparefilehash: auto compares hashes from src hash of file with stored hash file data

    [Options]
    
    file_to_store_hash: Set to None if you do not want a file created to store hash. Hash data of the src file is always returned whether or not this is set

    hash_algorithm: Default is 'sha256' - Other options: 'sha512', 'sha384', 'sha1', 'md5'

    [Example: Usage]

    createfilehash('path/to/src_filename', 'path/to/dst_hash_filename')

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html

    Maci docs: https://docs.macilib.org
    """

def comparefilehash(file_to_hash: str, stored_hash_file: str, hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> bool:
    """
    Compares a hash of any file by comparing the previously created file with hash data stored from using the "createfilehash" partner function

    Returns a bool if the hash does/doesn't match

    [Partner Functions]

    createfilehash: creates the initial hash file data to compare against

    [Options]

    hash_algorithm: Default is 'sha256' - Other options: 'sha512', 'sha384', 'sha1', 'md5'

    [Example: Usage]
    
    comparefilehash('path/to/src_filename', 'path/to/src_hash_filename')

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html

    Maci docs: https://docs.macilib.org
    """

def createhash(data_to_hash: _Union[str, bytes, int, _List[int], _Tuple[int], _Set[int], range, bool], hash_algorithm: str='sha256', *, encoding: str='utf-8') -> str:
    """
    Creates a hash of the provided data

    Returns a str of the hash in hex

    [Options]

    hash_algorithm: Default is 'sha256' - Other options: 'sha512', 'sha384', 'sha1', 'md5'

    [Example: Usage]

    var = createhash(data)

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html

    Maci docs: https://docs.macilib.org
    """


### JSON Lib ###
def jsonload(filename: str, *, encoding: _Union[str, None]=None) -> _Union[list, dict, str, int, float, bool, None]:
    """
    Loads json data from a file

    Returns data with matching python data type

    [Example: Usage]

    jsonload('path/to/filename.json')

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    Maci docs: https://docs.macilib.org
    """

def jsonloadstr(json_str_data: str) -> _Union[list, dict, str, int, float, bool, None]:
    """
    Loads json data from a string

    Returns data with matching python data type

    [Example: Usage]

    jsonloadstr('string with json data')

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    Maci docs: https://docs.macilib.org
    """

def jsondump(
    filename: str,
    data: _Union[dict, list, tuple, str, int, float, bool, None],
    *,
    append: bool=False,
    indent_level: int=4,
    encoding: _Union[str, None]=None
) -> None:
    """
    Dumps json data to a file from python data
    
    [Example: Usage]

    jsondump('path/to/filename.json', data)    

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    Maci docs: https://docs.macilib.org
    """

def jsondumpstr(data: _Union[dict, list, tuple, str, int, float, bool, None], *, indent_level: int=4) -> str:
    """
    Dumps json data to a str from python data

    Returns a json formatted str

    [Example: Usage]

    jsondumpstr(data)

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    Maci docs: https://docs.macilib.org
    """


### YAML Lib ###
def yamlload(filename: str, *, encoding: _Union[str, None]=None) -> _Any:
    """
    Loads yaml data from a file

    Returns data with matching python data type

    [Example: Usage]

    yamlload('path/to/filename.yaml')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    Maci docs: https://docs.macilib.org
    """

def yamlloadstr(yaml_str_data: str) -> _Any:
    """
    Loads yaml data from a string

    Returns data with matching python data type

    [Example: Usage]

    yamlloadstr('string with yaml data')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    Maci docs: https://docs.macilib.org
    """

def yamldump(filename: str, data: _Any, *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Dumps yaml data to a file from python data
    
    [Example: Usage]

    yamldump('path/to/filename.yaml', data)    

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    Maci docs: https://docs.macilib.org
    """

def yamldumpstr(data: _Any) -> str:
    """
    Dumps yaml data to a string from python data

    Returns a yaml formatted str

    [Example: Usage]

    yamldumpstr(data)

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    Maci docs: https://docs.macilib.org
    """


### TOML Lib ###
def tomlload(filename: str) -> _Dict[str, _Any]:
    """
    Loads toml data from a file

    Returns dict data with matching python data type values

    [Example: Usage]

    tomlload('path/to/filename.toml')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    
    Maci docs: https://docs.macilib.org
    """

def tomlloadstr(toml_str_data: str) -> _Dict[str, _Any]:
    """
    Load toml data from a string

    Returns dict data with matching python data type values

    [Example: Usage]

    tomlloadstr('string with toml data')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    
    Maci docs: https://docs.macilib.org
    """

def tomldump(
    filename: str,
    data: _Dict[str, _Any],
    *,
    append: bool=False,
    multi_line_str: bool=False
) -> None:
    """
    Dumps toml data to a file from dict

    [Example: Usage]

    tomldump('path/to/filename.toml', data)

    This is using the tomli-w library installed as a dependency from pypi.
    For more information on tomli-w, visit: https://pypi.org/project/tomli-w/

    Maci docs: https://docs.macilib.org
    """

def tomldumpstr(
    data: _Dict[str, _Any],
    *,
    multi_line_str: bool=False
) -> str:
    """
    Dumps toml data to a string from dict

    Returns a toml formatted str

    [Example: Usage]

    tomldumpstr(data)

    This is using the tomli-w library installed as a dependency from pypi.
    For more information on tomli-w, visit: https://pypi.org/project/tomli-w/
    
    Maci docs: https://docs.macilib.org
    """


### INI Lib ###
def iniload(filename: str, *, encoding: _Union[str, None]=None) -> _ConfigParser:
    """
    Loads ini data from a file

    Returns a ConfigParser object

    [Example: Usage]

    iniload('path/to/filename.ini')

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    
    Maci docs: https://docs.macilib.org
    """

def inidump(filename: str, data: _ConfigParser, *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Dumps ini data to a file from a ConfigParser object

    [Example: Usage]

    inidump('path/to/filename.ini', data)

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    
    Maci docs: https://docs.macilib.org
    """

def inibuildauto(data: _Dict[str, _Dict[str, _Any]]) -> _ConfigParser:
    """
    Auto builds ini data object from dict

    Returns a ConfigParser object with your data

    Note: All sub-values are converted to strings naturally by the library. However, if your sub-value
    contains a 'NoneType', this function will also auto-convert that to a string for you.

    Enter correctly structured dict to build data

    [Example: ini dict structure]

    {
        'section1': {'key1': 1},

        'section2': {'key2': 2}   
    }

    [Example: Usage]

    var = inibuildauto(data)

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html

    Maci docs: https://docs.macilib.org
    """

def inibuildmanual() -> _ConfigParser:
    """    
    Returns an empty ConfigParser object to manually build ini data

    [Example: Usage]

    var = inibuildmanual()

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html

    Maci docs: https://docs.macilib.org
    """


### XML Lib ###
def xmlload(filename: str, *, auto_get_root: bool=True) -> _Union[_Element, _ElementTree]:
    """
    Loads xml data from a file

    Returns a xml etree root Element object of the ElementTree parsed from a xml file by default

    [Example: Usage]

    xmlload('path/to/filename.xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """

def xmlloadstr(xml_str_data: str) -> _Element:
    """
    Loads xml data from a string

    Returns a xml etree Element object

    [Example: Usage]

    xmlloadstr('string with xml data')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """

def xmldump(filename: str, data: _Union[_ElementTree, _Element], *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Dumps xml data to a file from xml etree ElementTree or Element object
    
    [Example: Usage]

    xmldump('path/to/filename.xml', data)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """

def xmldumpstr(data: _Element, *, encoding: str='utf-8') -> str:
    """
    Dumps xml data to a string from xml etree Element object

    Returns a xml formatted str

    [Example: Usage]

    xmldumpstr(data)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """

def xmlbuildmanual() -> _ModuleType:
    """
    Returns an empty xml ElementTree module object to manually build xml etree data

    Returns etree -> Module('xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """

def _defuse_xml_stdlib() -> dict:
    """Monkey patch and defuse all stdlib packages

    :warning: The monkey patch is an EXPERIMETNAL feature.

    ___

    [Example: Usage]

    maci._defuse_xml_stdlib()

    For more information on the provided defusedxml ext pkg, visit: https://pypi.org/project/defusedxml

    Python doc stating std lib xml vulns and recommending defusedxml: https://docs.python.org/3/library/xml.html#xml-vulnerabilities
    
    Maci docs: https://docs.macilib.org
    """
