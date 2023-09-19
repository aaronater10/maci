# inibuildauto
#########################################################################################################
# Imports
from configparser import ConfigParser as _ConfigParser
from configparser import ExtendedInterpolation as _ExtendedInterpolation
from typing import Dict as _Dict
from typing import Any as _Any
from ..error import IniBuildAuto

#########################################################################################################
# Auto Build ini data
def inibuildauto(data: _Dict[str, _Dict[str, _Any]]) -> _ConfigParser:
    """
    Auto builds ini data object from dict

    Returns a ConfigParser object with your data

    Note: All sub-values are converted to strings naturally by the library. However, if your sub-value
    contains a 'NoneType', this function will also auto-convert that to a string for you.

    Enter correctly structured dict to build data

    [Example: ini dict structure]

    {
        'section1': {'key1': 1},

        'section2': {'key2': 2}   
    }

    [Example: Usage]

    var = inibuildauto(data)

    This is using the native configparser library shipped with the python standard library. Using ConfigParser method
    with ExtendedInterpolation enabled by default. For more information on the configparser library, 
    visit: https://docs.python.org/3/library/configparser.html

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_dict_type = f"Only dict is allowed for 'data'"
    err_msg_dict_struct = r"Please use correct dict structure: {'k':{'k':v}} "

    if not isinstance(data, dict): raise IniBuildAuto(err_msg_dict_type, f'\nGot: {repr(data)}')


    # Auto Build INI data structure
    __ini_data = _ConfigParser(interpolation=_ExtendedInterpolation())

    try:
        for section,dict_value in data.items():
            if None in dict_value.values():
                for sub_key,sub_value in dict_value.items():
                    if sub_value is None: # pragma: no branch
                        dict_value[sub_key] = 'None'
            __ini_data[section] = dict_value
        return __ini_data
    except AttributeError as __err_msg: raise IniBuildAuto(f'{__err_msg} - {err_msg_dict_struct}', f'\nGot: {repr(data)}')
