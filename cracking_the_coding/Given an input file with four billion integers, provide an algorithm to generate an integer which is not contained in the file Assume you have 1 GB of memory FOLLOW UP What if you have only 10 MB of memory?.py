'''
Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order

这道题目不用写代码的

'''

def generateNewNum(filePath):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    d = {}
    for l in lines:
        nums= l.split()
        for n in nums:
            d[int(n)] = 1
    lines = ''
    for i in range(4*2**30+1):
        if i not in d:
            return i
    
    


#Follow up. Only 10 MB   10*(2**20)
def generateNewNum2(filePath):
    f = open(filePath, 'r')
    N = 4*2**30
    blockSize = 2**20
    blockNum = 2**12
    blocks = [0]* blockNum
    while True:
        line = f.readline()
        if not line: break
        nums= line.split()
        for n in nums:
            num = int(n)
            blocks[num/blockSize]+=1
    f.close()
    lines = None
    targetBlockID = 0
    for i in range(blockNum):
        if blocks[i] < blockSize:
            targetBlockID = i
    blocks = None
    d = {}
    f = open(filePath, 'r')
    while True:
        line = f.readline()
        if not line: break
        nums= line.split()
        for n in nums:
            num = int(n)
            if num >= targetBlockID*blockSize and num < (targetBlockID+1)*blockSize:
                d[num] = 1
    f.close()
    for i in range(targetBlockID*blockSize, (targetBlockID+1)*blockSize):
        if i not in d:
            return i
    
        