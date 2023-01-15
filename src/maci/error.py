# error - Contains exception names and handling

# Base Exception
class MaciError(Exception):
    """
    maci base exception
    """
    def __init__(self, msg: str, item: str = '') -> None:
        self.msg = str(msg)
        self.item = str(item)

    def __str__(self) -> str:
        return f'{self.msg} {self.item}'


# Module Exceptions

# General Error
class GeneralError(MaciError): __module__ = 'maci.error'

# Native
class Load(MaciError): __module__ = 'maci.error'
class LoadStr(MaciError): __module__ = 'maci.error'
class LoadRaw(MaciError): __module__ = 'maci.error'
class LoadAttrs(MaciError): __module__ = 'maci.error'
class Dump(MaciError): __module__ = 'maci.error'
class DumpRaw(MaciError): __module__ = 'maci.error'
class CleanFormat(MaciError): __module__ = 'maci.error'

# Hash
class CompareFileHash(MaciError): __module__ = 'maci.error'
class CreateFileHash(MaciError): __module__ = 'maci.error'

# JSON
class JsonLoad(MaciError): __module__ = 'maci.error'
class JsonLoadStr(MaciError): __module__ = 'maci.error'
class JsonDump(MaciError): __module__ = 'maci.error'
class JsonDumpStr(MaciError): __module__ = 'maci.error'

# YAML
class YamlLoad(MaciError): __module__ = 'maci.error'
class YamlLoadStr(MaciError): __module__ = 'maci.error'
class YamlDump(MaciError): __module__ = 'maci.error'
class YamlDumpStr(MaciError): __module__ = 'maci.error'

# INI
class IniLoad(MaciError): __module__ = 'maci.error'
class IniDump(MaciError): __module__ = 'maci.error'
class IniBuildAuto(MaciError): __module__ = 'maci.error'

# XML
class XmlLoad(MaciError): __module__ = 'maci.error'
class XmlLoadStr(MaciError): __module__ = 'maci.error'
class XmlDump(MaciError): __module__ = 'maci.error'
class XmlDumpStr(MaciError): __module__ = 'maci.error'


# Name compatibility aliases/deprecation from ported library
def __getattr__(attr_name: str) -> object:
    # Native
    if attr_name == 'ImportFile': return Load
    if attr_name == 'ImportFileRaw': return LoadRaw
    if attr_name == 'ImportAttrs': return LoadAttrs
    if attr_name == 'SaveFile': return Dump
    if attr_name == 'ExportFile': return DumpRaw
    if attr_name == 'AppendFile': return DumpRaw
    # JSON
    if attr_name == 'JsonImportFile': return JsonLoad
    if attr_name == 'JsonImportStr': return JsonLoadStr
    if attr_name == 'JsonExportFile': return JsonDump
    if attr_name == 'JsonExportStr': return JsonDumpStr
    # YAML
    if attr_name == 'YamlImportFile': return YamlLoad
    if attr_name == 'YamlImportStr': return YamlLoadStr
    if attr_name == 'YamlExportFile': return YamlDump
    if attr_name == 'YamlExportStr': return YamlDumpStr
    # INI
    if attr_name == 'IniImportFile': return IniLoad
    if attr_name == 'IniExportFile': return IniDump
    # XML
    if attr_name == 'XmlImportFile': return XmlLoad
    if attr_name == 'XmlImportStr': return XmlLoadStr
    if attr_name == 'XmlExportFile': return XmlDump
    if attr_name == 'XmlExportStr': return XmlDumpStr

    # Raise normal error if anything else
    raise_msg = f"module '{__name__}' has no attribute '{attr_name}'"
    raise AttributeError(raise_msg)
