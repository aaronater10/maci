# hints
"""
Contains maci and other objects for type hints
"""

# Native
from .data import MaciDataObj
from .data import ClassObject as __ClassObject # for type check param hints

# INI
from configparser import ConfigParser

# XML
from xml.etree.ElementTree import ElementTree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from xml.etree.ElementTree import Element  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
