# error - Contains exception names and handling
"""
Contains exception names for handling
"""

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
class GeneralError(MaciError): ...

# Hints
class Hint(MaciError): ...

# Native
class Load(MaciError): ...
class LoadStr(MaciError): ...
class LoadRaw(MaciError): ...
class LoadAttrs(MaciError): ...
class Dump(MaciError): ...
class DumpStr(MaciError): ...
class DumpRaw(MaciError): ...
class CleanFormat(MaciError): ...

# Hash
class CompareFileHash(MaciError): ...
class CreateFileHash(MaciError): ...

# JSON
class JsonLoad(MaciError): ...
class JsonLoadStr(MaciError): ...
class JsonDump(MaciError): ...
class JsonDumpStr(MaciError): ...

# YAML
class YamlLoad(MaciError): ...
class YamlLoadStr(MaciError): ...
class YamlDump(MaciError): ...
class YamlDumpStr(MaciError): ...

# INI
class IniLoad(MaciError): ...
class IniDump(MaciError): ...
class IniBuildAuto(MaciError): ...

# XML
class XmlLoad(MaciError): ...
class XmlLoadStr(MaciError): ...
class XmlDump(MaciError): ...
class XmlDumpStr(MaciError): ...


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
