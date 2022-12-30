# inibuildmanual
#########################################################################################################
# Imports
from configparser import ConfigParser as __ConfigParser
from configparser import ExtendedInterpolation as __ExtendedInterpolation

#########################################################################################################
# Build manual ini data
def inibuildmanual() -> __ConfigParser:
    """    
    Returns an empty ConfigParser obj to manually build ini data
    
    Assign the output to var

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """
    return __ConfigParser(interpolation=__ExtendedInterpolation())
