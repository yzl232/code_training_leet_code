# encoding=utf-8
'''
 The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function will only be called once for each test case.
'''


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:  #输出是count， 另外要求存n个ch存到buf里面。 count和n不一定相等
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):   #给了个read4,  从stream里面读4个， 存到自变量buf里面
        buf1 = [None]*4;     i = 0
        while n > i:#tmp的作用就是判断是不是4096。
            n1, i1 = read4(buf1), 0
            if n1==0: break
            while i<n and i1<n1:
                buf[i]=buf1[i1]
                i1+=1; i+=1
        return i
#换了下变量名, 全部对应了.  i,j ,  nm,  


    
'''


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        tmpBuffer = [None for i in range(4)]
        count = 0; tmpN = 4; flag = True
        while n > count and flag:#tmp的作用就是判断是不是4096。
            tmpN = read4(tmpBuffer)
            if tmpN<4:  flag=False
            byteN = min(tmpN, n-count)
            buf[count:count+byteN]= tmpBuffer[:byteN]  #结束2个指标 : 1 tmp!=4096.   或者n<=count 完成目标是读n个。或者read4k读完了。
            count+=byteN
        return count
'''