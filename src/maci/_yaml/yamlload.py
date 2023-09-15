# yamlload
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Union as _Union
from pathlib import Path as _PathObj
import yaml as _yaml  # type: ignore  # ignoring type checker for ext lib
from ..error import YamlLoad

#########################################################################################################
# Import yaml file
def yamlload(filename: _Union[str, _PathObj], *, encoding: _Union[str, None]=None) -> _Any:
    """
    Loads yaml data from a file

    Returns data with matching python data type

    [Example: Usage]

    yamlload('path/to/filename.yaml')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, (str, _PathObj)): raise YamlLoad(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(encoding, (str, type(None))): raise YamlLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Import yaml file
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return _yaml.safe_load(f)
    except (FileNotFoundError, OSError) as err_msg: raise YamlLoad(err_msg, f'\nGot: {repr(filename)}')
    except _yaml.error.YAMLError as err_msg: raise YamlLoad(err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise YamlLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
