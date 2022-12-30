# xmlloadstr
#########################################################################################################
# Imports
import xml.etree.ElementTree as __xml_etree
from ..error import XmlLoadStr

#########################################################################################################
# Import xml str
def xmlloadstr(data: str) -> __xml_etree.Element:
    """
    Imports xml data from a string

    Returns a xml Element. Assign the output to var

    [Example Use]

    xmlloadstr('<tag>data</tag>')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    __err_msg_str = f"Only str is allowed for data"

    if not isinstance(data, str): raise XmlLoadStr(__err_msg_str, f'\nDATA: {repr(data)}')
    try:
        return __xml_etree.fromstring(str(data))
    except __xml_etree.ParseError as __err_msg: raise XmlLoadStr(__err_msg, f'\nDATA: {data}')
