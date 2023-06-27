# comparefilehash - Tests
from src import maci
from os import remove
import time

test_file_path = './tests/test_files/hash/'
file_delay_timer = 0.25


################################################################
# TESTS

# Hashes used to verfiy in tests
SHA256 = "5dd4b652c5279c6e38c29aeb348c08e84004df82d1cbadf2ccc8cde3a56ed981"
SHA256_U16 = "3d929c0dcbdbb9a3166be4e4d21d3069680a83c910bf69b4b814c9dc6608c031"
SHA256_U32 = "0b810fbdd326b62836e3686fa308c67d1d88886bf5e718862691c880846919e5"

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


# 2. Encoding - Test some common encoding types
def test2_comparefilehash_encodings():
    file_to_hash = '2_compare_hash_encoding.data'
    file_to_cache = '2_compare_hash_encoding.cache'
    filepath_to_hash = test_file_path + file_to_hash
    filepath_to_cache = test_file_path + file_to_cache

    # Remove Any Existing Cache Test File
    try: remove(filepath_to_cache)
    except: pass
    time.sleep(file_delay_timer)

    # Test - Using default hash algorithm SHA256
    maci.createfilehash(filepath_to_hash, filepath_to_cache, encoding='utf-8')
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache, encoding='utf-8')

    maci.createfilehash(filepath_to_hash, filepath_to_cache, encoding='utf-16')
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache, encoding='utf-16')

    maci.createfilehash(filepath_to_hash, filepath_to_cache, encoding='utf-32')
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache, encoding='utf-32')

    maci.createfilehash(filepath_to_hash, filepath_to_cache, encoding='ascii')
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache, encoding='ascii')

    maci.createfilehash(filepath_to_hash, filepath_to_cache, encoding='iso-8859-1')
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache, encoding='iso-8859-1')

    maci.createfilehash(filepath_to_hash, filepath_to_cache, encoding='cp1252')
    assert maci.comparefilehash(filepath_to_hash, filepath_to_cache, encoding='cp1252')

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath_to_cache)
    except: pass
