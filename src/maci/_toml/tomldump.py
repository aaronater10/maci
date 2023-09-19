# tomldump
#########################################################################################################
# Imports
import tomli_w as _tomli_w
from typing import Dict as _Dict
from typing import Any as _Any
from typing import Union as _Union
from pathlib import Path as _PathObj
from .._native.dumpraw import dumpraw as _dumpraw
from ..error import TomlDump

#########################################################################################################
# Dump toml file
def tomldump(
    filename: _Union[str, _PathObj],
    data: _Dict[str, _Any],
    *,
    append: bool=False,
    multi_line_str: bool=False
) -> None:
    """
    Dumps toml data to a file from dict

    [Example: Usage]

    tomldump('path/to/filename.toml', data)

    This is using the tomli-w library installed as a dependency from pypi.
    For more information on tomli-w, visit: https://pypi.org/project/tomli-w/

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_data = "Only dict is allowed for 'data'"
    err_msg_type_append = "Only bool is allowed for 'append'"
    err_msg_type_mls = "Only bool is allowed for 'multi_line_str'"

    if not isinstance(filename, (str, _PathObj)): raise TomlDump(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(data, dict): raise TomlDump(err_msg_type_data, f'\nGot: {repr(data)}')
    if not isinstance(append, bool): raise TomlDump(err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(multi_line_str, bool): raise TomlDump(err_msg_type_mls, f'\nGot: {repr(multi_line_str)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'ab' if append else 'wb'

    try:
        # Dump data to toml file
        file_data: _Any  # ignore type checker
        with open(filename, write_mode) as file_data:
            _tomli_w.dump(data, file_data, multiline_strings=multi_line_str)
            if write_mode == 'ab': _dumpraw(filename, '', append=True)
    except TypeError as err_msg: raise TomlDump(err_msg, f'\nFile: {repr(filename)} \nGot: {repr(data)}')
    except (FileNotFoundError, OSError) as err_msg: raise TomlDump(err_msg, f'\nGot: {repr(filename)}')
