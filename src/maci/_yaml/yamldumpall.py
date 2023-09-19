# yamldumpall
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Union as _Union
from typing import Iterable as _Iterable
from pathlib import Path as _PathObj
import yaml as _yaml  # type: ignore  # ignoring type checker for ext lib
from .._native.dumpraw import dumpraw as _dumpraw
from ..error import YamlDumpAll

#########################################################################################################
# Export yaml file
def yamldumpall(filename: _Union[str, _PathObj], data: _Iterable[_Any], *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Dumps a file from an iterable object that produces a yaml doc from each item to the file

    [Example Use]

    yamldumpall('path/to/filename.yml', data)    

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump_all" method, which only supports standard YAML tags and cannot represent arbitrary Python objects.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_data = "Only Iterable is allowed for 'data'"
    err_msg_type_append = "Only bool is allowed for 'append'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, (str, _PathObj)): raise YamlDumpAll(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(data, _Iterable): raise YamlDumpAll(err_msg_type_data, f'\nGot: {repr(data)}')
    if not isinstance(append, bool): raise YamlDumpAll(err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(encoding, (str, type(None))): raise YamlDumpAll(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    # Export data to yaml file
    try:
        with open(filename, write_mode, encoding=encoding) as f:
            if write_mode == 'a': _dumpraw(filename, '---\n', append=True)
            _yaml.safe_dump_all(data, f)
    except _yaml.error.YAMLError as err_msg: raise YamlDumpAll(err_msg, f'\nGot: {repr(data)}')
    except (FileNotFoundError, OSError) as err_msg: raise YamlDumpAll(err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise YamlDumpAll(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
