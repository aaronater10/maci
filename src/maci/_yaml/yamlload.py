# yamlload
#########################################################################################################
# Imports
from typing import Any as __Any
from typing import Union as __Union
import yaml as __yaml
from ..error import YamlLoad

#########################################################################################################
# Import yaml file
def yamlload(filename: str, *, encoding: __Union[str, None]=None) -> __Any:
    """
    Imports yaml data from a file.

    Returns data with matching python data type. Assign the output to var

    Enter yaml file location as str to import.

    [Example Use]

    yamlload('path/to/filename.yml')

    This is using the PyYAML framework installed as a dependency from pypi. It is only using the
    "safe_load" method to protect from untrusted input.
    For more information on PyYAML, visit: https://pypi.org/project/PyYAML/
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise YamlLoad(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(encoding, (str, type(None))): raise YamlLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')


    # Import yaml file
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return __yaml.safe_load(f)
    except FileNotFoundError as __err_msg: raise YamlLoad(__err_msg, f'\nFILE: "{filename}"')
    except OSError as __err_msg: raise YamlLoad(__err_msg, f'\nFILE: "{filename}"')
    except __yaml.scanner.ScannerError as __err_msg: raise YamlLoad(__err_msg, f'\nFILE: "{filename}"')
    except __yaml.parser.ParserError as __err_msg: raise YamlLoad(__err_msg, f'\nFILE: "{filename}"')
    except __yaml.reader.ReaderError as __err_msg: raise YamlLoad(__err_msg, f'\nFILE: "{filename}"')
    except ValueError as __err_msg: raise YamlLoad(__err_msg, f'\nFILE: "{filename}"')
    except TypeError as __err_msg: raise YamlLoad(__err_msg, f'\nFILE: "{filename}"')
    except LookupError: raise YamlLoad(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
