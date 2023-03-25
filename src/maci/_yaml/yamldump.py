# yamldump
#########################################################################################################
# Imports
from typing import Any as __Any
from typing import Union as __Union
import yaml as __yaml
from ..error import YamlDump

#########################################################################################################
# Export yaml file
def yamldump(filename: str, data: __Any, *, append: bool=False, encoding: __Union[str, None]=None) -> None:
    """
    Exports a new file from python data type to yaml data.
    
    Enter new filename as str. Pass any general data for output to file
    
    [Example Use]

    yamldump('path/to/filename.yml', data)    

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    """
    __err_msg_type_str_append = "Only bool is allowed for 'append'"

    if not isinstance(append, bool): raise YamlDump(__err_msg_type_str_append, f'\nFILE: "{filename}" \nDATA: {append}')

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    # Export data to yaml file
    try:
        with open(filename, write_mode, encoding=encoding) as f:
            __yaml.safe_dump(data, f)
    except __yaml.representer.RepresenterError as __err_msg: raise YamlDump(__err_msg, f'\nFILE: "{filename}" \nDATA: {data}')
    except TypeError as __err_msg: raise YamlDump(__err_msg, f'\nFILE: "{filename}" \nDATA: {data}')
    except ValueError as __err_msg: raise YamlDump(__err_msg, f'\nFILE: "{filename}" \nDATA: {data}')
    except FileNotFoundError as __err_msg: raise YamlDump(__err_msg, f'\nFILE: "{filename}"')
