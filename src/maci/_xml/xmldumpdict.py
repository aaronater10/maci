# xmldumpdict
#########################################################################################################
# Imports
from typing import Dict as _Dict
from typing import Any as _Any
from typing import Union as _Union
from pathlib import Path as _PathObj
import xmltodict as _xmltodict  # type: ignore  # ignoring type checker for ext lib
from .._native.dumpraw import dumpraw as _dumpraw
from ..error import XmlDumpDict

#########################################################################################################
# Dump xml file
def xmldumpdict(filename: _Union[str, _PathObj], data: _Dict[str, _Any], *, append: bool=False, pretty: bool=True, full_doc: bool=True) -> None:
    """
    Dumps xml data to a file from dict

    [Example Use]

    xmldumpdict('path/to/filename.xml', data) 

    This is using the xmltodict library installed as a dependency from pypi.
    For more information on xmltodict, visit: https://pypi.org/project/xmltodict/
    
    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_file = "Only str is allowed for 'filename'"
    err_msg_type_data = "Only dict is allowed for 'data'"
    err_msg_type_append = "Only bool is allowed for 'append'"
    err_msg_type_pretty = "Only bool is allowed for 'pretty'"
    err_msg_type_full_doc = "Only bool is allowed for 'full_doc'"

    if not isinstance(filename, (str, _PathObj)): raise XmlDumpDict(err_msg_type_file, f'\nGot: {repr(filename)}')
    if not isinstance(data, dict): raise XmlDumpDict(err_msg_type_data, f'\nGot: {repr(data)}')
    if not isinstance(append, bool): raise XmlDumpDict(err_msg_type_append, f'\nGot: {repr(append)}')
    if not isinstance(pretty, bool): raise XmlDumpDict(err_msg_type_pretty, f'\nGot: {repr(pretty)}')
    if not isinstance(full_doc, bool): raise XmlDumpDict(err_msg_type_full_doc, f'\nGot: {repr(full_doc)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Set Write Mode: 'a' = append, 'w' = write
    write_mode = 'a' if append else 'w'

    try:
        # Dump data to xml file
        file_data: _Any  # ignore type checker
        with open(filename, write_mode) as file_data:
            if write_mode == 'a': _dumpraw(filename, '', append=True)
            _xmltodict.unparse(input_dict=data, output=file_data, pretty=pretty, full_document=full_doc)
    except TypeError as err_msg: raise XmlDumpDict(err_msg, f'\nFile: {repr(filename)} \nGot: {repr(data)}')
    except (FileNotFoundError, OSError) as err_msg: raise XmlDumpDict(err_msg, f'\nGot: {repr(filename)}')
