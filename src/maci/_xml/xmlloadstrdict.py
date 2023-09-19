# xmlloadstrdict
#########################################################################################################
# Imports
from typing import Union as _Union
from typing import Any as _Any
from typing import OrderedDict as _OrderedDict
import xmltodict as _xmltodict  # type: ignore  # ignoring type checker for ext lib
from xml.parsers.expat import ExpatError
from ..error import XmlLoadStrDict

#########################################################################################################
# Load xml string
def xmlloadstrdict(xml_str_data: str) -> _OrderedDict[str, _Any]:
    """
    Loads xml data from a string

    Returns dict representing your xml data

    [Example: Usage]

    xmlloadstrdict('<tag>data</tag>')

    This is using the xmltodict library installed as a dependency from pypi.
    For more information on xmltodict, visit: https://pypi.org/project/xmltodict/
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_str = f"Only str is allowed for 'xml_str_data'"

    if not isinstance(xml_str_data, str): raise XmlLoadStrDict(err_msg_str, f'\nGot: {repr(xml_str_data)}')
    
    # Load Str Data
    try: return _xmltodict.parse(xml_input=xml_str_data)
    except (ExpatError) as err_msg: raise XmlLoadStrDict(err_msg, f'\nGot: {repr(xml_str_data)}')
