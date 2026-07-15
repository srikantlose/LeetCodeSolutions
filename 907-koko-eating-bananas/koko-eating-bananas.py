class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        L,R=1,max(piles)
        minMid=R
        while(L<=R):
            mid=(L+R)//2
            hours=0
            for i in piles:
                hours+=math.ceil(i/mid)
                if hours>h:

                    break
            
            if(hours<=h):
                minMid=mid
                R=mid-1
            else:
                L=mid+1
            
        return minMid          



    # def binarySearch(L,R,arr):
    #     while(L<=R):
    #         mid=(L+R)//2
    #         if isCorrect(mid)>0:
    #             L=mid+1
    #         elif isCorrect(mid)<0:
    #             R=mid-1
    #         else:
    #             return mid
    # def isCorrect(mid):
