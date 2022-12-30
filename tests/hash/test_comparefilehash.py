# comparefilehash - Tests
from src import maci

test_file_path = './tests/test_files/hash/'


################################################################
# TESTS

# 1. Compare File Hash - Read a file and generate hash from it, then compare hash from stored hash
def test1_compare_file_hash():
    file_to_hash = '1_file_hash.data'
    cached_file_256 = '1_compare_hash_256.cache'
    cached_file_512 = '1_compare_hash_512.cache'
    cached_file_384 = '1_compare_hash_384.cache'
    cached_file_sha1 = '1_compare_hash_sha1.cache'
    cached_file_md5 = '1_compare_hash_md5.cache'
    filepath_to_hash = test_file_path + file_to_hash
    filepath_to_cache_256 = test_file_path + cached_file_256
    filepath_to_cache_512 = test_file_path + cached_file_512
    filepath_to_cache_384 = test_file_path + cached_file_384
    filepath_to_cache_sha1 = test_file_path + cached_file_sha1
    filepath_to_cache_md5 = test_file_path + cached_file_md5

    # Test sha256 - generate hash of file and import to test value and type
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache_256) == True    
    assert isinstance(maci.comparefilehash(filepath_to_hash, filepath_to_cache_256), bool)

    # Test sha512 - generate hash of file and import to test value and type
    algo_option = 'sha512'
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache_512, algo_option) == True    
    assert isinstance(maci.comparefilehash(filepath_to_hash, filepath_to_cache_512, algo_option), bool)

    # Test sha384 - generate hash of file and import to test value and type
    algo_option = 'sha384'
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache_384, algo_option) == True    
    assert isinstance(maci.comparefilehash(filepath_to_hash, filepath_to_cache_384, algo_option), bool)

    # Test sha1 - generate hash of file and import to test value and type
    algo_option = 'sha1'
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache_sha1, algo_option) == True    
    assert isinstance(maci.comparefilehash(filepath_to_hash, filepath_to_cache_sha1, algo_option), bool)

    # Test md5 - generate hash of file and import to test value and type
    algo_option = 'md5'
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache_md5, algo_option) == True    
    assert isinstance(maci.comparefilehash(filepath_to_hash, filepath_to_cache_md5, algo_option), bool)