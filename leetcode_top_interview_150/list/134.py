class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        total_cost = 0
        start = 0
        for i in range(n):
            total_cost += gas[i] - cost[i]
            if total_cost < 0:
                start = i + 1
                total_cost = 0 

        return -1 if total_cost < 0 else start