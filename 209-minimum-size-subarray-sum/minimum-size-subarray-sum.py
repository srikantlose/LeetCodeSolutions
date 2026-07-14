class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L,R,curSum,diff,minDiff=0,0,0,0,float('inf')
        while (R<len(nums)):
            curSum+=nums[R]
            while(curSum>=target):
                diff=R-L+1
                minDiff=min(diff,minDiff)
                curSum-=nums[L]
                L+=1
            R+=1
        return minDiff if minDiff != float('inf') else 0