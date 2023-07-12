# xmlload
#########################################################################################################
# Imports
from typing import Union as _Union
import xml.etree.ElementTree as _xml_etree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
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
    err_msg_type_filename = "Only str is allowed for 'filename'"
    err_msg_type_auto_get_root = "Only bool is allowed for 'auto_get_root'"

    if not isinstance(filename, str): raise XmlLoad(err_msg_type_filename, f'\nGot: {repr(filename)}')
    if not isinstance(auto_get_root, bool): raise XmlLoad(err_msg_type_auto_get_root, f'\nGot: {repr(auto_get_root)}')

    # Load File Data
    try:
        if auto_get_root:
            return _xml_etree.parse(filename).getroot()  # nosec: B314  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
        return _xml_etree.parse(filename)  # nosec: B314  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
    except (FileNotFoundError, OSError) as err_msg: raise XmlLoad(err_msg, f'\nGot: {repr(filename)}')
    except _xml_etree.ParseError as err_msg: raise XmlLoad(err_msg, f'\nGot: {repr(filename)}')
