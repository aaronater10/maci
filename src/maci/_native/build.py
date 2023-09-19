# build
#########################################################################################################
# Imports
from typing import Any as _Any
from ..data import MaciDataObj as _MaciDataObj

#########################################################################################################
# Build manual MaciDataObj (python data)
def build() -> '_MaciDataObj':
    """
    Returns an empty 'MaciDataObj' object to manually build data with maci features

    Use attribute assignment as you normally would to build out data

    [Example: Usage]

    var = maci.build()

    [Example: Assign Data]

    var.my_list = [1,2,3]

    Maci docs: https://docs.macilib.org
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
