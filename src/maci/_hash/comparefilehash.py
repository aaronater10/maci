# comparefilehash
#########################################################################################################
# Imports
from typing import Union as _Union
from typing import Any as _Any
from pathlib import Path as _PathObj
from .createfilehash import createfilehash as _createfilehash
from .._native.load import load as _load
from ..error import CompareFileHash, CreateFileHash, Load

#########################################################################################################
# Compare file hashes
def comparefilehash(file_to_hash: _Union[str, _PathObj], stored_hash_file: _Union[str, _PathObj], hash_algorithm: str='sha256', *, encoding: _Union[str, None]=None) -> bool:
    """
    Compares a hash of any file by comparing the previously created file with hash data stored from using the "createfilehash" partner function

    Returns a bool if the hash does/doesn't match

    [Partner Functions]

    createfilehash: creates the initial hash file data to compare against

    [Options]

    hash_algorithm: Default is 'sha256' - Other options: 'sha512', 'sha384', 'sha1', 'md5'

    [Example: Usage]
    
    comparefilehash('path/to/src_filename', 'path/to/src_hash_filename')

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html

    Maci docs: https://docs.macilib.org
    """
    ALGO_OPTIONS = ('sha256', 'sha512', 'sha384', 'sha1', 'md5')

    # Error checks
    err_msg_str_file_src = f"Only str is allowed for 'file_to_hash'"
    err_msg_hash_file = f"Only str is allowed for 'stored_hash_file'"
    err_msg_str_hash = f"Only str is allowed for 'hash_algorithm'"
    err_msg_hash = f"Invalid or no hash option chosen for 'hash_algorithm'"
    err_msg_str_encoding = f"Only str|None or valid option is allowed for 'encoding'"

    if not isinstance(file_to_hash, (str, _PathObj)): raise CompareFileHash(err_msg_str_file_src, f'"{file_to_hash}"')
    if not isinstance(stored_hash_file, (str, _PathObj)): raise CompareFileHash(err_msg_hash_file, f'"{stored_hash_file}"')
    if not isinstance(hash_algorithm, str): raise CompareFileHash(err_msg_str_hash, f'"{hash_algorithm}"')
    if not hash_algorithm in ALGO_OPTIONS: raise CompareFileHash(err_msg_hash, f'"{hash_algorithm}"')
    if not isinstance(encoding, (str, type(None))): raise CompareFileHash(err_msg_str_encoding, f'\nGot: {repr(encoding)}')

    # Convert filenames to str to catch Path objects
    file_to_hash = str(file_to_hash)
    stored_hash_file = str(stored_hash_file)

    # Collect hash data, then return result
    try: _hash_data = _createfilehash(file_to_hash, None, hash_algorithm, encoding=encoding)
    except CreateFileHash as err_msg: raise CompareFileHash(err_msg)

    try:
        _stored_hash_data: _Any  # ignore type checker
        _stored_hash_data = _load(stored_hash_file, encoding=encoding)
    except Load as err_msg: raise CompareFileHash(err_msg)

    return (_hash_data == _stored_hash_data.hash_data)
