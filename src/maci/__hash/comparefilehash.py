# comparefilehash
#########################################################################################################
# Imports
from .createfilehash import createfilehash
from ..__native.load import load
from ..error import CompareFileHash

#########################################################################################################
# Compare file hashes
def comparefilehash(file_to_hash: str, stored_hash_file: str, hash_algorithm: str='sha256') -> bool:
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
    __ALGO_OPTIONS = ('sha256', 'sha512', 'sha384', 'sha1', 'md5')

    # Error checks
    __err_msg_str_file_src = f"Only str is allowed for file_to_hash"
    __err_msg_hash_file = f"Only str is allowed for stored_hash_file"
    __err_msg_str_hash = f"Only str is allowed for hash_algorithm"
    __err_msg_hash = f"Invalid or no hash option chosen for hash_algorithm"

    if not isinstance(file_to_hash, str): raise CompareFileHash(__err_msg_str_file_src, f'"{file_to_hash}"')
    if not isinstance(stored_hash_file, str): raise CompareFileHash(__err_msg_hash_file, f'"{stored_hash_file}"')
    if not isinstance(hash_algorithm, str): raise CompareFileHash(__err_msg_str_hash, f'"{hash_algorithm}"')
    if not hash_algorithm in __ALGO_OPTIONS: raise CompareFileHash(__err_msg_hash, f'"{hash_algorithm}"')
    
    # Collect hash data, then return result
    __hash_data = createfilehash(file_to_hash, False, hash_algorithm)
    __stored_hash_data = load(stored_hash_file)
    return (__hash_data == __stored_hash_data.hash_data)