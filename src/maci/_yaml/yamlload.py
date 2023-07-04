# yamlload
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Union as _Union
import yaml as _yaml  # type: ignore  # ignoring type checker for ext lib
from ..error import YamlLoad

#########################################################################################################
# Import yaml file
def yamlload(filename: str, *, encoding: _Union[str, None]=None) -> _Any:
    """
    Imports yaml data from a file.

    Returns data with matching python data type. Assign the output to var

    Enter yaml file location as str to import.

    [Example Use]

    yamlload('path/to/filename.yml')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise YamlLoad(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(encoding, (str, type(None))): raise YamlLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')


    # Import yaml file
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return _yaml.safe_load(f)
    except (FileNotFoundError, OSError) as err_msg: raise YamlLoad(err_msg, f'\nGot: {repr(filename)}')
    except _yaml.error.YAMLError as err_msg: raise YamlLoad(err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise YamlLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
