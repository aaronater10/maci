# yamlloadstr
#########################################################################################################
# Imports
from typing import Any as __Any
import yaml as __yaml
from ..error import YamlLoadStr

#########################################################################################################
# Import yaml str
def yamlloadstr(yaml_str_data: str) -> __Any:
    """
    Imports yaml data from a string

    Returns data with matching python data type. Assign the output to var

    Enter yaml string as str to import.

    [Example Use]

    yamlloadstr('string with yaml data')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    """
    # Error Checks
    __err_msg_type_str = "Only str is allowed for 'yaml_str_data'"

    if not isinstance(yaml_str_data, str): raise YamlLoadStr(__err_msg_type_str, f'\nGot: {repr(yaml_str_data)}')

    # Import yaml str
    try:       
        return __yaml.safe_load(yaml_str_data)
    except __yaml.error.YAMLError as __err_msg: raise YamlLoadStr(__err_msg, f'\nGot: {yaml_str_data}')
