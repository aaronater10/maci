# loadstr
#########################################################################################################
# Imports
from .load import MaciFileData
from ..error import LoadStr

#########################################################################################################
# Import py Data from String
def loadstr(py_str_data: str) -> 'MaciFileData':
    """
    Imports python data from a string.

    Returns a class of attributes. Assign the output to var

    Enter python data string as str to import.

    Accepted data types: str, int, float, bool, list, dict, tuple, set, nonetype, bytes

    Returns None if empty

    [Example Use]

    loadstr("data1 = 'value1'\\ndata2 = "value2")
    """
    ...