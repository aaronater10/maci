# yamldump
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Union as _Union
import yaml as _yaml  # type: ignore  # ignoring type checker for ext lib
from ..error import YamlDump

#########################################################################################################
# Export yaml file
def yamldump(filename: str, data: _Any, *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Exports a new file from python data type to yaml data.
    
    Enter new filename as str. Pass any general data for output to file
    
    [Example Use]

    yamldump('path/to/filename.yml', data)    

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_append = "Only bool is allowed for 'append'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise YamlDump(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(append, bool): raise YamlDump(err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(encoding, (str, type(None))): raise YamlDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    # Export data to yaml file
    try:
        with open(filename, write_mode, encoding=encoding) as f:
            _yaml.safe_dump(data, f)
    except _yaml.error.YAMLError as err_msg: raise YamlDump(err_msg, f'\nGot: {repr(data)}')
    except (FileNotFoundError, OSError) as err_msg: raise YamlDump(err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise YamlDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
