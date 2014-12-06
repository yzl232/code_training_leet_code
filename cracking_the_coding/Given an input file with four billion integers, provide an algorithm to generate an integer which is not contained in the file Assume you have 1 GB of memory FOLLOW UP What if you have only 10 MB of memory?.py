'''
Given an input file with four billion integers, provide an algorithm to generate an integer which is not contained in the file Assume you have 1 GB of memory FOLLOW UP What if you have only 10 MB of memory?
这道题目不用写代码的

'''


'''
It’s possible to find a missing integer with just two passes of the data set. We can divide up the integers into blocks of some size (we’ll discuss how to decide on a size later). Let’s just as- sume that we divide up the integers into blocks of 1000. So, block 0 represents the numbers 0 through 999, block 1 represents blocks 1000 - 1999, etc. Since the range of ints is finite, we know that the number of blocks needed is finite.
In the first pass, we count how many ints are in each block. That is, if we see 552, we know that that is in block 0, we increment counter[0]. If we see 1425, we know that that is in block 1, so we increment counter[1].
At the end of the first pass, we’ll be able to quickly spot a block that is missing a number. If our block size is 1000, then any block which has fewer than 1000 numbers must be missing a number. Pick any one of those blocks.
In the second pass, we’ll actually look for which number is missing. We can do this by creat- ing a simple bit vector of size 1000. We iterate through the file, and for each number that should be in our block, we set the appropriate bit in the bit vector. By the end, we’ll know which number (or numbers) is missing.
Now we just have to decide what the block size is.
A quick answer is 2^20 values per block. We will need an array with 2^12 block counters and a bit vector in 2^17 bytes. Both of these can comfortably fit in 10*2^20 bytes.
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
    
        