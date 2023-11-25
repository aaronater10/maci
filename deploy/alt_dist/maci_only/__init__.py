"""
maci - by aaronater10 (flavor: maci-only)

Python-styled Serialization Language & Thin Wrapper Library

Version 1.0.0

Tutorials and docs: https://docs.macilib.org

Source: https://github.com/aaronater10/maci
"""
__version__ = '1.0.0'
__lang_version__ = '1.0.0'

#########################################################################################################
# Imports

# Exceptions
from . import error

# Hints
from . import hint

# Native Lib
from ._native.load import load
from ._native.loaddict import loaddict
from ._native.loadstr import loadstr
from ._native.loadstrdict import loadstrdict
from ._native.loadraw import loadraw
from ._native.loadattrs import loadattrs
from ._native.dump import dump
from ._native.dumpstr import dumpstr
from ._native.dumpraw import dumpraw
from ._native.cleanformat import cleanformat
from ._native.build import build

# Hash Lib
from ._hash.createfilehash import createfilehash
from ._hash.comparefilehash import comparefilehash
from ._hash.createhash import createhash


# Name compatibility aliases/deprecation from ported library
def __getattr__(attr_name: str) -> object:
    # Native
    if attr_name == 'importfile': return load
    if attr_name == 'importfileraw': return loadraw
    if attr_name == 'importattrs': return loadattrs
    if attr_name == 'savefile': return dump
    if attr_name == 'exportfile': return dumpraw
    if attr_name == 'appendfile': raise error.GeneralError('"appendfile" no longer available. Use "dumpraw" with append=True option')

    # Raise normal error if anything else
    raise_msg = f"module '{__name__}' has no attribute '{attr_name}'"
    raise AttributeError(raise_msg)
