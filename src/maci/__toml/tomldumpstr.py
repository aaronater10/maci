# tomldumpstr
#########################################################################################################
# Imports
import tomli_w as _tomli_w
from ..error import TomlDumpStr
from typing import Dict as _Dict
from typing import Any as _Any

#########################################################################################################
# Dump toml file
def tomldumpstr(
    data: _Dict[str, _Any],
    *,
    multi_line_str: bool=False
) -> str:
    """
    Dumps dict data to toml string

    Returns a toml formatted str. Assign the output to var

    [Example Use]

    tomldumpstr(data)

    This is using the tomli-w library installed as a dependency from pypi.
    For more information on tomli-w, visit: https://pypi.org/project/tomli-w/
    """
    __err_msg_type_str_data = "Only dict is allowed for 'data'"
    __err_msg_type_str_mls = "Only bool is allowed for 'multi_line_str'"

    if not isinstance(data, dict): raise TomlDumpStr(__err_msg_type_str_data, f'\nDATA: {data}')
    if not isinstance(multi_line_str, bool): raise TomlDumpStr(__err_msg_type_str_mls, f'\nDATA: {multi_line_str}')

    try:
        # Dump data to toml str
        return _tomli_w.dumps(data, multiline_strings=multi_line_str)
    except TypeError as __err_msg: raise TomlDumpStr(__err_msg, f'\nDATA:{data}')
    except ValueError as __err_msg: raise TomlDumpStr(__err_msg, f'\nDATA:{data}')