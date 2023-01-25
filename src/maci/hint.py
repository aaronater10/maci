# hints - Contains hints for data objects
"""
Contains objects for hinting
"""
# Native
from .data import MaciDataObj as __MaciDataObj

__hint_settings = {
    'filename': '',
    'attrib_name_dedup': True,
    '_is_hint_request': True,
}

MaciDataObj = type(__MaciDataObj(**__hint_settings))


# INI
from configparser import ConfigParser
