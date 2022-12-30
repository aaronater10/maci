# loadattrs
#########################################################################################################
# Imports
from ..error import LoadAttrs, Load
from .load import load as __load
from .load import MaciFileData as __MaciFileData

#########################################################################################################
# Import Attributes from File
class __MaciDummy:
    class Class: """dummy class for hinting"""

def loadattrs(filename: str, class_object: '__MaciDummy.Class') -> None:
    """
    Import saved attributes from file back into a custom class. This is done in-place

    Enter filename as str, Pass custom class object.

    [Example Use]

    loadattrs('path/of/filename', 'class_object')
    """
    # Error Checks
    __err_msg_type_str_filename = "Only str is allowed for filename"
    __err_msg_type_class_obj = "Only a custom class object is allowed for class_object"
    __err_msg_type_maci_obj = "Please use 'load' function to properly import a MaciFileData object"

    if not isinstance(filename, str): raise LoadAttrs(__err_msg_type_str_filename, f'\nFILE: "{filename}"')
    
    # Verify if Custom Class Obj
    _filter_objects = (str, int, float, bool, list, dict, tuple, set, type(None), bytes, complex, range, frozenset, bytearray, memoryview)
    if isinstance(class_object, _filter_objects):
        raise LoadAttrs(__err_msg_type_class_obj, f'\nFILE: "{filename}" \nDATA: {class_object}')

    if isinstance(class_object, __MaciFileData):
        raise LoadAttrs(__err_msg_type_maci_obj, f'\nFILE: "{filename}" \nDATA: {class_object}')

    # Import Attrs from File and Inject into Given Class Object

    # Skip Key
    __skip_object_key = ('_MaciFileData', '__maci_file_format_id')

    # Import Attrs
    try:
        __imported_data = __load(filename)
        for key,value in __imported_data.__dict__.items():
            if key.startswith(__skip_object_key): continue
            setattr(class_object, key, value)
    except Load as __err_msg:
        raise LoadAttrs(__err_msg, '')

    return None
