# xmldumpstr
#########################################################################################################
# Imports
import xml.etree.ElementTree as _xml_etree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from ..error import XmlDumpStr

#########################################################################################################
# Export xml str
def xmldumpstr(data: _xml_etree.Element, *, encoding: str='utf-8') -> str:
    """
    Exports xml Element object to a string

    Returns a str. Assign the output to var

    [Example Use]

    xmldumpstr(Element)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Error Checks
    err_msg_type_etree = "Only Element is allowed for 'data'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(data, _xml_etree.Element): raise XmlDumpStr(err_msg_type_etree, f'\nGot: {repr(data)}')
    if not isinstance(encoding, (str, type(None))): raise XmlDumpStr(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Export Data
    try: return _xml_etree.tostring(data).decode(encoding=encoding)
    except LookupError: raise XmlDumpStr(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
