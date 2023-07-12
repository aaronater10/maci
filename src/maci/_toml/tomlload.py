# tomlload
#########################################################################################################
# Imports
import tomli as _tomli
from typing import Dict as _Dict
from typing import Any as _Any
from ..error import TomlLoad

#########################################################################################################
# Load toml file
def tomlload(filename: str) -> _Dict[str, _Any]:
    """
    Loads toml data from a file

    Returns dict data with matching python data type. Assign the output to var

    Enter toml file location as str to load

    [Example Use]

    tomlload('path/to/filename.toml')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"

    if not isinstance(filename, str): raise TomlLoad(err_msg_type_file, f'\nGot: {repr(filename)}')

    # Load toml file
    try:
        with open(filename, 'rb') as f:
            return _tomli.load(f)
    except (FileNotFoundError, OSError) as err_msg: raise TomlLoad(err_msg, f'\nGot: {repr(filename)}')
    except _tomli.TOMLDecodeError as err_msg: raise TomlLoad(err_msg, f'\nGot: {repr(filename)}')
