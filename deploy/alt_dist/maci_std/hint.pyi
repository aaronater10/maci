# stub file to document public api class hint types objects
#########################################################################################################
"""
Contains maci and other objects for type hints
"""
#########################################################################################################
# Stub data: Classes for hint objects

# Native
from .data import MaciDataObj as MaciDataObj
from .data import ClassObject as __ClassObject # for type check param hints

# INI
from configparser import ConfigParser as ConfigParser

# XML
from xml.etree.ElementTree import ElementTree as ElementTree  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
from xml.etree.ElementTree import Element as Element  # nosec: B405  # ignore sec checker - upto dev discretion to run provided maci._defuse_xml_stdlib()
