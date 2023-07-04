# xmlloadstr
#########################################################################################################
# Imports
import xml.etree.ElementTree as _xml_etree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from ..error import XmlLoadStr

#########################################################################################################
# Import xml str
def xmlloadstr(xml_str_data: str) -> _xml_etree.Element:
    """
    Imports xml data from a string

    Returns a xml Element. Assign the output to var

    [Example Use]

    xmlloadstr('<tag>data</tag>')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Error Checks
    err_msg_str = f"Only str is allowed for 'xml_str_data'"

    if not isinstance(xml_str_data, str): raise XmlLoadStr(err_msg_str, f'\nGot: {repr(xml_str_data)}')

    # Load Str Data
    try: return _xml_etree.fromstring(str(xml_str_data))  # nosec: B314  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
    except _xml_etree.ParseError as err_msg: raise XmlLoadStr(err_msg, f'\nGot: {repr(xml_str_data)}')
