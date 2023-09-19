# xmldump
#########################################################################################################
# Imports
from typing import Union as _Union
from pathlib import Path as _PathObj
from .._native.dumpraw import dumpraw as _dumpraw
from .xmldumpstr import xmldumpstr as _xmldumpstr
from xml.etree.ElementTree import ElementTree as _ElementTree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from xml.etree.ElementTree import Element as _Element  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from ..error import XmlDump, DumpRaw

#########################################################################################################
# Export xml file
def xmldump(filename: _Union[str, _PathObj], data: _Union[_ElementTree, _Element], *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Dumps xml data to a file from xml etree ElementTree or Element object
    
    [Example: Usage]

    xmldump('path/to/filename.xml', data)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_str = "Only str is allowed for 'filename'"
    err_msg_etree = "Only ElementTree|Element is allowed for 'data'"
    err_msg_type_str_append = "Only bool is allowed for 'append'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, (str, _PathObj)): raise XmlDump(err_msg_str, f'\nGot: {repr(filename)}')
    if not isinstance(data, (_ElementTree, _Element)): raise XmlDump(err_msg_etree, f"\nGot: {repr(data)}")
    if not isinstance(append, bool): raise XmlDump(err_msg_type_str_append, f'\nGot: {repr(append)}')
    if not isinstance(encoding, (str, type(None))): raise XmlDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Export Data
    try:
        # If ElementTree, convert to Element by getting root
        if isinstance(data, _ElementTree):
            data = data.getroot()

        data_str = _xmldumpstr(data)
        _dumpraw(filename, data_str, encoding=encoding, append=append)
    except DumpRaw as err_msg: raise XmlDump(err_msg) from None
