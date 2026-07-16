class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        diff = [g - c for g, c in zip(gas, cost)]
        totalgas = 0
        start=0
        for i in range (len(diff)):
            totalgas+=diff[i]
            if totalgas<0:
                totalgas=0
                start=i+1
                
        return start
