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
        return f'[Error] {self.msg} {self.item}'


# Module Exceptions

# General Error
class GeneralError(MaciError): __module__ = 'maci.error'

# Native
class Load(MaciError): __module__ = 'maci.error'
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
