# xmldump
#########################################################################################################
# Imports
from typing import Union as _Union
from .._native.dumpraw import dumpraw
from .xmldumpstr import xmldumpstr
from xml.etree.ElementTree import ElementTree as _ElementTree
from xml.etree.ElementTree import Element as _Element
from ..error import XmlDump

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
    __err_msg_str = "Only str is allowed for 'filename'"
    __err_msg_etree = "Only ElementTree|Element is allowed for 'data'"
    __err_msg_type_str_append = "Only bool is allowed for 'append'"

    if not isinstance(filename, str): raise XmlDump(__err_msg_str, f'\nGot: "{filename}"')
    if not isinstance(data, (_ElementTree, _Element)): raise XmlDump(__err_msg_etree, f"\nGot: {data}")
    if not isinstance(append, bool): raise XmlDump(__err_msg_type_str_append, f'\nGot: {append}')

    # Export Data
    try:
        # If ElementTree, convert to Element by getting root
        if isinstance(data, _ElementTree):
            data = data.getroot()

        data = xmldumpstr(data)
        dumpraw(filename, data, encoding=encoding, append=append)
    except FileNotFoundError as __err_msg: raise XmlDump(__err_msg, f'\nFILE: "{filename}"')
