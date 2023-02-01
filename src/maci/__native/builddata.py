# builddata
#########################################################################################################
# Imports
from ..data import MaciDataObj

#########################################################################################################
# Build manual MaciDataObj (python data)
def builddata() -> 'MaciDataObj':
    """
    Returns an empty MaciDataObj obj to manually build python data with maci features
    
    Assign the output to var

    Literally just use attribute assignment as you normally would

    [Example]

    object.attribute1 = [1,2,3]

    object.attribute2 = 'string data'

    More information on object features: https://docs.macilib.org/docs/tools/build-data/python-data-build
    """
    # Syntax/Usage Error Messages
    __err_messages = {
        '_py_syntax_err_msg': "Must have valid Python data types to import, or syntax is not formatted correctly",
        '_name_preexists_err_msg': "Name already preexists. Must give unique attribute names",
        '_name_reference_does_not_exist_msg': "Name reference does not exist! Must reference attribute names that have been defined",
        '_assignment_locked_atrribs_err_msg': "Value Locked! Attribute cannot be reassigned",
        '_assignment_hard_locked_atrribs_err_msg': "Value Hard Locked! Attribute cannot be reassigned, deleted, or unlocked"
    }
    return MaciDataObj(
                '',
                attr_name_dedup=True,
                _is_build_request=True,
                **__err_messages,
            )
