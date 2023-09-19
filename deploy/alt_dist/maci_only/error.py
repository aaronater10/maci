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


# Name compatibility aliases/deprecation from ported library
def __getattr__(attr_name: str) -> object:
    # Native
    if attr_name == 'ImportFile': return Load
    if attr_name == 'ImportFileRaw': return LoadRaw
    if attr_name == 'ImportAttrs': return LoadAttrs
    if attr_name == 'SaveFile': return Dump
    if attr_name == 'ExportFile': return DumpRaw
    if attr_name == 'AppendFile': return DumpRaw

    # Raise normal error if anything else
    raise_msg = f"module '{__name__}' has no attribute '{attr_name}'"
    raise AttributeError(raise_msg)
