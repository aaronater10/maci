# pickledumpbytes
#########################################################################################################
# Imports
import pickle as _pickle  # nosec: B403  # ignore sec checker - upto dev discretion to pickle data
from typing import Any as _Any
from ..error import PickleDumpBytes

#########################################################################################################
# Dump pickle byte string
def pickledumpbytes(data: _Any) -> bytes:
    """
    Dump data to a pickled byte string

    [Example Use]

    pickledumpbytes(data)

    *** Only pickle data you trust! ***

    This is using the native pickle library shipped with the python standard library. For more
    information on the pickle library and official security concerns with pickling, visit: https://docs.python.org/3/library/pickle.html

    Maci docs: https://docs.macilib.org
    """
    # Dump pickle byte data
    try:
        return _pickle.dumps(data)
    except _pickle.PickleError as err_msg: raise PickleDumpBytes(err_msg, f'\nGot: {repr(data)}')  # pragma: no cover  # catch all. inconvenient examples to test
    except TypeError as err_msg: raise PickleDumpBytes(err_msg, f'\nGot: {repr(data)}')
