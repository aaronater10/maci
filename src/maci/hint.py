# hints
"""
Contains maci and other objects for type hints
"""

# Native
from .data import MaciDataObj
from .data import CustomClass as __CustomClass # for type check param hints

# INI
from configparser import ConfigParser

# XML
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
