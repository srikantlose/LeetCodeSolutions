class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L,R,count,sum1=0,0,0,0
        target = threshold * k
        while R < len(arr):
            sum1 += arr[R]
            if (R - L + 1) == k:
                if sum1 >= target:
                    count += 1
                sum1 -= arr[L]
                L += 1
            R += 1
            
        return count
        