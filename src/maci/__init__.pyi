"""
stub file to document public api functions, errors, object types, and doc string comments
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
from .data import MaciDataObj as __MaciDataObj
from .data import CustomClass as _CustomClass

#########################################################################################################
# Stub data: Exceptions, Hints

### Exceptions ###
from . import error

### Hints ###
from . import hint


#########################################################################################################
# Stub data: Functions

### Native Lib ###
def load(filename: str, *, attr_name_dedup: bool=True, encoding: _Optional[str]=None, _ignore_maci_attr_check: bool=False) -> _Optional[__MaciDataObj]:
    """
    Imports saved python data from any text file.

    Returns a class of attributes. Assign the output to var

    Enter file location as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if file empty

    [Example Use]
    load('filename.data' or 'path/to/filename.data')

    [Warning]
    Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This also may affect MaciDataObj behavior
    including the ability to overwrite internal dunder names. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.
    """

def loaddict(filename: str, *, attr_name_dedup: bool=True, encoding: _Optional[str]=None) -> _Optional[dict]:
    """
    Imports pythonic data from any text file

    Returns a dict. Assign the output to var

    Enter file location as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if file empty

    [Example Use]
    loaddict('path/to/filename.data')

    [Warning]
    Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This also may affect MaciDataObj behavior
    including the ability to overwrite internal dunder names. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.
    """

def loadstr(py_str_data: str, *, attr_name_dedup: bool=True) -> _Optional[__MaciDataObj]:
    """
    Imports python data from a string.

    Returns a class of attributes. Assign the output to var

    Enter python data string as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if empty

    [Example Use]

    loadstr("data1 = 'value1'\\ndata2 = "value2")
    """

def loadstrdict(py_str_data: str, *, attr_name_dedup: bool=True) -> dict:
    """
    Imports pythonic data from a string.

    Returns a dict. Assign the output to var

    Enter pythonic data string as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes, datetime

    Returns None if empty

    [Example Use]

    loadstrdict("data1 = 'value1'\\ndata2 = "value2")
    """

def loadraw(filename: str, *, byte_data: bool=False, encoding: _Union[str, None]=None) -> _Union[str, bytes]:
    """
    Imports any raw data from a file.

    Returns a str. Assign the output to var

    [Options]
    byte_data: Set to True if importing byte data

    [Example Use]

    loadraw('path/to/filename')
    """

def loadattrs(filename: str, class_object: _CustomClass, *, encoding: _Union[str, None]=None, attr_name_dedup: bool=False, _ignore_maci_attr_check: bool=True) -> None:
    """
    Import saved attributes from file back into a custom class. This is done in-place

    Enter filename as str, Pass custom class object.

    [Example Use]

    loadattrs('path/of/filename', 'class_object')

    [Warning]
    Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This also may affect MaciDataObj behavior
    including the ability to overwrite internal dunder names. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.
    """

def dump(
    filename: str, 
    data: _Union['__MaciDataObj', dict, _CustomClass], 
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
    Dumps your attributes or key/value pair data to a file

    Enter filename as str, Pass MaciDataObj, dict, or Custom Class data type for output to file

    [Importing Data Back] Functions:

    load: Import data back returning a class of attributes with Maci features

    loadattrs: Import attributes back into a custom class. This is done in-place

    [Options]

    append: set to True to append data to a file (Default=False, which writes a new file each time)

    indent_level: set indent level for types list, dict, tuple, set (Default 1)

    indentation_on: set to False to turn OFF indentation on types list, dict, tuple, set (Default ON)

    [Example Use]
    Normal: dump('path/of/filename', 'data')

    Append to File: dump('path/of/filename', 'data', append=True)

    Indent OFF: dump('path/of/filename', 'data', indentation_on=False)
    """

def dumpstr(
    data: _Union['__MaciDataObj', dict, _CustomClass], 
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
    Dumps your attributes or key/value pair data to a string

    Pass MaciDataObj, dict, or Custom Class data type for output to str

    [Importing Data Back] Functions:

    loadstr: Import data from str returning a class of attributes with Maci features

    [Options]

    indent_level: set indent level for types list, dict, tuple, set (Default 1)

    indentation_on: set to False to turn OFF indentation on types list, dict, tuple, set (Default ON)

    [Example Use]
    Normal: dumpstr(data)

    Indent OFF: dumpstr(data, indentation_on=False)
    """

def dumpraw(filename: str, *data: _Any, append: bool=False, byte_data: bool=False, newline_sep: bool=True, encoding: _Union[str, None]=None) -> None:
    """
    Exports a new file with the new data.
    
    Enter new filename as str, Pass any data type for output to file.

    [Options]
    append: set to True to append data to a file (Default=False, which writes a new file each time)

    byte_data: Set to True to write byte data. Default False

    [Example Use]
    Normal: dump('path/of/filename', 'data')

    Byte Data: dump('path/of/filename', b'data', byte_data=True)
    """

def cleanformat(data: _Union[dict,list,tuple,set], indent_level: int=1) -> str:
    """
    Formats a (single) dictionary, list, tuple, or set, to have a clean multiline output for exporting to a file.

    Returned output will be a str

    Note: Higher indent levels will decrease performance. Indentation is applied to the main data set only.

    Tip: Changing indent level to 0 increases cleaning performance by 5%, but output will have no indentation (Default = 1).

    Accepted data types: dict, list, tuple, set 

    [Example Use]
    
    var = cleanformat(data)
    """

def build() -> __MaciDataObj:
    """
    Returns an empty MaciDataObj obj to manually build pythonic data with maci features
    
    Assign the output to var

    Literally, just use attribute assignment as you normally would

    [Example]

    object.attribute1 = [1,2,3]

    object.attribute2 = 'string data'

    More information on object features: https://docs.macilib.org/docs/tools/build-data/python-data-build
    """


### Hash Lib ###
def createfilehash(file_to_hash: str, file_to_store_hash: _Union[str,None], hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> str:
    """
    Creates a hash of any file, and stores the hash data to a new created file

    Always returns a str of the hash as well. Assign the output to var

    Enter file locations as str

    [Options]
    file_to_store_hash: Set to False if you do not want hash data stored to a file. Hash data is always returned whether or not this is set

    hash_algorithm: Already set to default of 'sha256'. Supported options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'

    [Example Use]

    Default: createfilehash('path/to/src_filename', 'path/to/dst_hash_filename')
    Hash only, no file: hash_data = createfilehash('path/to/filename', False)

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html
    """

def comparefilehash(file_to_hash: str, stored_hash_file: str, hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> bool:
    """
    Compares hash of any file by importing the previously stored hash file data from using "createfilehash"

    Returns a bool if the hash does/doesn't match

    Enter file locations as str

    [Options]

    hash_algorithm: Already set to default of 'sha256'. Supported options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'

    [Example Use]
    
    comparefilehash('path/to/src_filename', 'path/to/src_hash_filename')

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html
    """

def createhash(data_to_hash: _Union[str, bytes, int, _List[int], _Tuple[int], _Set[int], range, bool], hash_algorithm: str='sha256', *, encoding: str='utf-8') -> str:
    """
    Creates a hash of the provided data

    Returns a str of the hash in hex. Assign the output to var

    [Options]

    hash_algorithm: Default is 'sha256'. Supported options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'

    [Example Use]

    createhash('data')

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html
    """


### JSON Lib ###
def jsonload(filename: str, *, encoding: _Union[str, None]=None) -> _Union[list, dict, str, int, float, bool, None]:
    """
    Imports json data from a file

    Returns data with matching python data type. Assign the output to var

    Enter json file location as str to import.

    [Example Use]

    jsonload('path/to/filename.json')

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
    """

def jsonloadstr(json_str_data: str) -> _Union[list, dict, str, int, float, bool, None]:
    """
    Imports json data from a string

    Returns data with matching python data type. Assign the output to var

    Enter json string as str to import.

    [Example Use]

    jsonloadstr('string with json data')

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html
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
    Exports a new file from python data type to json data.
    
    Enter new filename as str. Pass data for output to file
    
    [Example Use]

    jsondump('path/to/filename.json', data)    

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    """

def jsondumpstr(data: _Union[dict, list, tuple, str, int, float, bool, None], *, indent_level: int=4) -> str:
    """
    Exports python data type to json string

    Returns a json formatted str. Assign the output to var

    [Example Use]

    jsondumpstr(data, [optional] indent_level)

    This is using the native json library shipped with the python standard library. For more
    information on the json library, visit: https://docs.python.org/3/library/json.html

    """


### YAML Lib ###
def yamlload(filename: str, *, encoding: _Union[str, None]=None) -> _Any:
    """
    Imports yaml data from a file.

    Returns data with matching python data type. Assign the output to var

    Enter yaml file location as str to import.

    [Example Use]

    yamlload('path/to/filename.yml')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    """

def yamlloadstr(yaml_str_data: str) -> _Any:
    """
    Imports yaml data from a string

    Returns data with matching python data type. Assign the output to var

    Enter yaml string as str to import.

    [Example Use]

    yamlloadstr('string with yaml data')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    """

def yamldump(filename: str, data: _Any, *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Exports a new file from python data type to yaml data.
    
    Enter new filename as str. Pass any general data for output to file
    
    [Example Use]

    yamldump('path/to/filename.yml', data)    

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    """

def yamldumpstr(data: _Any) -> str:
    """
    Exports python data type to yaml string

    Returns a yaml formatted str. Assign the output to var

    [Example Use]

    yamldumpstr(data)

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    """


### TOML Lib ###
def tomlload(filename: str) -> _Dict[str, _Any]:
    """
    Loads toml data from a file

    Returns dict data with matching python data type. Assign the output to var

    Enter toml file location as str to load

    [Example Use]

    tomlload('path/to/filename.toml')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    """

def tomlloadstr(toml_str_data: str) -> _Dict[str, _Any]:
    """
    Load toml data from a string

    Returns dict data with matching python data types. Assign the output to var

    [Example Use]

    tomlloadstr('string with toml data')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    """

def tomldump(
    filename: str,
    data: _Dict[str, _Any],
    *,
    append: bool=False,
    multi_line_str: bool=False
) -> None:
    """
    Dumps a new file from dict to toml data.

    Enter filename as str. Pass data for output to file

    [Example Use]

    tomldump('path/to/filename.toml', data)    

    This is using the tomli-w library installed as a dependency from pypi.
    For more information on tomli-w, visit: https://pypi.org/project/tomli-w/
    """

def tomldumpstr(
    data: _Dict[str, _Any],
    *,
    multi_line_str: bool=False
) -> str:
    """
    Dumps dict data to toml string

    Returns a toml formatted str. Assign the output to var

    [Example Use]

    tomldumpstr(data)

    This is using the tomli-w library installed as a dependency from pypi.
    For more information on tomli-w, visit: https://pypi.org/project/tomli-w/
    """


### INI Lib ###
def iniload(filename: str, *, encoding: _Union[str, None]=None) -> _ConfigParser:
    """
    Imports ini data from a file.

    Returns a ConfigParser obj. Assign the output to var

    Enter ini file location as str to import.

    [Example Use]

    iniload('path/to/filename.ini')

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """

def inidump(filename: str, ini_data: _ConfigParser, *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Exports a new file from a ini data (ConfigParser) obj

    Enter new filename as str. Pass ini data for output to file
    
    [Example Use]

    inidump('path/to/filename.ini', ini_data)

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method.
    For more information on the configparser library, visit: https://docs.python.org/3/library/configparser.html
    """

def inibuildauto(data: _Dict[str, _Dict[str, _Any]]) -> _ConfigParser:
    """
    Auto converts dict to ini data structure

    Returns a ConfigParser obj with your data. Assign the output to var

    All sub-values are converted to strings naturally by the library. However, if your sub-value
    contains a Nonetype, this function will also auto-convert to a string for you.

    Enter correctly structured dict to convert data

    [Example dict structure]

    {
        'section1': {'key1': 1},

        'section2': {'key2': 2}   
    }

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """

def inibuildmanual() -> _ConfigParser:
    """    
    Returns an empty ConfigParser object to manually build ini data
    
    Assign the output to var

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """


### XML Lib ###
def xmlload(filename: str, *, auto_get_root: bool=True) -> _Union[_Element, _ElementTree]:
    """
    Imports xml data from a file.

    Returns the root Element object of the ElementTree parsed from a xml file by default. Assign the output to var

    Enter xml file location as str to import.

    [Example Use]

    xmlload('path/to/filename.xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """

def xmlloadstr(xml_str_data: str) -> _Element:
    """
    Imports xml data from a string

    Returns a xml Element. Assign the output to var

    [Example Use]

    xmlloadstr('<tag>data</tag>')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """

def xmldump(filename: str, data: _Union[_ElementTree, _Element], *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Exports a new file from xml ElementTree or Element object as xml data
    
    Enter new filename as str. Pass ElementTree data for output to file
    
    [Example Use]

    xmldump('path/to/filename.xml', Element_data)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """

def xmldumpstr(data: _Element, *, encoding: str='utf-8') -> str:
    """
    Exports xml Element object to a string

    Returns a str. Assign the output to var

    [Example Use]

    xmldumpstr(Element)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """

def xmlbuildmanual() -> _ModuleType:
    """
    Returns a xml ElementTree module object to build/work with xml data
    
    Assign the output to var -> Module('xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
