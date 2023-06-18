# hints - Contains hints for data objects
"""
Contains objects for hinting
"""
# Native
from .data import MaciDataObj as __MaciDataObj

__hint_settings = {
    'filename': '',
    'attr_name_dedup': True,
    '_is_hint_request': True,
}
MaciDataObj = type(__MaciDataObj(**__hint_settings, encoding=None))


# INI
from configparser import ConfigParser as __ConfigParser
ConfigParser = __ConfigParser


# XML
from xml.etree.ElementTree import ElementTree as __ElementTree
from xml.etree.ElementTree import Element as __Element
ElementTree = __ElementTree
Element = __Element
