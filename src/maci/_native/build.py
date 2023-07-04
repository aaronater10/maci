# build
#########################################################################################################
# Imports
from typing import Any as _Any
from ..data import MaciDataObj as _MaciDataObj

#########################################################################################################
# Build manual MaciDataObj (python data)
def build() -> '_MaciDataObj':
    """
    Returns an empty MaciDataObj obj to manually build pythonic data with maci features
    
    Assign the output to var

    Literally, just use attribute assignment as you normally would

    [Example]

    object.attribute1 = [1,2,3]

    object.attribute2 = 'string data'

    More information on object features: https://docs.macilib.org/docs/tools/build-data/python-data-build
    """
    # Syntax/Usage Error Messages
    err_messages: _Any = {  # ignore type checker
        '_py_syntax_err_msg': "Must have valid Python data types to import, or maci syntax is incorrect",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names",
        '_name_reference_does_not_exist_msg': "Map name does not exist! Must map attribute names that have been defined",
        '_assignment_locked_atrribs_err_msg': "Attribute Name Locked! Cannot be reassigned",
        '_assignment_hard_locked_atrribs_err_msg': "Attribute Name Hard Locked! Cannot be reassigned, deleted, or unlocked"
    }
    return _MaciDataObj(
                '',
                attr_name_dedup=True,
                _is_build_request=True,
                encoding=None,
                **err_messages,
            )
