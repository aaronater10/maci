# builddata
#########################################################################################################
# Imports
from .load import MaciFileData

#########################################################################################################
# Build manual MaciFileData (python data)
def builddata() -> MaciFileData:
    """
    Returns an empty MaciFileData obj to manually build python data with maci features
    
    Assign the output to var

    Literally just use attribute assignment as you normally would

    [Example]

    object.attribute1 = [1,2,3]

    object.attribute2 = 'string data'

    More information on object features: https://docs.macilib.org/docs/tools/build-data/python-data-build
    """
    return MaciFileData('', True, True)
