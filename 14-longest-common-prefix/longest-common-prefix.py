class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cp=[]
        sample=strs[0]
        flag=0
        minlength=float('inf')
        for i in strs:
            minlength=min(minlength,len(i))
        
        for i in range(minlength):
            for j in strs:
                if sample[i]!=j[i]:
                    flag=1
                else:
                    continue
            if flag==0:
                cp.append(sample[i])
            else:
                break
        return "".join(cp)