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
        
        
        '''
         There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

        Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

        Note:
        The solution is guaranteed to be unique.
        
        '''