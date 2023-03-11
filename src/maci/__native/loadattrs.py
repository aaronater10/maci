# loadattrs
#########################################################################################################
# Imports
from typing import NewType as __NewType
from typing import Union as __Union
from ..error import LoadAttrs, Load
from .load import load as __load
from ..data import MaciDataObj as __MaciDataObj

#########################################################################################################
# Import Attributes from File

# Hinting reference name for "CustomClass" to denote a CustomClass can be used to dump data
CustomClass = __NewType('CustomClass', object)

def loadattrs(filename: str, class_object: CustomClass, *, attr_name_dedup: bool=True, encoding: __Union[str, None]=None) -> None:
    """
    Import saved attributes from file back into a custom class. This is done in-place

    Enter filename as str, Pass custom class object.

    [Example Use]

    loadattrs('path/of/filename', 'class_object')

    [Warning]
    Turning OFF 'attr_name_dedup' is not recommended as you gain the ability to overwrite
    your attribute names that already preexist. This also may affect MaciDataObj behavior
    including the ability to overwrite internal dunder names. This feature is meant to protect you from accidentally
    duplicating an attribute name in a file that has already been created.
    """
    # Error Checks
    __err_msg_type_str_filename = "Only str is allowed for filename"
    __err_msg_type_class_obj = "Only a custom class object is allowed for class_object"
    __err_msg_type_maci_obj = "Please use 'load' function to properly import a MaciDataObj object"

    if not isinstance(filename, str): raise LoadAttrs(__err_msg_type_str_filename, f'\nFILE: "{filename}"')
    
    # Verify if Custom Class Obj
    _filter_objects = (str, int, float, bool, list, dict, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)
    if isinstance(class_object, _filter_objects):
        raise LoadAttrs(__err_msg_type_class_obj, f'\nFILE: "{filename}" \nDATA: {class_object}')

    if isinstance(class_object, __MaciDataObj):
        raise LoadAttrs(__err_msg_type_maci_obj, f'\nFILE: "{filename}" \nDATA: {class_object}')

    # Import Attrs from File and Inject into Given Class Object

    # Skip Key
    __skip_object_key = ('_MaciDataObjConstructor', '__maci_obj_format_id')

    # Import Attrs
    try:
        __imported_data = __load(filename, attr_name_dedup=attr_name_dedup, encoding=encoding)
        for key,value in __imported_data.__dict__.items():
            if key.startswith(__skip_object_key): continue
            setattr(class_object, key, value)
    except Load as __err_msg:
        raise LoadAttrs(__err_msg, '')
    except TypeError as __err_msg:
        raise LoadAttrs(__err_msg_type_class_obj, f'\n"{__err_msg}"\nDATA: {class_object}')

    return None
