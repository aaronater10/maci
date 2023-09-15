# loadattrs
#########################################################################################################
# Imports
from typing import Union as _Union
from pathlib import Path as _PathObj
from ..error import LoadAttrs, Load
from .load import load as _load
from ..data import MaciDataObj as _MaciDataObj
from ..hint import __ClassObject  # type: ignore  # ignoring attr export

#########################################################################################################
# Import Attributes from File
def loadattrs(filename: _Union[str, _PathObj], class_object: __ClassObject, *, encoding: _Union[str, None]=None, attr_name_dedup: bool=False, _ignore_maci_attr_check: bool=True) -> None:
    """
    Load attribute data from file into a custom class/object. This is done in-place

    [Example: Usage]

    loadattrs('path/of/filename.any', custom_object)

    [Warning] Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_filename = "Only str is allowed for 'filename'"
    err_msg_type_class_obj = "Only a custom ClassObject is allowed for 'class_object'"
    err_msg_type_maci_obj = "Please use 'load' function to properly import a 'MaciDataObj' object"

    if not isinstance(filename, (str, _PathObj)): raise LoadAttrs(err_msg_type_filename, f'\nGot: {repr(filename)}')

    # Convert filename to str to catch Path objects
    filename = str(filename)

    # Verify if Custom Class Obj
    _filter_objects = (str, int, float, bool, list, dict, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)
    if isinstance(class_object, _filter_objects):
        raise LoadAttrs(err_msg_type_class_obj, f'\nGot: {repr(class_object)}')

    if isinstance(class_object, _MaciDataObj):
        raise LoadAttrs(err_msg_type_maci_obj, f'\nGot: {repr(class_object)}')

    if isinstance(class_object, type(_MaciDataObj)):
        raise LoadAttrs(err_msg_type_maci_obj, f'\nGot: {repr(class_object)}')

    # Import Attrs from File and Inject into Given Class Object

    # Skip Key
    skip_object_key = ('_MaciDataObjConstructor', '__maci_obj_format_id')

    # Import Attrs
    try:
        imported_data = _load(filename, attr_name_dedup=attr_name_dedup, encoding=encoding, _ignore_maci_attr_check=_ignore_maci_attr_check)
        for key,value in imported_data.__dict__.items():
            if key.startswith(skip_object_key): continue
            setattr(class_object, key, value)
    except Load as err_msg:
        raise LoadAttrs(err_msg, '')

    return None
