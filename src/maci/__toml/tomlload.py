# tomlload
#########################################################################################################
# Imports
import tomli as _tomli
from ..error import TomlLoad
from typing import Dict as _Dict
from typing import Any as _Any

#########################################################################################################
# Load toml file
def tomlload(filename: str) -> _Dict[str, _Any]:
    """
    Loads toml data from a file

    Returns data with matching python data type. Assign the output to var

    Enter toml file location as str to load

    [Example Use]

    tomlload('path/to/filename.toml')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    """

    # Load toml file
    try:
        with open(filename, 'rb') as f:
            return _tomli.load(f)
    except FileNotFoundError as _err_msg: raise TomlLoad(_err_msg, f'\nFILE: "{filename}"')
    except OSError as _err_msg: raise TomlLoad(_err_msg, f'\nFILE: "{filename}"')
    except TypeError as _err_msg: raise TomlLoad(_err_msg, f'\nFILE: "{filename}"')
    except _tomli.TOMLDecodeError as _err_msg: raise TomlLoad(_err_msg, f'\nFILE: "{filename}"')
