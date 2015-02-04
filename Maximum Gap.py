# encoding=utf-8
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, arr):
        if len(arr) < 2: return 0   # 例子 1  4  6.   buckets 1~ 3    4~6
        a = min(arr);  b = max(arr);  t = max(1, int((b - a - 1) / (len(arr) - 1)) + 1) #ceil( (B - A) / (N - 1) )
        n = ((b - a) / t + 1);    bkt = [None] * n  #这个t和n的得出很难。
        for x in arr:
            i = (x - a) / t
            if not bkt[i]: bkt[i] =  (x, x)
            else:  bkt[i] = (min(bkt[i][0], x), max(bkt[i][1], x))
        ret = 0; pre=0; i=1
        while i<n:
            while i<n and not bkt[i]: i+=1
            ret = max(bkt[i][0]-bkt[pre][1], ret)
            pre = i;  i+=1
        print bkt, t
        return ret


s = Solution()
print s.maximumGap([3, 6, 9, 1])