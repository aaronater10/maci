# inibuildmanual
#########################################################################################################
# Imports
from configparser import ConfigParser as _ConfigParser
from configparser import ExtendedInterpolation as _ExtendedInterpolation

#########################################################################################################
# Build manual ini data
def inibuildmanual() -> _ConfigParser:
    """    
    Returns an empty ConfigParser object to manually build ini data
    
    Assign the output to var

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html
    """
    return _ConfigParser(interpolation=_ExtendedInterpolation())
