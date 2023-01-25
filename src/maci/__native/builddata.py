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
    return MaciDataObj('', attrib_name_dedup=True, _is_build_request=True)
