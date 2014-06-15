class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        total = 0
        sum = 0 
        n = len(gas)
        start = 0
        for i in range(n):
            sum += (gas[i] - cost[i])
            total += (gas[i] - cost[i])
            if total < 0:
                start = i+1
                total = 0
        if sum < 0:
            return -1
        return start