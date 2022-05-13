import math
def calculateAverageBlockAccess(blocks, lenOfList, blockSpace):
    remaining=lenOfList%(blocks*blockSpace)
    totalAccess=lenOfList+remaining
    avg=round(totalAccess/lenOfList, 2)
    print(avg)

lengthOfList=9
blocks=4
spaceInBlocks=2
calculateAverageBlockAccess(blocks, lengthOfList, spaceInBlocks)
