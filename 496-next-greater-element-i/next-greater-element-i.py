class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreatest={}
        L=[]
        for i in nums2:
            x=nums2.index(i)
            for j in range(x,len(nums2)):
                if nums2[j]>i:
                    nextE=nums2[j]
                    break
                else:
                    nextE=-1
            nextGreatest[i]=nextE
        
        
        for i in nums1:
            L.append(nextGreatest[i])
        return L



       