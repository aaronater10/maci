# pickleloadbytes
#########################################################################################################
# Imports
import pickle as _pickle  # nosec: B403  # ignore sec checker - upto dev discretion to unpickle data
from typing import Any as _Any
from ..error import PickleLoadBytes

#########################################################################################################
# Load pickle byte string
def pickleloadbytes(pickled_byte_data: bytes) -> _Any:
    """
    Load data from a pickled byte string

    [Example Use]

    pickleloadbytes(b'byte string with pickled data')

    *** Only unpickle data you trust! ***

    This is using the native pickle library shipped with the python standard library. For more
    information on the pickle library and official security concerns with pickling, visit: https://docs.python.org/3/library/pickle.html

    Maci docs: https://docs.macilib.org
    """
    # Error Checks
    err_msg_type_bytes = "Only bytes is allowed for 'pickled_byte_data'"

    if not isinstance(pickled_byte_data, bytes): raise PickleLoadBytes(err_msg_type_bytes, f'\nGot: {repr(pickled_byte_data)}')

    # Load pickle byte data
    try:
        return _pickle.loads(pickled_byte_data)  # nosec: B301  # ignore sec checker - upto dev discretion to unpickle data
    except _pickle.PickleError as err_msg: raise PickleLoadBytes(err_msg, f'\nGot: {repr(pickled_byte_data)}')
