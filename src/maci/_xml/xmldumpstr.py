# xmldumpstr
#########################################################################################################
# Imports
import sys
import xml.etree.ElementTree as _xml_etree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from ..error import XmlDumpStr

#########################################################################################################
# Export xml str
def xmldumpstr(data: _xml_etree.Element, *, pretty: bool=True, full_doc: bool=True, encoding: str='utf-8') -> str:
    """
    Dumps xml data to a string from xml etree Element object

    Returns a xml formatted str

    [Example: Usage]

    xmldumpstr(data)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_etree = "Only Element is allowed for 'data'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(data, _xml_etree.Element): raise XmlDumpStr(err_msg_type_etree, f'\nGot: {repr(data)}')
    if not isinstance(encoding, (str, type(None))): raise XmlDumpStr(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Export Data
    if (sys.version_info >= (3, 9)) and pretty:  # pragma: no cover  # etree indent only supported py39+
        space_level = 4
        _xml_etree.indent(data, space=" "*space_level)
    
    encoding = sys.getdefaultencoding() if encoding is None else encoding

    try:
        return _xml_etree.tostring(data, encoding=encoding, xml_declaration=full_doc).decode(encoding=encoding)
    except LookupError: raise XmlDumpStr(err_msg_type_encoding, f'\nGot: {repr(encoding)}')
