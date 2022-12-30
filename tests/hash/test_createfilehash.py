# createfilehash - Tests
from src import maci
from os import remove
import time

test_file_path = './tests/test_files/hash/'
file_delay_timer = 0.5


################################################################
# TESTS

# Hashes used to verfiy in tests
SHA256 = "5dd4b652c5279c6e38c29aeb348c08e84004df82d1cbadf2ccc8cde3a56ed981"
SHA512 = "5d087321d80436bb8710b524d42d266bfd52a6264d12733202b6e4d410faeef4c05e5c79f6f05ee05f1be6fffdda11fc906cfec37dadfbca4e093870e188bf7d"
SHA384 = "440549e7a25995a2346bfe905c21941ae1302928833430ef06582613550dba364cb72db4470dd818b608998bd91c7737"
SHA1 = "090496ae5a8bf96828fc9e1a3739a1246e617093"
MD5 = "af1c462ac9a2cf3b47d3d33a780dd377"

# 1. Create Hash File - Read a file and generate hash from it, then export hash and also return the hash
def test1_create_hash_file():
    file_to_hash = '1_file_hash.data'
    file_to_cache = '1_file_hash.cache'
    filepath_to_hash = test_file_path + file_to_hash
    filepath_to_cache = test_file_path + file_to_cache

    # Remove Any Existing Cache Test File
    try: remove(filepath_to_cache)
    except: pass
    time.sleep(file_delay_timer)

    # Test sha256 - generate hash of file and import to test value and type
    sha256_returned = maci.createfilehash(filepath_to_hash, filepath_to_cache)
    file_import = maci.load(filepath_to_cache)
    assert (file_import.hash_data == SHA256) and (isinstance(file_import.hash_data, str))
    assert (sha256_returned == SHA256) and (isinstance(sha256_returned, str))

    # Test sha512 - generate hash of file and import to test value and type
    sha512_returned = maci.createfilehash(filepath_to_hash, filepath_to_cache, 'sha512')
    file_import = maci.load(filepath_to_cache)
    assert (file_import.hash_data == SHA512) and (isinstance(file_import.hash_data, str))
    assert (sha512_returned == SHA512) and (isinstance(sha512_returned, str))

    # Test sha384 - generate hash of file and import to test value and type
    sha384_returned = maci.createfilehash(filepath_to_hash, filepath_to_cache, 'sha384')
    file_import = maci.load(filepath_to_cache)
    assert (file_import.hash_data == SHA384) and (isinstance(file_import.hash_data, str))
    assert (sha384_returned == SHA384) and (isinstance(sha384_returned, str))

    # Test sha1 - generate hash of file and import to test value and type
    sha1_returned = maci.createfilehash(filepath_to_hash, filepath_to_cache, 'sha1')
    file_import = maci.load(filepath_to_cache)
    assert (file_import.hash_data == SHA1) and (isinstance(file_import.hash_data, str))
    assert (sha1_returned == SHA1) and (isinstance(sha1_returned, str))

    # Test md5 - generate hash of file and import to test value and type
    md5_returned = maci.createfilehash(filepath_to_hash, filepath_to_cache, 'md5')
    file_import = maci.load(filepath_to_cache)
    assert (file_import.hash_data == MD5) and (isinstance(file_import.hash_data, str))
    assert (md5_returned == MD5) and (isinstance(md5_returned, str))

    # Remove Cache Test File
    time.sleep(file_delay_timer)
    try: remove(filepath_to_cache)
    except: pass


# 2. Create Hash Only - Read a file and generate hash from it, then return the hash only
def test2_create_hash_only():
    file_to_hash = '2_file_hash_only.data'
    filepath_to_hash = test_file_path + file_to_hash

    # Test sha256 - generate hash of file and import to test value and type
    sha256_returned = maci.createfilehash(filepath_to_hash, False)
    assert (sha256_returned == SHA256) and (isinstance(sha256_returned, str))

    # Test sha512 - generate hash of file and import to test value and type
    sha512_returned = maci.createfilehash(filepath_to_hash, False, 'sha512')
    assert (sha512_returned == SHA512) and (isinstance(sha512_returned, str))

    # Test sha384 - generate hash of file and import to test value and type
    sha384_returned = maci.createfilehash(filepath_to_hash, False, 'sha384')
    assert (sha384_returned == SHA384) and (isinstance(sha384_returned, str))

    # Test sha1 - generate hash of file and import to test value and type
    sha1_returned = maci.createfilehash(filepath_to_hash, False, 'sha1')
    assert (sha1_returned == SHA1) and (isinstance(sha1_returned, str))

    # Test md5 - generate hash of file and import to test value and type
    md5_returned = maci.createfilehash(filepath_to_hash, False, 'md5')
    assert (md5_returned == MD5) and (isinstance(md5_returned, str))