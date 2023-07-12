# createfilehash
#########################################################################################################
# Imports
from .._native.loadraw import loadraw as _loadraw
from .._native.dumpraw import dumpraw as _dumpraw
from typing import Union as _Union
from typing import Any as _Any
import hashlib as _hashlib
from ..error import CreateFileHash, LoadRaw, DumpRaw

#########################################################################################################
# Create file hash
def createfilehash(file_to_hash: str, file_to_store_hash: _Union[str,None], hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> str:
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
    err_msg_str_file_src = f"Only str is allowed for 'file_to_hash'"
    err_msg_file_dst = f"Only str|None is allowed for 'file_to_store_hash'"
    err_msg_str_hash = f"Only str is allowed for 'hash_algorithm'"
    err_msg_hash = f"Invalid or no hash option chosen for 'hash_algorithm'"
    err_msg_str_encoding = f"Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(file_to_hash, str): raise CreateFileHash(err_msg_str_file_src, f'"{file_to_hash}"')
    if not isinstance(file_to_store_hash, (str, type(None))): raise CreateFileHash(err_msg_file_dst, f'"{file_to_store_hash}"')
    if not isinstance(hash_algorithm, str): raise CreateFileHash(err_msg_str_hash, f'"{hash_algorithm}"')
    if not hash_algorithm in ALGO_OPTIONS: raise CreateFileHash(err_msg_hash, f'"{hash_algorithm}"')
    if not isinstance(encoding, (str, type(None))): raise CreateFileHash(err_msg_str_encoding, f'\nGot: {repr(encoding)}')

    # Generate Hash Type
    _hash_type: _Any  # ignore type checker
    if hash_algorithm == ALGO_OPTIONS[0]: _hash_type = _hashlib.sha256() # sha256
    if hash_algorithm == ALGO_OPTIONS[1]: _hash_type = _hashlib.sha512() # sha512
    if hash_algorithm == ALGO_OPTIONS[2]: _hash_type = _hashlib.sha384() # sha384
    if hash_algorithm == ALGO_OPTIONS[3]: _hash_type = _hashlib.sha1() # sha1  # nosec: B303, B324  # ignore sec checker - up to dev discretion
    if hash_algorithm == ALGO_OPTIONS[4]: _hash_type = _hashlib.md5() # md5  # nosec: B303, B324  # ignore sec checker - up to dev discretion

    # Read source file data and update hash
    _readbytes: _Any  # ignore type checker
    try: _readbytes = _loadraw(file_to_hash)
    except LoadRaw as err_msg: raise CreateFileHash(err_msg)

    try: _readbytes = _readbytes.encode() if encoding is None else _readbytes.encode(encoding=encoding)
    except LookupError: raise CreateFileHash(err_msg_str_encoding, f'\nGot: {repr(encoding)}')
    _hash_type.update(_readbytes)
    
    # Store hash to file
    _hash_type = _hash_type.hexdigest()

    try:
        if isinstance(file_to_store_hash, str):
            _dumpraw(file_to_store_hash, f'hash_data = "{_hash_type}"', encoding=encoding)
    except DumpRaw as err_msg: raise CreateFileHash(err_msg)

    # Return hash data also
    return _hash_type
