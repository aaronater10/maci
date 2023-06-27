# createhash - Tests
from src import maci

################################################################
# TESTS

# Hashes used to verfiy in tests
SHA256 = "5dd4b652c5279c6e38c29aeb348c08e84004df82d1cbadf2ccc8cde3a56ed981"
SHA256_U16 = "3d929c0dcbdbb9a3166be4e4d21d3069680a83c910bf69b4b814c9dc6608c031"
SHA256_U32 = "0b810fbdd326b62836e3686fa308c67d1d88886bf5e718862691c880846919e5"
SHA512 = "5d087321d80436bb8710b524d42d266bfd52a6264d12733202b6e4d410faeef4c05e5c79f6f05ee05f1be6fffdda11fc906cfec37dadfbca4e093870e188bf7d"
SHA384 = "440549e7a25995a2346bfe905c21941ae1302928833430ef06582613550dba364cb72db4470dd818b608998bd91c7737"
SHA1 = "090496ae5a8bf96828fc9e1a3739a1246e617093"
MD5 = "af1c462ac9a2cf3b47d3d33a780dd377"

# 1. Create Hash - Read data and generate hash from it, then return the hash only
def test1_create_hash():
    # Test sha256 - generate hash of data and test value and type
    sha256_returned = maci.createhash('dummydatatohash')
    assert (sha256_returned == SHA256) and (isinstance(sha256_returned, str))

    # Test sha512 - generate hash of data and test value and type
    sha512_returned = maci.createhash('dummydatatohash', 'sha512')
    assert (sha512_returned == SHA512) and (isinstance(sha512_returned, str))

    # Test sha384 - generate hash of data and test value and type
    sha384_returned = maci.createhash('dummydatatohash', 'sha384')
    assert (sha384_returned == SHA384) and (isinstance(sha384_returned, str))

    # Test sha1 - generate hash of data and test value and type
    sha1_returned = maci.createhash('dummydatatohash', 'sha1')
    assert (sha1_returned == SHA1) and (isinstance(sha1_returned, str))

    # Test md5 - generate hash of data and test value and type
    md5_returned = maci.createhash('dummydatatohash', 'md5')
    assert (md5_returned == MD5) and (isinstance(md5_returned, str))


# 2. Encoding - Test some common encoding types
def test2_createhash_encodings():
    # Using default hash algorithm SHA256
    assert SHA256 == maci.createhash('dummydatatohash', encoding='utf-8')
    assert SHA256_U16 == maci.createhash('dummydatatohash', encoding='utf-16')
    assert SHA256_U32 == maci.createhash('dummydatatohash', encoding='utf-32')
    assert SHA256 == maci.createhash('dummydatatohash', encoding='ascii')
    assert SHA256 == maci.createhash('dummydatatohash', encoding='iso-8859-1')
    assert SHA256 == maci.createhash('dummydatatohash', encoding='cp1252')


# 3. Hash Data Types - Test supported data types to get hashed
def test3_createhash_supported_types():
    # Using default hash algorithm SHA256
    data_str = 'dummydatatohash'
    data_bytes = b'data'
    data_int = 1
    data_list = [1,2,3]
    data_tuple = (1,2,3)
    data_set = {1,2,3}
    data_float = range(3)
    data_bool = True

    test_data = (
        data_str,
        data_bytes,
        data_int,
        data_list,
        data_tuple,
        data_set,
        data_float,
        data_bool
    )
    # Test Loading Supported Data Types
    for data_type in test_data:
        maci.createhash(data_type)
