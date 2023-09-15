# xmldumpstrdict
#########################################################################################################
# Imports
from typing import Dict as _Dict
from typing import Any as _Any
import xmltodict as _xmltodict  # type: ignore  # ignoring type checker for ext lib
from .._native.dumpraw import dumpraw as _dumpraw
from ..error import XmlDumpStrDict

#########################################################################################################
# Dump xml string
def xmldumpstrdict(data: _Dict[str, _Any], *, pretty: bool=True, full_doc: bool=True) -> str:
    """
    Dumps dict data to xml string

    Returns a xml formatted str

    [Example Use]

    xmldumpstrdict(data)

    This is using the xmltodict library installed as a dependency from pypi.
    For more information on xmltodict, visit: https://pypi.org/project/xmltodict/
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_data = "Only dict is allowed for 'data'"
    err_msg_type_pretty = "Only bool is allowed for 'pretty'"
    err_msg_type_full_doc = "Only bool is allowed for 'full_doc'"

    if not isinstance(data, dict): raise XmlDumpStrDict(err_msg_type_data, f'\nGot: {repr(data)}')
    if not isinstance(pretty, bool): raise XmlDumpStrDict(err_msg_type_pretty, f'\nGot: {repr(pretty)}')
    if not isinstance(full_doc, bool): raise XmlDumpStrDict(err_msg_type_full_doc, f'\nGot: {repr(full_doc)}')

    try:
        # Dump data to xml string
        return _xmltodict.unparse(input_dict=data, output=None, pretty=pretty, full_document=full_doc)        
    except TypeError as err_msg: raise XmlDumpStrDict(err_msg, f'\nGot: {repr(data)}')
