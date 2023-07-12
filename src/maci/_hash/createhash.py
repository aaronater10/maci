# createhash
#########################################################################################################
# Imports
from typing import Union as _Union
from typing import List as _List
from typing import Tuple as _Tuple
from typing import Set as _Set
import hashlib as _hashlib
from ..error import CreateHash

#########################################################################################################
# Create Hash
def createhash(data_to_hash: _Union[str, bytes, int, _List[int], _Tuple[int], _Set[int], range, bool], hash_algorithm: str='sha256', *, encoding: str='utf-8') -> str:
    """
    Creates a hash of the provided data

    Returns a str of the hash in hex. Assign the output to var

    [Options]

    hash_algorithm: Default is 'sha256'. Supported options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'

    [Example Use]

    createhash('data')

    This is using the hashlib library shipped with the python standard library. For more
    information on hashlib, visit: https://docs.python.org/3/library/hashlib.html
    """
    ALGO_OPTIONS = ('sha256', 'sha512', 'sha384', 'sha1', 'md5')

    # Error checks
    err_msg_data = f"Only str|bytes|int|List[int]|Tuple[int]|Set[int]|range|bool is allowed for 'data_to_hash'"
    err_msg_str_hash = f"Only str is allowed for 'hash_algorithm'"
    err_msg_hash = f"Invalid hash option chosen for 'hash_algorithm'. Valid options: 'sha256', 'sha512', 'sha384', 'sha1', 'md5'"
    err_msg_str_encoding = f"Only str or valid option is allowed for 'encoding'"

    # Check Types
    valid_types_to_hash = (str, bytes, int, list, tuple, set, range, bool)
    valid_seq_of_int_types = (list, tuple, set, range)

    if not isinstance(data_to_hash, valid_types_to_hash): raise CreateHash(err_msg_data, f'\nGot: {repr(data_to_hash)}')
    if not isinstance(encoding, str): raise CreateHash(err_msg_str_encoding, f'\nGot: {repr(encoding)}')

    if isinstance(data_to_hash, valid_seq_of_int_types):
        if not all(isinstance(item, int) for item in data_to_hash):
            raise CreateHash(err_msg_data, f'\nGot: {repr(data_to_hash)}')

    if not isinstance(hash_algorithm, str): raise CreateHash(err_msg_str_hash, f'\nGot: {repr(hash_algorithm)}')
    if not hash_algorithm in ALGO_OPTIONS: raise CreateHash(err_msg_hash, f'\nGot: {repr(hash_algorithm)}')

    # Generate Hash Type
    if hash_algorithm == ALGO_OPTIONS[0]: hash_type = _hashlib.sha256() # sha256
    if hash_algorithm == ALGO_OPTIONS[1]: hash_type = _hashlib.sha512() # sha512
    if hash_algorithm == ALGO_OPTIONS[2]: hash_type = _hashlib.sha384() # sha384
    if hash_algorithm == ALGO_OPTIONS[3]: hash_type = _hashlib.sha1() # sha1  # nosec: B303, B324  # ignore sec checker - up to dev discretion
    if hash_algorithm == ALGO_OPTIONS[4]: hash_type = _hashlib.md5() # md5  # nosec: B303, B324  # ignore sec checker - up to dev discretion

    # Check and Convert data to bytes and update hash
    try: 
        if isinstance(data_to_hash, str): byte_data = data_to_hash.encode(encoding=encoding)
    except LookupError: raise CreateHash(err_msg_str_encoding, f'\nGot: {repr(encoding)}')

    if isinstance(data_to_hash, bytes): byte_data = data_to_hash
    if isinstance(data_to_hash, int): byte_data = bytes(data_to_hash) # catches bool as well
    if isinstance(data_to_hash, valid_seq_of_int_types): byte_data = bytes(data_to_hash)

    hash_type.update(byte_data)
    return hash_type.hexdigest()
