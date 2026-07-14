class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sample={}
        for s in strs:
            x="".join(sorted(s))
            if x not in sample:
                sample[x]=[]
            sample[x].append(s)
        L=[]
        for value in sample.values():
            L.append(value)
        return L
        