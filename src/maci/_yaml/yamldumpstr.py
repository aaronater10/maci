# yamldumpstr
#########################################################################################################
# Imports
from typing import Any as __Any
import yaml as __yaml  # type: ignore  # ignoring type checker for ext lib
from ..error import YamlDumpStr

#########################################################################################################
# Export yaml str
def yamldumpstr(data: __Any) -> str:
    """
    Exports python data type to yaml string

    Returns a yaml formatted str. Assign the output to var

    [Example Use]

    yamldumpstr(data)

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_dump" method, which only supports standard YAML tags and cannot represent an arbitrary Python object.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    
    """
    # Export data to yaml str
    try: return __yaml.safe_dump(data, stream=None).rstrip() # Strip trailing \n, yaml parser adds this automatically
    except __yaml.error.YAMLError as __err_msg: raise YamlDumpStr(__err_msg, f'\nGot: {repr(data)}')
