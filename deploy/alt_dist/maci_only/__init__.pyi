# stub file to document public api functions, errors, object types, and doc string comments
"""
maci - by aaronater10 (flavor: maci-only)

Python-styled Serialization Language & Thin Wrapper Library

Version 1.0.0

Tutorials and docs: https://docs.macilib.org

Source: https://github.com/aaronater10/maci
"""
__version__: str
__lang_version__: str

#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List
from typing import Tuple as _Tuple
from typing import Union as _Union
from typing import Optional as _Optional
from typing import Set as _Set
from typing import OrderedDict as _OrderedDict
from typing import Iterator as _Iterator
from typing import Iterable as _Iterable
from types import ModuleType as _ModuleType
from pathlib import Path as _PathObj
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
def load(filename: _Union[str, _PathObj], *, attr_name_dedup: bool=True, encoding: _Optional[str]=None, _ignore_maci_attr_check: bool=False) -> _MaciDataObj:
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

def loaddict(filename: _Union[str, _PathObj], *, attr_name_dedup: bool=True, encoding: _Optional[str]=None) -> dict:
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

def loadraw(filename: _Union[str, _PathObj], *, byte_data: bool=False, encoding: _Union[str, None]=None) -> _Union[str, bytes]:
    """
    Loads raw data from a file

    Returns a str or bytes. Returns empty string if file truly empty. Returns any whitespace if found in file

    [Options]

    byte_data: set to True if loading byte data

    [Example: Usage]

    loadraw('path/to/filename.any')

    Maci docs: https://docs.macilib.org
    """

def loadattrs(filename: _Union[str, _PathObj], class_object: _ClassObject, *, encoding: _Union[str, None]=None, attr_name_dedup: bool=False, _ignore_maci_attr_check: bool=True) -> None:
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
    filename: _Union[str, _PathObj], 
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

def dumpraw(filename: _Union[str, _PathObj], *data: _Any, append: bool=False, byte_data: bool=False, newline_sep: bool=True, encoding: _Union[str, None]=None) -> None:
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
    Formats a dict, list, tuple, or set, to a clean multiline structure to string

    [Example Use]
    
    var = cleanformat(data)

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
def createfilehash(file_to_hash: _Union[str, _PathObj], file_to_store_hash: _Union[str, _PathObj, None], hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> str:
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

def comparefilehash(file_to_hash: _Union[str, _PathObj], stored_hash_file: _Union[str, _PathObj], hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> bool:
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
