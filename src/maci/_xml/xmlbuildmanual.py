# xmlbuildmanual
#########################################################################################################
# Imports
import xml.etree.ElementTree as _xml_etree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from types import ModuleType as _ModuleType

#########################################################################################################
# Build manual xml data
def xmlbuildmanual() -> _ModuleType:
    """
    Returns a xml ElementTree module object to build/work with xml data
    
    Assign the output to var -> Module('xml')

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    return _xml_etree
