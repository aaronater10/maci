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
    # Import yaml str
    try:       
        return __yaml.safe_load(yaml_str_data)
    except FileNotFoundError as __err_msg: raise YamlLoadStr(__err_msg, f'\nDATA: {yaml_str_data}')
    except OSError as __err_msg: raise YamlLoadStr(__err_msg, f'\nDATA: {yaml_str_data}')
    except __yaml.scanner.ScannerError as __err_msg: raise YamlLoadStr(__err_msg, f'\nDATA: {yaml_str_data}')
    except __yaml.parser.ParserError as __err_msg: raise YamlLoadStr(__err_msg, f'\nDATA: {yaml_str_data}')
    except ValueError as __err_msg: raise YamlLoadStr(__err_msg, f'\nDATA: {yaml_str_data}')
    except TypeError as __err_msg: raise YamlLoadStr(__err_msg, f'\nDATA: {yaml_str_data}')
    except AttributeError as __err_msg: raise YamlLoadStr(__err_msg, f'\nDATA: {yaml_str_data}')
