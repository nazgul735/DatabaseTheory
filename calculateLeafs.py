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

def nestedLoopJoin(postAmount1, blocks1, postAmount2, blocks2, bufferBlocks):
    return blocks1+((blocks1/(bufferBlocks-2))*blocks2)




postAmount1=47000
blocks1=800
postAmount2=500000
blocks2=12800
bufferBlocks=34

print(f" there's {nestedLoopJoin(postAmount1, blocks1, postAmount2, blocks2, bufferBlocks)} accesses for the nesten loop")
print("")
print("-------------")



fillDegree=2/3
observations=10000
entityByte=4
blockByte=4
blockSpace=2048
recordsInBlock=8
recordsByte=250

f=calculateBlocksInLeaf(observations, recordsInBlock, fillDegree)
f1=calculateBlockAtFirstLevel(entityByte,blockByte,blockSpace,fillDegree,f)

