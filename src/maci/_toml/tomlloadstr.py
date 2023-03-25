# tomlloadstr
#########################################################################################################
# Imports
import tomli as _tomli
from ..error import TomlLoadStr
from typing import Dict as _Dict
from typing import Any as _Any

#########################################################################################################
# Load toml file
def tomlloadstr(data: str) -> _Dict[str, _Any]:
    """
    Load toml data from a string

    Returns dict data with matching python data types. Assign the output to var

    [Example Use]

    tomlloadstr('string with toml data')

    This is using the tomli library installed as a dependency from pypi.
    For more information on tomli, visit: https://pypi.org/project/tomli/
    """
    __err_msg_type_str = "Only str is allowed for 'data'"

    if not isinstance(data, str): raise TomlLoadStr(__err_msg_type_str, f'\nDATA: {data}')

    # Load toml data from str
    try:
        return _tomli.loads(data)
    except TypeError as _err_msg: raise TomlLoadStr(_err_msg, f'\nDATA:{data}')
    except _tomli.TOMLDecodeError as _err_msg: raise TomlLoadStr(_err_msg, f'\nDATA:{data}')
