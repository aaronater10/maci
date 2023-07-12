# tomldumpstr
#########################################################################################################
# Imports
import tomli_w as _tomli_w
from typing import Dict as _Dict
from typing import Any as _Any
from ..error import TomlDumpStr

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
    err_msg_type_str_data = "Only dict is allowed for 'data'"
    err_msg_type_str_mls = "Only bool is allowed for 'multi_line_str'"

    if not isinstance(data, dict): raise TomlDumpStr(err_msg_type_str_data, f'\nGot: {repr(data)}')
    if not isinstance(multi_line_str, bool): raise TomlDumpStr(err_msg_type_str_mls, f'\nGot: {repr(multi_line_str)}')

    try:
        # Dump data to toml str
        return _tomli_w.dumps(data, multiline_strings=multi_line_str)
    except TypeError as err_msg: raise TomlDumpStr(err_msg, f'\nGot: {repr(data)}')
