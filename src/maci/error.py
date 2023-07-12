# error - Contains maci and other exception names for handling
"""
Contains maci and other exception names for handling
"""
from typing import Any as _Any

# Base Exception
class MaciError(Exception):
    """
    maci base exception
    """
    def __init__(self, msg: _Any, item: _Any='') -> None:
        self.msg = str(msg)
        self.item = str(item)

    def __str__(self) -> str:
        return f'{self.msg} {self.item}'


# Module Exceptions

# General Error
class GeneralError(MaciError): pass

# Hints
class Hint(MaciError): pass

# Native
class Load(MaciError): pass
class LoadDict(MaciError): pass
class LoadStr(MaciError): pass
class LoadStrDict(MaciError): pass
class LoadRaw(MaciError): pass
class LoadAttrs(MaciError): pass
class Dump(MaciError): pass
class DumpStr(MaciError): pass
class DumpRaw(MaciError): pass
class CleanFormat(MaciError): pass

# Hash
class CompareFileHash(MaciError): pass
class CreateFileHash(MaciError): pass
class CreateHash(MaciError): pass

# JSON
class JsonLoad(MaciError): pass
class JsonLoadStr(MaciError): pass
class JsonDump(MaciError): pass
class JsonDumpStr(MaciError): pass

# YAML
class YamlLoad(MaciError): pass
class YamlLoadStr(MaciError): pass
class YamlDump(MaciError): pass
class YamlDumpStr(MaciError): pass

# TOML
class TomlLoad(MaciError): pass
class TomlLoadStr(MaciError): pass
class TomlDump(MaciError): pass
class TomlDumpStr(MaciError): pass

# INI
class IniLoad(MaciError): pass
class IniDump(MaciError): pass
class IniBuildAuto(MaciError): pass

# XML
class XmlLoad(MaciError): pass
class XmlLoadStr(MaciError): pass
class XmlDump(MaciError): pass
class XmlDumpStr(MaciError): pass


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
