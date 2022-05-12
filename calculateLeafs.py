import math
def calculateBlocksInLeaf(observations, recordsInBlock, fillDegree):
    perfectStorage=observations/recordsInBlock
    actualInRoot=perfectStorage/fillDegree
    print(f"Theres {actualInRoot} blocks in root level")
    print("")
    print("------------------")
    return actualInRoot

def calculateBlockAtFirstLevel(entityByte, blockByte, blockSize, fillDegree,calculateBlocksInLeaf):
    postRequires=entityByte+blockByte
    blockSpaceAsPosts=(blockSize/postRequires)
    actualBlockSpaceAsPosts=blockSpaceAsPosts*fillDegree
    actualBlockSpaceAsPosts=math.floor(actualBlockSpaceAsPosts)
    print(f"The block fits {actualBlockSpaceAsPosts} posts")
    blocksInLevelOne=math.ceil(calculateBlocksInLeaf/actualBlockSpaceAsPosts)
    print(f"It's therefor {blocksInLevelOne} blocks in level 1")
    print("")
    print("------------------")



fillDegree=2/3
observations=10000
entityByte=4
blockByte=4
blockSpace=2048
recordsInBlock=8
recordsByte=250

f=calculateBlocksInLeaf(observations, recordsInBlock, fillDegree)
f1=calculateBlockAtFirstLevel(entityByte,blockByte,blockSpace,fillDegree,f)

