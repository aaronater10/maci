# xmlbuildmanual
#########################################################################################################
# Imports
import xml.etree.ElementTree as _xml_etree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from types import ModuleType as _ModuleType

#########################################################################################################
# Build manual xml data
def xmlbuildmanual() -> _ModuleType:
    """
    Returns an empty xml ElementTree module object to manually build xml etree data

    Returns etree -> Module('xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    
    Maci docs: https://docs.macilib.org
    """
    return _xml_etree
