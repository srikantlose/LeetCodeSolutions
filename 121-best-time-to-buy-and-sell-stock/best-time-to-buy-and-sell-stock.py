class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        newPrices=[-x for x in prices]
        L,R,=0,1
        curDiff,maxDiff=0,float('-inf')
        while(R<len(prices)):
            curDiff=prices[R]-prices[L]
            maxDiff=max(maxDiff,curDiff)
            if curDiff<=0:
                L=R
            # elif curDiff==0:
            #     L=R
            R+=1
        return maxDiff if (maxDiff!='-inf' and maxDiff>0) else 0