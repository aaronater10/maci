# yamlloadall
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import Union as _Union
from typing import Iterator as _Iterator
from pathlib import Path as _PathObj
import yaml as _yaml  # type: ignore  # ignoring type checker for ext lib
from ..error import YamlLoadAll

#########################################################################################################
# Import yaml file
def yamlloadall(filename: _Union[str, _PathObj], *, encoding: _Union[str, None]=None) -> _Iterator[_Any]:
    """
    Loads all yaml docs from a file

    Returns a generator of matching python data types

    [Example Use]

    yamlloadall('path/to/filename.yml')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load_all" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, (str, _PathObj)): raise YamlLoadAll(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(encoding, (str, type(None))): raise YamlLoadAll(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Import yaml docs from file
    try:
        with open(filename, 'r', encoding=encoding) as f:
            yaml_data = list(_yaml.safe_load_all(f))
            return (doc for doc in yaml_data)

    except (FileNotFoundError, OSError) as err_msg: raise YamlLoadAll(err_msg, f'\nGot: {repr(filename)}')
    except _yaml.error.YAMLError as err_msg: raise YamlLoadAll(err_msg, f'\nGot: {repr(filename)}')
    except LookupError: raise YamlLoadAll(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
