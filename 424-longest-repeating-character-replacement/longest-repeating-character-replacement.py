class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L,R=0,0
        count={}
        maxResult,curResult=0,0
        while R<len(s):
            diff=R-L+1
            if s[R] not in count:
                count[s[R]]=1
            else:
                count[s[R]]+=1


            if ((diff-max(count.values()))<=k):
                curResult=diff
            else:
                count[s[L]]-=1
                L+=1

            maxResult=max(maxResult,curResult)
            R+=1
        return maxResult