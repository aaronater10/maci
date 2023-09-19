# exceptions: pickle - Tests
from src import maci
import pytest


################################################################
# TESTS

### pickledumpbytes ###

# 1. Pickle Dump Bytes - Type Checks
# NO EXCEPTIONS AVAILABLE TO TEST AT THIS TIME


# 2. Pickle Dump Bytes - Unsupported Options or Data
def test2_exceptions_pickledumpbytes_opts_data():
    # Tests
    with pytest.raises(maci.error.PickleDumpBytes):
        maci.pickledumpbytes(data=maci.error)    


### pickleloadbytes ###

# 1. Pickle Load Bytes - Type Checks
def test1_exceptions_pickleloadbytes_types():
    # Tests
    with pytest.raises(maci.error.PickleLoadBytes):
        maci.pickleloadbytes(pickled_byte_data=1.0)


# 2. Pickle Load Bytes - Unsupported Options or Data
def test2_exceptions_pickleloadbytes_opts_data():
    bad_data = b'\x80\x03\x00.'
    
    # Tests
    with pytest.raises(maci.error.PickleLoadBytes):
        maci.pickleloadbytes(pickled_byte_data=bad_data)
