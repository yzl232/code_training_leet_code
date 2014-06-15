class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        l = len(ratings)
        candy = [1 for i in range(l)]
        for i in range(l-2):
            if ratings[i+1] > ratings[i] and candy[i+1] <= candy[i]:
                candy[i+1] = candy[i]+1
        for i in range(l-1, 0, -1):
            if ratings[i-1] > ratings[i] and candy[i-1] <= candy[i]:
                candy[i-1] = candy[i]+1
        return sum(candy)