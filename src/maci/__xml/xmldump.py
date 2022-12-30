# xmldump
#########################################################################################################
# Imports
from ..__native.dumpraw import dumpraw
from .xmldumpstr import xmldumpstr
import xml.etree.ElementTree as __xml_etree
from ..error import XmlDump

#########################################################################################################
# Export xml file
def xmldump(filename: str, data: __xml_etree.Element) -> None:
    """
    Exports a new file from xml Element obj as xml data
    
    Enter new filename as str. Pass ElementTree data for output to file
    
    [Example Use]

    xmldump('path/to/filename.xml', Element_data)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Check for Error
    __err_msg_str = f"Only str is allowed for filename"
    __err_msg_etree = f"Only Element is allowed for data"

    if not isinstance(filename, str): raise XmlDump(__err_msg_str, f'\nFILE: "{filename}"')
    if not isinstance(data, __xml_etree.Element): raise XmlDump(__err_msg_etree, f"\nDATA: {data}")

    # Export Data
    try:
        data = xmldumpstr(data)
        dumpraw(filename, data)
    except FileNotFoundError as __err_msg: raise XmlDump(__err_msg, f'\nFILE: "{filename}"')
