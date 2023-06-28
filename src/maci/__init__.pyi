"""
stub file to document public api functions, errors, object types, and doc string comments
"""
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Dict as _Dict
from typing import List as _List
from typing import Union as _Union
from typing import Optional as _Optional
from typing import NamedTuple as _NamedTuple
from typing import Set as _Set
from typing import Callable as _Callable
from data import MaciDataObj as __MaciDataObj

#########################################################################################################
# Stub data

### Exceptions ###
from . import error

### Hints ###
from . import hint

### Functions ###

# Native Lib
def load():
    ...
def loaddict():
    ...
def loadstr():
    ...
def loadstrdict():
    ...
def loadraw():
    ...
def loadattrs():
    ...
def dump():
    ...
def dumpstr():
    ...
def dumpraw():
    ...
def cleanformat():
    ...
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

# Hash Lib
def createfilehash():
    ...
def comparefilehash():
    ...
def createhash():
    ...

# JSON Lib
def jsonload():
    ...
def jsonloadstr():
    ...
def jsondump():
    ...
def jsondumpstr():
    ...

# YAML Lib
def yamlload():
    ...
def yamlloadstr():
    ...
def yamldump():
    ...
def yamldumpstr():
    ...

# TOML Lib
def tomlload():
    ...
def tomlloadstr():
    ...
def tomldump():
    ...
def tomldumpstr():
    ...

# INI Lib
def iniload():
    ...
def inidump():
    ...
def inibuildauto():
    ...
def inibuildmanual():
    ...

# XML Lib
def xmlload():
    ...
def xmlloadstr():
    ...
def xmldump():
    ...
def xmldumpstr():
    ...
def xmlbuildmanual():
    ...
