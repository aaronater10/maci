# xmlbuildmanual
#########################################################################################################
# Imports
import xml.etree.ElementTree as __xml_etree

#########################################################################################################
# Build manual xml data
def xmlbuildmanual() -> __xml_etree:
    """
    Returns an empty xml ElementTree obj to build/work with xml data
    
    Assign the output to var

    This is using the native xml library via etree shipped with the python standard library.
    For more information on the xml.etree api, visit: https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree
    """
    return __xml_etree
