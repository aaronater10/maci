# comparefilehash
#########################################################################################################
# Imports
from typing import Union as _Union
from typing import Any as _Any
from .createfilehash import createfilehash as _createfilehash
from .._native.load import load as _load
from ..error import CompareFileHash, CreateFileHash, Load

#########################################################################################################
# Compare file hashes
def comparefilehash(file_to_hash: str, stored_hash_file: str, hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> bool:
    """
    Compares hash of any file by importing the previously stored hash file data from using "createfilehash"

    Returns a bool if the hash does/doesn't match

    Enter file locations as str

    [Options]

    hash_algorithm: Already set to default of 'sha256'. Supported options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'

    [Example Use]
    
    comparefilehash('path/to/src_filename', 'path/to/src_hash_filename')

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html
    """
    ALGO_OPTIONS = ('sha256', 'sha512', 'sha384', 'sha1', 'md5')

    # Error checks
    err_msg_str_file_src = f"Only str is allowed for 'file_to_hash'"
    err_msg_hash_file = f"Only str is allowed for 'stored_hash_file'"
    err_msg_str_hash = f"Only str is allowed for 'hash_algorithm'"
    err_msg_hash = f"Invalid or no hash option chosen for 'hash_algorithm'"
    err_msg_str_encoding = f"Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(file_to_hash, str): raise CompareFileHash(err_msg_str_file_src, f'"{file_to_hash}"')
    if not isinstance(stored_hash_file, str): raise CompareFileHash(err_msg_hash_file, f'"{stored_hash_file}"')
    if not isinstance(hash_algorithm, str): raise CompareFileHash(err_msg_str_hash, f'"{hash_algorithm}"')
    if not hash_algorithm in ALGO_OPTIONS: raise CompareFileHash(err_msg_hash, f'"{hash_algorithm}"')
    if not isinstance(encoding, (str, type(None))): raise CompareFileHash(err_msg_str_encoding, f'\nGot: {repr(encoding)}')

    # Collect hash data, then return result
    try: _hash_data = _createfilehash(file_to_hash, None, hash_algorithm, encoding=encoding)
    except CreateFileHash as err_msg: raise CompareFileHash(err_msg)

    try:
        _stored_hash_data: _Any  # ignore type checker
        _stored_hash_data = _load(stored_hash_file, encoding=encoding)
    except Load as err_msg: raise CompareFileHash(err_msg)

    return (_hash_data == _stored_hash_data.hash_data)
