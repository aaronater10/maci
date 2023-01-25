# hints - Contains hints for data objects
"""
Contains objects for hinting
"""
from .data import MaciDataObj as __MaciDataObj

# Native
__hint_settings = {
    'filename': '',
    'attrib_name_dedup': True,
    '_is_hint_request': True,
}

MaciDataObj = type(__MaciDataObj(**__hint_settings))
