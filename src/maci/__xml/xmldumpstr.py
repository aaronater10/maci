# xmldumpstr
#########################################################################################################
# Imports
import xml.etree.ElementTree as __xml_etree
from ..error import XmlDumpStr

#########################################################################################################
# Export xml str
def xmldumpstr(data: __xml_etree.Element) -> str:
    """
    Exports xml Element obj to a string

    Returns a str. Assign the output to var

    [Example Use]

    xmldumpstr(Element)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Check for Error
    __err_msg_etree = f"Only Element is allowed for data"

    if not isinstance(data, __xml_etree.Element): raise XmlDumpStr(__err_msg_etree, f'\nDATA: {data}')

    # Export Data
    return __xml_etree.tostring(data).decode()
