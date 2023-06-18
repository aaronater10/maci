# xmlload
#########################################################################################################
# Imports
from typing import Union as _Union
import xml.etree.ElementTree as _xml_etree
from ..error import XmlLoad

#########################################################################################################
# Import xml file
def xmlload(filename: str, *, auto_get_root: bool=True) -> _Union[_xml_etree.Element, _xml_etree.ElementTree]:
    """
    Imports xml data from a file.

    Returns the root Element object of the ElementTree parsed from a xml file by default. Assign the output to var

    Enter xml file location as str to import.

    [Example Use]

    xmlload('path/to/filename.xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Error Checks
    err_msg_str = "Only str is allowed for 'filename'"

    if not isinstance(filename, str): raise XmlLoad(err_msg_str, f'\nGot: {repr(filename)}')

    # Load File Data
    try:
        if auto_get_root:
            return _xml_etree.parse(filename).getroot()
        return _xml_etree.parse(filename)
    except FileNotFoundError as __err_msg: raise XmlLoad(__err_msg, f'\nGot: {repr(filename)}')
    except _xml_etree.ParseError as __err_msg: raise XmlLoad(__err_msg, f'\nGot: {repr(filename)}')
