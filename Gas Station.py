'''
 There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        tank = total = 0
        n = len(gas);  start = 0
        for i in range(n):
            total += (gas[i] - cost[i])
            tank += (gas[i] - cost[i])
            if tank < 0:
                start = i+1;   tank = 0
        return -1 if total<0 else start

# If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)

# Proof For 1st point, if A can't reach B, and there exists C between A & B which can reach B, then A can reach C first, then reach B from C, which is conflict with our init statement: A can't reach B. so, the assume that such C exists is invalid.