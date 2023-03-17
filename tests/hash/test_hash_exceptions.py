# exceptions: hash - Tests
from src import maci
import pytest

################################################################
# Tests

# 1. Create Hash - Type Checks
def test1_exceptions_createhash_types():    
    with pytest.raises(maci.error.CreateHash):
        maci.createhash(data_to_hash=1.0)
    with pytest.raises(maci.error.CreateHash):
        maci.createhash('', hash_algorithm=1.0)
    with pytest.raises(maci.error.CreateHash):
        maci.createhash('', 'sha256', encoding=1.0)

# 2. Create Hash - Unsupported Options or Data
def test2_exceptions_createhash_unsupported_opts_data():    
    with pytest.raises(maci.error.CreateHash):
        maci.createhash('', hash_algorithm='')
    with pytest.raises(maci.error.CreateHash):
        maci.createhash('', 'sha256', encoding='')
