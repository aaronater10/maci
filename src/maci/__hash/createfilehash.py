# createfilehash
#########################################################################################################
# Imports
from ..__native.loadraw import loadraw as _loadraw
from ..__native.dumpraw import dumpraw as _dumpraw
from typing import Union as _Union
import hashlib as _hashlib
from ..error import CreateFileHash

#########################################################################################################
# Create file hash
def createfilehash(file_to_hash: str, file_to_store_hash: _Union[str,bool], hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> str:
    """
    Creates a hash of any file, and stores the hash data to a new created file

    Always returns a str of the hash as well. Assign the output to var

    Enter file locations as str

    [Options]
    file_to_store_hash: Set to False if you do not want hash data stored to a file. Hash data is always returned whether or not this is set

    hash_algorithm: Already set to default of 'sha256'. Supported options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'

    [Example Use]

    Default: createfilehash('path/to/src_filename', 'path/to/dst_hash_filename')
    Hash only, no file: hash_data = createfilehash('path/to/filename', False)

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html
    """
    ALGO_OPTIONS = ('sha256', 'sha512', 'sha384', 'sha1', 'md5')

    # Error checks
    _err_msg_str_file_src = f"Only str is allowed for file_to_hash"
    _err_msg_file_dst = f"Only str|bool is allowed for file_to_store_hash"
    _err_msg_str_hash = f"Only str is allowed for hash_algorithm"
    _err_msg_hash = f"Invalid or no hash option chosen for hash_algorithm"

    if not isinstance(file_to_hash, str): raise CreateFileHash(_err_msg_str_file_src, f'"{file_to_hash}"')
    if not ((isinstance(file_to_store_hash, str)) \
        or (isinstance(file_to_store_hash, bool))): raise CreateFileHash(_err_msg_file_dst, f'"{file_to_store_hash}"')
    if not isinstance(hash_algorithm, str): raise CreateFileHash(_err_msg_str_hash, f'"{hash_algorithm}"')
    if not hash_algorithm in ALGO_OPTIONS: raise CreateFileHash(_err_msg_hash, f'"{hash_algorithm}"')

    # Generate Hash Type
    if hash_algorithm == ALGO_OPTIONS[0]: _hash_type = _hashlib.sha256() # sha256
    if hash_algorithm == ALGO_OPTIONS[1]: _hash_type = _hashlib.sha512() # sha512
    if hash_algorithm == ALGO_OPTIONS[2]: _hash_type = _hashlib.sha384() # sha384
    if hash_algorithm == ALGO_OPTIONS[3]: _hash_type = _hashlib.sha1() # sha1
    if hash_algorithm == ALGO_OPTIONS[4]: _hash_type = _hashlib.md5() # md5
    
    # Read source file data and update hash
    _readbytes = _loadraw(file_to_hash, byte_data=True)
    _hash_type.update(_readbytes)
    # Store hash to file
    _hash_type = _hash_type.hexdigest()
    if bool(file_to_store_hash):
        _dumpraw(file_to_store_hash, f'hash_data = "{_hash_type}"', encoding=encoding)
    # Return hash data also
    return _hash_type
