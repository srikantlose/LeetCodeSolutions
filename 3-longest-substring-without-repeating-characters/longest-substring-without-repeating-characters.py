class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R,diff,maxDiff=0,0,0,float('-inf')
        if(s!=""):
         seen=set()
         while R<len(s):
                while s[R] in seen:
                    seen.remove(s[L])
                    L+=1
                seen.add(s[R])
                diff=R-L+1
                maxDiff=max(maxDiff,diff)
                R+=1
            
         return maxDiff if maxDiff!=float('-inf') else 0
        else: 
            return 0
        