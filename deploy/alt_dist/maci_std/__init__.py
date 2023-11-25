"""
maci - by aaronater10 (flavor: maci-std)

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

# JSON Lib
from ._json.jsonload import jsonload
from ._json.jsonloadstr import jsonloadstr
from ._json.jsondump import jsondump
from ._json.jsondumpstr import jsondumpstr

# INI Lib
from ._ini.iniload import iniload
from ._ini.inidump import inidump
from ._ini.inibuildauto import inibuildauto
from ._ini.inibuildmanual import inibuildmanual

# XML Lib
from ._xml.xmlload import xmlload
from ._xml.xmlloadstr import xmlloadstr
from ._xml.xmldump import xmldump
from ._xml.xmldumpstr import xmldumpstr
from ._xml.xmlbuildmanual import xmlbuildmanual

# Pickle Lib
from ._pickle.pickleloadbytes import pickleloadbytes
from ._pickle.pickledumpbytes import pickledumpbytes


# Name compatibility aliases/deprecation from ported library
def __getattr__(attr_name: str) -> object:
    # Native
    if attr_name == 'importfile': return load
    if attr_name == 'importfileraw': return loadraw
    if attr_name == 'importattrs': return loadattrs
    if attr_name == 'savefile': return dump
    if attr_name == 'exportfile': return dumpraw
    if attr_name == 'appendfile': raise error.GeneralError('"appendfile" no longer available. Use "dumpraw" with append=True option')
    # JSON
    if attr_name == 'jsonimportfile': return jsonload
    if attr_name == 'jsonimportstr': return jsonloadstr
    if attr_name == 'jsonexportfile': return jsondump
    if attr_name == 'jsonexportstr': return jsondumpstr
    # INI
    if attr_name == 'iniimportfile': return iniload
    if attr_name == 'iniexportfile': return inidump
    # XML
    if attr_name == 'xmlimportfile': return xmlload
    if attr_name == 'xmlimportstr': return xmlloadstr
    if attr_name == 'xmlexportfile': return xmldump
    if attr_name == 'xmlexportstr': return xmldumpstr

    # Raise normal error if anything else
    raise_msg = f"module '{__name__}' has no attribute '{attr_name}'"
    raise AttributeError(raise_msg)
