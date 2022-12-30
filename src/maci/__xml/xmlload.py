# xmlload
#########################################################################################################
# Imports
import xml.etree.ElementTree as __xml_etree
from ..error import XmlLoad

#########################################################################################################
# Import xml file
def xmlload(filename: str) -> __xml_etree.Element:
    """
    Imports xml data from a file.

    Returns a xml Parsed Element obj with the root. Assign the output to var

    Enter xml file location as str to import.

    [Example Use]

    xmlload('path/to/filename.xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    __err_msg_str = f"Only str is allowed for filename"

    if not isinstance(filename, str): raise XmlLoad(__err_msg_str, f'\nFILE: "{filename}"')

    try: return __xml_etree.parse(filename).getroot()
    except FileNotFoundError as __err_msg: raise XmlLoad(__err_msg, f'\nFILE: "{filename}"')
    except __xml_etree.ParseError as __err_msg: raise XmlLoad(__err_msg, f'\nFILE: "{filename}"')
