# tomldump
#########################################################################################################
# Imports
import tomli_w as _tomli_w
from ..error import TomlDump
from ..__native.dumpraw import dumpraw as _dumpraw
from typing import Dict as _Dict
from typing import Any as _Any

#########################################################################################################
# Dump toml file
def tomldump(
    filename: str,
    data: _Dict[str, _Any],
    *,
    append: bool=False,
    multi_line_str: bool=False
) -> None:
    """
    Dumps a new file from dict to toml data.

    Enter filename as str. Pass data for output to file

    [Example Use]

    tomldump('path/to/filename.toml', data)    

    This is using the tomli-w library installed as a dependency from pypi.
    For more information on tomli-w, visit: https://pypi.org/project/tomli-w/
    """
    __err_msg_type_str_data = "Only dict is allowed for 'data'"
    __err_msg_type_str_append = "Only bool is allowed for 'append'"
    __err_msg_type_str_mls = "Only bool is allowed for 'multi_line_str'"

    if not isinstance(data, dict): raise TomlDump(__err_msg_type_str_data, f'\nFILE: "{filename}" \nDATA: {data}')
    if not isinstance(append, bool): raise TomlDump(__err_msg_type_str_append, f'\nFILE: "{filename}" \nDATA: {append}')
    if not isinstance(multi_line_str, bool): raise TomlDump(__err_msg_type_str_mls, f'\nFILE: "{filename}" \nDATA: {multi_line_str}')

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'ab' if append else 'wb'

    try:
        # Dump data to toml file
        with open(filename, write_mode) as f:
            _tomli_w.dump(data, f, multiline_strings=multi_line_str)
            if write_mode == 'ab': _dumpraw(filename, '', append=True)
    except TypeError as __err_msg: raise TomlDump(__err_msg, f'\nFILE: "{filename}" \nDATA:{data}')
    except ValueError as __err_msg: raise TomlDump(__err_msg, f'\nFILE: "{filename}" \nDATA:{data}')
    except FileNotFoundError as __err_msg: raise TomlDump(__err_msg, f'\nFILE: "{filename}"')
