# exceptions: hash - Tests
from src import maci
from os import remove
import time
import pytest

test_file_path = './tests/test_files/hash/'
file_delay_timer = 0.25


################################################################
# Tests

### createhash ###

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


### createfilehash ###

# 1. Create File Hash - Type Checks
def test1_exceptions_createfilehash_types():
    filepath_to_hash = test_file_path + 'exc_createfilehash.data'
    filepath_to_cache = test_file_path + '1_exc_createfilehash.cache'

    # Remove Any Existing Cache Test File
    try: remove(filepath_to_cache)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(file_to_hash=1.0, file_to_store_hash='')
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash('', file_to_store_hash=1.0)
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(filepath_to_hash, filepath_to_cache, hash_algorithm=1.0)
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(filepath_to_hash, filepath_to_cache, 'sha256', encoding=1.0)

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath_to_cache)
    except: pass


# 2. Create File Hash - Unsupported Options or Data
def test2_exceptions_createfilehash_unsupported_opts_data():
    filepath_to_hash = test_file_path + 'exc_createfilehash.data'
    filepath_to_cache = test_file_path + '2_exc_createfilehash.cache'

    # Remove Any Existing Cache Test File
    try: remove(filepath_to_cache)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(file_to_hash='', file_to_store_hash=filepath_to_cache)
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(file_to_hash=filepath_to_hash, file_to_store_hash='')
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(file_to_hash=filepath_to_hash, file_to_store_hash=False) # old way
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(filepath_to_hash, filepath_to_cache, hash_algorithm='')
    with pytest.raises(maci.error.CreateFileHash):
        maci.createfilehash(filepath_to_hash, filepath_to_cache, 'sha256', encoding='')

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath_to_cache)
    except: pass


### comparefilehash ###

# 1. Compare File Hash - Type Checks
def test1_exceptions_comparefilehash_types():
    filepath_to_hash = test_file_path + 'exc_comparefilehash.data'
    filepath_to_cache = test_file_path + '1_exc_comparefilehash.cache'

    # Remove Any Existing Cache Test File
    try: remove(filepath_to_cache)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash(file_to_hash=1.0, stored_hash_file='')
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash('', stored_hash_file=1.0)
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash(filepath_to_hash, filepath_to_cache, hash_algorithm=1.0)
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash(filepath_to_hash, filepath_to_cache, 'sha256', encoding=1.0)

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath_to_cache)
    except: pass


# 2. Compare File Hash - Unsupported Options or Data
def test2_exceptions_comparefilehash_unsupported_opts_data():
    filepath_to_hash = test_file_path + 'exc_comparefilehash.data'
    filepath_to_cache = test_file_path + '2_exc_comparefilehash.cache'

    # Remove Any Existing Cache Test File
    try: remove(filepath_to_cache)
    except: pass
    time.sleep(file_delay_timer)

    # Tests
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash(file_to_hash='', stored_hash_file=filepath_to_cache)
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash(file_to_hash=filepath_to_hash, stored_hash_file='')
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash(filepath_to_hash, filepath_to_cache, hash_algorithm='')
    with pytest.raises(maci.error.CompareFileHash):
        maci.comparefilehash(filepath_to_hash, filepath_to_cache, 'sha256', encoding='')

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath_to_cache)
    except: pass
