# Internal Exceptions - Tests
from src import maci
import pytest

################################################################
# Tests

# 1. Internal Constructor Lock
def test1_internal_constructor_lock():
    # Throws exception if attempting to use constructor directly without specifying request type
    
    # Tests
    with pytest.raises(maci.error.Hint):
        maci.data.MaciDataObj(filename="", attr_name_dedup=True, encoding=None)
