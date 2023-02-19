"""
maci - by aaronater10

Version 0.1.0

The easy to use library for your data, configuration, and save files.

Import or Export custom, or industry-common, data, config, and save files easily for
your python program or script!

See tutorials and docs here for more info: https://docs.macilib.org

Source Code: https://github.com/aaronater10/maci
"""
__version__ = '0.1.0'

#########################################################################################################
# Imports

# Base Exceptions
from . import error

# Hints
from . import hint

# Native Lib
from .__native.load import load
from .__native.loadstr import loadstr
from .__native.loadraw import loadraw
from .__native.loadattrs import loadattrs
from .__native.dump import dump
from .__native.dumpstr import dumpstr
from .__native.dumpraw import dumpraw
from .__native.cleanformat import cleanformat
from .__native.build import build

# Hash Lib
from .__hash.createfilehash import createfilehash
from .__hash.comparefilehash import comparefilehash
from .__hash.createhash import createhash

# JSON Lib
from .__json.jsonload import jsonload
from .__json.jsonloadstr import jsonloadstr
from .__json.jsondump import jsondump
from .__json.jsondumpstr import jsondumpstr

# YAML Lib
from .__yaml.yamlload import yamlload
from .__yaml.yamlloadstr import yamlloadstr
from .__yaml.yamldump import yamldump
from .__yaml.yamldumpstr import yamldumpstr

# INI Lib
from .__ini.iniload import iniload
from .__ini.inidump import inidump
from .__ini.inibuildauto import inibuildauto
from .__ini.inibuildmanual import inibuildmanual

# XML Lib
from .__xml.xmlload import xmlload
from .__xml.xmlloadstr import xmlloadstr
from .__xml.xmldump import xmldump
from .__xml.xmldumpstr import xmldumpstr
from .__xml.xmlbuildmanual import xmlbuildmanual


# Name compatibility aliases/deprecation from ported library
def __getattr__(attr_name: str) -> object:
    # Native
    if attr_name == 'importfile': return load
    if attr_name == 'importfileraw': return loadraw
    if attr_name == 'importattrs': return loadattrs
    if attr_name == 'savefile': return dump
    if attr_name == 'exportfile': return dumpraw
    if attr_name == 'appendfile': raise error.GeneralError('"appendfile" no longer available. Use "dumpraw" with mode="a" option')
    # JSON
    if attr_name == 'jsonimportfile': return jsonload
    if attr_name == 'jsonimportstr': return jsonloadstr
    if attr_name == 'jsonexportfile': return jsondump
    if attr_name == 'jsonexportstr': return jsondumpstr
    # YAML
    if attr_name == 'yamlimportfile': return yamlload
    if attr_name == 'yamlimportstr': return yamlloadstr
    if attr_name == 'yamlexportfile': return yamldump
    if attr_name == 'yamlexportstr': return yamldumpstr
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
