# tomlloadstr
#########################################################################################################
# Imports
import tomli as _tomli
from typing import Dict as _Dict
from typing import Any as _Any
from ..error import TomlLoadStr

#########################################################################################################
# Load toml file
def tomlloadstr(toml_str_data: str) -> _Dict[str, _Any]:
    """
    Load toml data from a string

    Returns dict data with matching python data types. Assign the output to var

    [Example Use]

    tomlloadstr('string with toml data')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    """
    # Error Checks
    err_msg_type_str = "Only str is allowed for 'toml_str_data'"

    if not isinstance(toml_str_data, str): raise TomlLoadStr(err_msg_type_str, f'\nGot: {repr(toml_str_data)}')

    # Load toml data from str
    try:
        return _tomli.loads(toml_str_data)
    except _tomli.TOMLDecodeError as err_msg: raise TomlLoadStr(err_msg, f'\nGot: {repr(toml_str_data)}')
