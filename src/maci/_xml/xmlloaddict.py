# xmlloaddict
#########################################################################################################
# Imports
from typing import Any as _Any
from typing import OrderedDict as _OrderedDict
from typing import Union as _Union
from pathlib import Path as _PathObj
import xmltodict as _xmltodict  # type: ignore  # ignoring type checker for ext lib
from xml.parsers.expat import ExpatError
from ..error import XmlLoadDict

#########################################################################################################
# Load xml file
def xmlloaddict(filename: _Union[str, _PathObj]) -> _OrderedDict[str, _Any]:
    """
    Loads xml data from a file

    Returns dict representing your xml data

    [Example: Usage]

    xmlloaddict('path/to/filename.xml')

    This is using the xmltodict library installed as a dependency from pypi.
    For more information on xmltodict, visit: https://pypi.org/project/xmltodict/
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_filename = "Only str is allowed for 'filename'"

    if not isinstance(filename, (str, _PathObj)): raise XmlLoadDict(err_msg_type_filename, f'\nGot: {repr(filename)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Load File Data
    try:
        with open(filename, 'rb') as file_data:
            return _xmltodict.parse(xml_input=file_data)
    except (FileNotFoundError, OSError) as err_msg: raise XmlLoadDict(err_msg, f'\nGot: {repr(filename)}')
    except ExpatError as err_msg: raise XmlLoadDict(err_msg, f'\nGot: {repr(filename)}')
