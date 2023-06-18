# xmldump
#########################################################################################################
# Imports
from typing import Union as _Union
from .._native.dumpraw import dumpraw
from .xmldumpstr import xmldumpstr
from xml.etree.ElementTree import ElementTree as _ElementTree
from xml.etree.ElementTree import Element as _Element
from ..error import XmlDump, DumpRaw

#########################################################################################################
# Export xml file
def xmldump(filename: str, data: _Union[_ElementTree, _Element], *, append: bool=False, encoding: _Union[str, None]=None) -> None:
    """
    Exports a new file from xml ElementTree or Element object as xml data
    
    Enter new filename as str. Pass ElementTree data for output to file
    
    [Example Use]

    xmldump('path/to/filename.xml', Element_data)

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    # Check for Error
    err_msg_str = "Only str is allowed for 'filename'"
    err_msg_etree = "Only ElementTree|Element is allowed for 'data'"
    err_msg_type_str_append = "Only bool is allowed for 'append'"
    err_msg_type_encoding = "Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(filename, str): raise XmlDump(err_msg_str, f'\nGot: {repr(filename)}')
    if not isinstance(data, (_ElementTree, _Element)): raise XmlDump(err_msg_etree, f"\nGot: {repr(data)}")
    if not isinstance(append, bool): raise XmlDump(err_msg_type_str_append, f'\nGot: {repr(append)}')
    if not isinstance(encoding, (str, type(None))): raise XmlDump(err_msg_type_encoding, f'\nGot: {repr(encoding)}')

    # Export Data
    try:
        # If ElementTree, convert to Element by getting root
        if isinstance(data, _ElementTree):
            data = data.getroot()

        data = xmldumpstr(data)
        dumpraw(filename, data, encoding=encoding, append=append)
    except FileNotFoundError as __err_msg: raise XmlDump(__err_msg, f'\nFILE: "{filename}"')
    except DumpRaw as _err_msg: raise XmlDump(_err_msg) from None
