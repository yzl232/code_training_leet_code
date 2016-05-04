'''
 Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2. 
'''

class Solution(object):
    def integerBreak(self, n):
        if n == 2:  return 1
        if n == 3: return 2
        t = n % 3
        if t == 0:    return int(math.pow(3,n/3))
        if t == 1:    return int(math.pow(3,(n-4)/3) * 4)
        if t == 2:  return int(math.pow(3,(n-2)/3) * 2)
'''

+15 votes
1,358 views

Given a number n lets say we have a possible product P = p1 * p2 * ... pk. Then we notice what would happen if we could break pi up into two more terms lets say one of the terms is 2 we would get the terms pi-2 and 2 so if 2(pi-2) > pi we would get a bigger product and this happens if pi > 4. since there is one other possible number less then 4 that is not 2 aka 3. Likewise for 3 if we instead breakup the one of the terms into pi-3 and 3 we would get a bigger product if 3*(pi-3) > pi which happens if pi > 4.5.

Hence we see that all of the terms in the product must be 2's and 3's. So we now just need to write n = a3 + b2 such that P = (3^a) * (2^b) is maximized. Hence we should favor more 3's then 2's in the product then 2's if possible.

So if n = a*3 then the answer will just be 3^a.

if n = a3 + 2 then the answer will be 2(3^a).

and if n = a3 + 22 then the answer will be 2 * 2 * 3^a

The above three cover all cases that n can be written as and the Math.pow() function takes O(log n) time to preform hence that is the running time.


贪心算法：时间复杂度O(log(n))

关键思路：任何一个比3大的数经过分解都能够得到更大的乘积，所以在一个数的最大乘积分解的结果中将不会有比3大的数，因为只要出现一个这样的数，我们都可以把它分解掉。

算法导论告诉我们一个贪心算法背后都是有一个更加复杂的动态规划的。也就是动态规划能做出来，那么我们就可以想一想用贪心可不可以呢。（在讨论帖游荡了一圈的我，发现原来是可以的。。哈哈）

令 h(n) = h(a1 + a2 + ... + ak) = a1a2...*ak，表示数 n 分解后的最大乘积，首先看一些基本情况：h(2) = h(1 + 1) = 1， h(3) = h(1 + 2) = 2， h(4) = h(2 + 2) = 4，h(5) = h(2 + 3) = 6， h(6) = h(3 + 3) = 9，h(7) = h(3 + 2 + 2) = 12，h(8) = h(3 + 3 + 2) = 18，h(9) = h(3 + 3 + 3) = 27，等等都是最大乘积的分解，有没有发现一个规律，除了 2 = 1 + 1，3 = 1 + 2 之外，所有的这些分解后乘积都变大了。实际上，当一个数小于等于 3 时，分解一个数一定会有一个 1 ，这样肯定会使得这个数被分解后乘积反而小于自身了（1 * 2 < 3），这也告诉我们，在分解的过程中不要分解出 1，因为 1 加上任何一个数比 1 乘以这个数要大。另外，当一个数大于等于 4 之后，分解这个数都能得到一个更大的乘积。现在我们来用这个原则来分解 9，将 9 分解一定能得到一个更大的乘积，随意分解为 9 = 5 + 4，我们发现 4，5 >= 4 , 因此将 5 分解为 5 = 2 + 3，将 4 分解为 4 = 2 + 2，那么 9 = 2 + 2 + 2 + 3。这样我们就不可以再分了。但是其实 h(2 + 2 + 2) = 8 比 h(3 + 3) = 9 要小，因此在最后结果中我们把所有 2 + 2 + 2 都替换成 3 + 3。这样就能得到最大的分解了。这也告诉我们对于任何一个数我们尽量的先把这个数分解为 3，最后分解不出 3 后在分解出 2。。因此代码如下：

(有的同学可能好奇，如果一开始把 9 分解为 2 + 7，会不会得到更好的解呢，实际上不管分解为什么，最后都会只剩下 2 和 3 的组合，因此我们只需要不断地分解出 2 和 3 就好了)

（另外有的同学可能会好奇这样做复杂度应该为O(n)，实际上在代码中我们不是一次乘以一个 3，而是一次性计算有多少个 3 要相乘，在计算 3 的 n 次方时，其实是可以达到O(lgn)的复杂度的，具体可以了解下求幂时的优化）
        
        
        证明是2或者3
        You're making it pretty complicated. Simplifying 2*(f-2) >= f to f >= 4 shows that breaking any factor f >= 4 into factors 2 and f-2 won't hurt the product. There, done :-P

        Edit: Rephrased, maybe that's better:
        If an optimal product contains a factor f >= 4, then you can replace it with factors 2 and f-2 without losing optimality, as 2*(f-2) = 2f-4 >= f. So you never need a factor greater than or equal to 4, meaning you only need factors 1, 2 and 3 (and 1 is of course wasteful and you'd only use it for n=2 and n=3, where it's needed).
        
'''